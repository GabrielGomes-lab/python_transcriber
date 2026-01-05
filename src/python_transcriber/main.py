from pathlib import Path
from python_transcriber import Transcriber


def main():
    project_root = Path(__file__).parent.parent.parent
    raw_dir = project_root / "data" / "raw"
    output_dir = project_root / "data" / "processed"

    transcriber = Transcriber(
        model_size="large-v3",
        language="pt"
    )

    transcriber.transcribe_directory(raw_dir, output_dir)


if __name__ == "__main__":
    main()
