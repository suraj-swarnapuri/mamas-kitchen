from abc import ABC, abstractmethod
import logging
import requests
import io

logging.basicConfig(level=logging.INFO)

class Transcriber(ABC):
    @abstractmethod
    def run(self, file_name:str, audio:bytes):
        pass


class LocalTranscriber(Transcriber):
    def __init__(self):
        pass

    def run(self, file_name:str, audio:bytes):
        logging.info("Local Transcriber Running")
        response = requests.post(
            "http://open-ai:8080/v1/audio/transcriptions",
            files={"file": (file_name, audio, "audio/mp4")},
            data={"model": "whisper-1"}
        )

        if response.status_code == 200:
            logging.info("Transcription successful")
            logging.info(response.json()["text"])
        else:
            logging.error(f"Transcription failed with status code {response.status_code}")



class OpenAITranscriber(Transcriber):
    def __init__(self):
        pass
    
    def run(self,file_name:str, audio:bytes):
        logging.info("OpenAI Transcriber")



