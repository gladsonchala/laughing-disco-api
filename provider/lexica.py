import requests
import json

class LexicaProvider:
    def __init__(self):
        self.url = "https://lexica.qewertyy.me/models/"
        self.model_id = 20

    def send_request(self, text):
        params = {'model_id': self.model_id, 'prompt': text}
        response = requests.post(self.url, params=params)
        parsed_response = json.loads(response.text)
        content = parsed_response["content"]
        return content

