import paralleldots

class API:
    def __init__(self):
# Setting your API key
        paralleldots.set_api_key("uDrmRaWPOOoCwm5c1n9qW51jM6oZBr1F9zFr8ut9yw4")
    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response

    def NER_analysis(self,text):
        response = paralleldots.ner(text)
        return response

    def emotion_detect(self,text):
        response = paralleldots.emotion(text)
        return response


