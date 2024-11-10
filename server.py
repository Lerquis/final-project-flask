from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/')

@app.route('/emotionDetector')
def get_emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    return f"Para la frase data, la respuesta del sistema es 'anger': {response['anger']}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)