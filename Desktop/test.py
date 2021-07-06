from gtts import gTTS
from playsound import playsound
import os
mytext = 'こんにちは、私はドドックマン'
myobj = gTTS(text= mytext, lang ='ja', slow = False)
myobj.save("py.mp3")
playsound("py.mp3")