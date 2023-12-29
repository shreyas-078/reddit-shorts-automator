# Reddit Stories YT Shorts Automator
A Python Application which can create YT Shorts of Reddit Stories instantly.

Libraries Used: 
1. MoviePy
2. OpenAI Whisper
3. SRT 

Pre-Requisites: (Only works on UNIX based systems)
1. Need a Background Video, place it in the assets folder with the name ```input.mp4```
2. Need to place a story in the ```TTS.py``` file without brackets () or quotes ( ' )

How to Use:
1. Once the pre requisites are done, run the TTS.py file and it should output a ```text.mp3``` file with your audio.
2. Then Run the ```STT.py``` file to reverse the process and convert speech back to text in an SRT format, saved as ```ouput.srt``` in the assets folder.
3. If needed, edit the SRT file and remove any subtitle errors.
4. Then run the shorts.py file to create a video file, ready with the given background video and subtitles according to the TTS.
5. Upload and Enjoy!
