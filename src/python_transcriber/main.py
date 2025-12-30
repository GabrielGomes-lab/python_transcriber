import sys
import os
from pathlib import Path

# Adiciona o diretório src ao caminho de busca
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from python_transcriber.transcriber import Transcriber

def main():
    project_root = Path(__file__).parent.parent.parent
    audio_path = project_root / "data" / "raw" / "Gravando.m4a"
    
    print(f"Procurando áudio em: {audio_path}")
    
    if not audio_path.exists():
        print(f"ERRO: Arquivo não encontrado em {audio_path}")
        return
    
    print("Carregando modelo Whisper (pode levar alguns minutos para o modelo 'base')...")
    transcriber = Transcriber(
        model_size='base',  # Considere usar 'base' ou 'small' para teste
        language='pt'
    )
    
    print("Transcrevendo áudio...")
    try:
        text = transcriber.transcribe(str(audio_path))
        print("\n" + "="*50)
        print("► TRANSCRIÇÃO:")
        print("="*50)
        print(text)
        print("="*50)
    except Exception as e:
        print(f"ERRO durante transcrição: {e}")

if __name__ == "__main__":
    main()