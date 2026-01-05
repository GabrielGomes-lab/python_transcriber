from pathlib import Path
from faster_whisper import WhisperModel


class Transcriber:
    def __init__(
        self,
        model_size: str = "large-v3",
        language: str = "pt",
        device: str = "cpu",
        compute_type: str = "int8",
        cpu_threads: int = 12,
    ):
        self.language = language

        print(f"Carregando modelo Whisper ({model_size})...")
        self.model = WhisperModel(
            model_size,
            device=device,
            compute_type=compute_type,
            cpu_threads=cpu_threads,
        )

    def transcribe_file(self, audio_path: Path, output_path: Path) -> None:
        print(f"Transcrevendo: {audio_path.name}")

        segments, info = self.model.transcribe(
            str(audio_path),
            language=self.language,
            vad_filter=False,
            beam_size=2,
            chunk_length=90,
        )

        with open(output_path, "w", encoding="utf-8") as f:
            for segment in segments:
                text = segment.text.strip()
                print(f"[{segment.start:.2f} - {segment.end:.2f}] {text}", flush=True)
                f.write(text + "\n")

        print(f"✔ Transcrição salva em: {output_path}")
        print(f"⏱ Duração do áudio: {info.duration:.2f}s\n")

    def transcribe_directory(self, raw_dir: Path, output_dir: Path) -> None:
        output_dir.mkdir(parents=True, exist_ok=True)

        for audio_path in raw_dir.glob("*.m4a"):
            output_path = output_dir / f"{audio_path.stem}_transcricao.txt"
            self.transcribe_file(audio_path, output_path)

