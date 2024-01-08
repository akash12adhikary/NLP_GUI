import paralleldots
# Setting your API key

class API:

    def __init__(self):
        paralleldots.set_api_key('IH4OCcC3pwUFU6jRcoyzug4ShpopFEtpLFigQEZImmk')

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response

    def ner_analysis(self,text):
        response=paralleldots.ner(text)
        return response

    def emotion_analysis(self,text):
        import requests
        API_URL = "https://api-inference.huggingface.co/models/SamLowe/roberta-base-go_emotions"
        headers = {"Authorization": "Bearer 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"}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
        output = query({
            "inputs":text
        })
        return output