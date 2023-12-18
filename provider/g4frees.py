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
                    {"role": "user", "content": f"{themessage} IMPORTANT: Don't write another shits except your thoughts(1 sentence) and answer of the user's question(after thought 1 sentence. not related to thought): >> {user_message} <<"}
                ],
            )

            formatted_response = "".join(response)
            return formatted_response
        except Exception as e:
            raise ValueError(f"Error generating response: {e}")
