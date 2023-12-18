import g4f
from strings import themessage

class G4Frees:
    def __init__(self):
        self.model = g4f.models.default

    def send_request(self, user_message):
        try:
            response = g4f.ChatCompletion.create(
                model=self.model,
                provider=g4f.Provider.HuggingChat,
                messages=[
                    {"role": "user", "content": user_message}
                ],
            )

            formatted_response = "".join(response)
            return formatted_response
        except Exception as e:
            raise ValueError(f"Error generating response: {e}")
