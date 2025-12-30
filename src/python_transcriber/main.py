# main.py
from src.python_transcriber.transcriber import Transcriber

def main():
    transcriber = Transcriber(
        model_size="large",
        language="pt"
    )

    text = transcriber.transcribe("data/raw/Gravando.m4a")
    print("\n📝 Transcrição:")
    print(text)

if __name__ == "__main__":
    main()
