"""
    Este modulo funciona para llamar al servidor de flask y todas sus funcionalidades
"""


from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/')
def index():
    """
        Esta funcion sirve para renderizar el index html para cuando el usuario entra a la
        pagina
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def get_emotion_detector():
    """
        Esta funcion sirve para que cuando el usuario llena el formulario, se llame
        esta funcion y pueda realizar su funcionalidad de analizar el texto
        insertado por el usuario
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return 'Entrada invalida.'

    return f"Para la frase data, la respuesta del sistema es 'anger': " \
    f"{response['anger']}, 'disgust': {response['disgust']}, 'fear': " \
    f"{response['fear']}, 'joy': {response['joy']} y 'sadness': " \
    f"{response['sadness']}. La emoción dominante es {response['dominant_emotion']}."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
