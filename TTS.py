import os
from pydub import AudioSegment


text = ""

command = f"say {text} -o assets/text.aiff"


def convert_aiff_to_mp3(input_path, output_path):
    # Load the AIFF file
    audio = AudioSegment.from_file(input_path, format="aiff")

    # Export the audio to MP3 format
    audio.export(output_path, format="mp3")


os.system(command=command)
input_file = "assets/text.aiff"
output_file = "assets/text.mp3"
convert_aiff_to_mp3(input_file, output_file)
