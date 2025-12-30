# main.py
from src.python_transcriber.transcriber import Transcriber

def main():
    transcriber = Transcriber(
        model_size="large",
        language="pt"
    )

    text = transcriber.transcribe("data/raw/ICX503 - Aula 08_11 - EST-UFMG (youtube).mp3")
    print("\n📝 Transcrição:")
    print(text)

if __name__ == "__main__":
    main()
