from moviepy.editor import TextClip, VideoFileClip, CompositeVideoClip, AudioFileClip
from moviepy.video.tools.subtitles import SubtitlesClip
import srt


def make_video():
    # Function to convert SRT time to seconds
    def srt_to_seconds(srt_time):
        return srt_time.total_seconds()

    with open("assets/output.srt", "r") as f:
        srt_content = f.read()

    # Parse SRT content
    subs = list(srt.parse(srt_content))

    # Convert SRT subtitles to MoviePy format
    subs_moviepy = [
        ((srt_to_seconds(sub.start), srt_to_seconds(sub.end)), sub.content)
        for sub in subs
    ]

    video = VideoFileClip("assets/input.mp4").subclip((1, 0), (1, 56))

    generator = lambda txt: TextClip(
        txt,
        font="Montserrat",
        fontsize=60,
        color="white",
        method="caption",
        stroke_width=2,
        stroke_color="black",
        size=(700, 500),
    )

    subtitles = SubtitlesClip(subs_moviepy, generator)

    # Create a CompositeVideoClip without audio
    result = CompositeVideoClip([video, subtitles.set_position(("center", "center"))])

    result.write_videofile(
        "output/output.mp4",
        fps=video.fps,
        temp_audiofile="temp-audio.m4a",
        remove_temp=True,
        codec="libx264",
        audio_codec="aac",
    )


def add_audio():
    audio = AudioFileClip("assets/text.mp3")
    video1 = VideoFileClip("output/output.mp4")
    final = video1.set_audio(audio)

    final.write_videofile("output/output-final.mp4")


make_video()
add_audio()
