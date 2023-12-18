from fastapi import FastAPI

from strings import themessage
#from provider.g4frees import G4Frees
from provider.lexica import LexicaProvider  

app = FastAPI()
#provider_instance = G4Frees()
provider_instance = LexicaProvider()

@app.post("/api/deebisi/")
def deebisi_endpoint(user_message: str):
    try:
        question = themessage + " IMPORTANT: Don't write another shits except your thoughts(1 sentence) and answer of the user's question(after thought 1 sentence. not related to thought): >> " + user_message + " <<"
        
        # Use Provider instance to send request
        ai_response = provider_instance.send_request(question)

        json_response = {"response_code": 200, "message": ai_response}
        return json_response
    except Exception as e:
        error_message = f"Error processing message: {e}"
        json_error_response = {"response_code": 500, "message": error_message}
        return json_error_response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
