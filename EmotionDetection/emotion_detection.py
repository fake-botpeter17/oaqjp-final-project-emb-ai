import requests, json

def emotion_detector(text_to_analyse):
    URL = r"https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    response = requests.post(url=URL, headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}, json = { "raw_document": { "text": text_to_analyse } })
    res_json: dict = json.loads(response.text)
    emotions = res_json.get("emotionPredictions")[0]
    return emotions.get("emotion")