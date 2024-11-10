import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }  # Crear un diccionario con el texto a analizar
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Establecer los encabezados requeridos para la solicitud API
    response = requests.post(url, json = myobj, headers=header)  # Enviar una solicitud POST a la API con el texto y los encabezados
    
    formatted_response = json.loads(response.text)

    emotions = {
        'anger': formatted_response['emotionPredictions'][0]['emotion']['anger'],
        'disgust': formatted_response['emotionPredictions'][0]['emotion']['disgust'],  
        'fear': formatted_response['emotionPredictions'][0]['emotion']['fear'],  
        'joy': formatted_response['emotionPredictions'][0]['emotion']['joy'],  
        'sadness': formatted_response['emotionPredictions'][0]['emotion']['sadness'],
    }

    dominant_emotion = max(emotions, key=emotions.get)

    final_response = {
        **emotions,
        'dominant_emotion':dominant_emotion
    }
    
    return final_response  # Devolver el texto de respuesta de la API
