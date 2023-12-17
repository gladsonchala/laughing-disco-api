from fastapi import FastAPI
from provider.g4frees import G4Frees

app = FastAPI()
g4frees_instance = G4Frees()

@app.post("/api/deebisi/")
def deebisi_endpoint(user_message: str):
    try:
        response = g4frees_instance.process_message(user_message)
        json_response = {"response_code": 200, "message": response}
        return json_response
    except Exception as e:
        error_message = f"Error processing message: {e}"
        json_error_response = {"response_code": 500, "message": error_message}
        return json_error_response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
