from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

def find_max(res):
    current_max_name = ""
    current_max_number = 0
    for emotion in res:
        if res[emotion] >= current_max_number:
            current_max_name = emotion
            current_max_number = res[emotion]
    return current_max_name

@app.route("/emotionDetector")
def home():
    text = request.data
    res = emotion_detector(text)
    return res | {"dominant_emotion":find_max(res)}


if __name__ == "__main__":
    app.run(port = 5000)