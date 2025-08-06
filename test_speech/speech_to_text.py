import requests
import json

import json
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def speech_to_text(file_name):
    api_key = 'tpsBIAnKOzdIfst9hQyqBsPiJFOyuE93K5-Z3QHyt024'
    service_url = "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/90fa4454-30db-4a5e-9b28-8f616e7bfb5d"

    authenticator = IAMAuthenticator(api_key)
    speech_to_text = SpeechToTextV1(authenticator=authenticator)
    speech_to_text.set_service_url(service_url)

    with open(file_name, 'rb') as audio_file:
        response = speech_to_text.recognize(
            audio=audio_file,
            content_type='audio/wav',
            model='en-US_MultimediaModel',
            smart_formatting=True,
            background_audio_suppression=0.6
        ).get_result()

    output = ""
    for r in response.get("results", []):
        for alt in r.get("alternatives", []):
            output += " " + alt.get("transcript", "")

    return output.strip()

