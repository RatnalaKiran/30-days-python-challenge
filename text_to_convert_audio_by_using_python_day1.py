from gtts import gTTS
from playsound3 import playsound
text = "my first project"
audio = gTTS(text=text, lang='en')
audio.save("output.mp3")
playsound("output.mp3")
print("Audio generarted Successfully!")