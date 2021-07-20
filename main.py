from gtts import gTTS
from playsound import playsound

audio = 'voice.mp3'
language = 'en'
my_text = input(str('Enter text which you want convert into audio: '))
result = gTTS(text=my_text, lang=language, slow=False)

result.save(audio)
playsound(audio)

