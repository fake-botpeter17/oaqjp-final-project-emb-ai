from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__, static_folder="static")

def find_max(res):
    current_max_name = ""
    current_max_number = 0
    for emotion in res:
        if res[emotion] >= current_max_number:
            current_max_name = emotion
            current_max_number = res[emotion]
    return current_max_name

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector")
def detector():
    text = request.args.get("textToAnalyze")
    result = emotion_detector(text)
    return result | {"dominant_emotion":find_max(result)}

if __name__ == "__main__":
    app.run(debug=True, port = 5000)