from fastapi import FastAPI
from provider.g4frees import G4Frees
from provider.lexica import LexicaProvider  # Import the LexicaProvider class

app = FastAPI()
g4frees_instance = G4Frees()
lexica_instance = LexicaProvider()

@app.post("/api/deebisi/")
def deebisi_endpoint(user_message: str):
    try:
        # Use LexicaProvider
        lexica_response = lexica_instance.send_request(user_message)

        # Use G4Frees provider
        g4frees_response = g4frees_instance.send_request(user_message)

        # Return a JSON response of both responses
        json_response = {"response_code": 200, "lexica_message": lexica_response, "g4frees_message": g4frees_response}
        return json_response
    except Exception as e:
        error_message = f"Error processing message: {e}"
        json_error_response = {"response_code": 500, "message": error_message}
        return json_error_response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
