# utils.py
from pathlib import Path

class AudioLoader:
    @staticmethod
    def load(path: str) -> Path:
        audio_path = Path(path)

        if not audio_path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {path}")

        return audio_path
