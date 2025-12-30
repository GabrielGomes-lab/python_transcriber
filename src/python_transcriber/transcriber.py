# transcriber.py
import whisper
from python_transcriber.utils import AudioLoader

class Transcriber:
    def __init__(self, model_size: str = "base", language: str = "pt"):
        self.language = language
        self.model = whisper.load_model(model_size)

    def transcribe(self, audio_path: str) -> str:
        audio = AudioLoader.load(audio_path)

        result = self.model.transcribe(
            str(audio),
            language=self.language
        )

        return result["text"]
