# main.py
import sys
import os

# Obtém o diretório do arquivo atual (src/python_transcriber)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Obtém o diretório pai (src)
parent_dir = os.path.dirname(current_dir)
# Adiciona o diretório src ao sys.path
sys.path.insert(0, parent_dir)

# Agora tenta a importação
from python_transcriber.transcriber import Transcriber

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
