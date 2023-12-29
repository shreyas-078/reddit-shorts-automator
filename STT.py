import whisper
from whisper.utils import get_writer


def make_subtitle():
    model = whisper.load_model("base")  # Base Model of Whisper OpenAI

    result = model.transcribe("assets/text.mp3")  # Text Transcription

    output_dir = "./assets"  # Location of output

    with open("assets/output.srt", "w") as op:
        writer = get_writer("srt", output_dir=output_dir)  # Spits the file here
        writer.write_result(result, op)  # Pass the file object here


make_subtitle()
