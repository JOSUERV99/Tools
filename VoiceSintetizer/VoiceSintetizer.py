"""
@objective: get text, create a .mp3 with it and later play it
@author: josuerv99
@since: 07/04/2020
"""
from gtts import gTTS
import playsound as player
import io

txt_filename = 'Example.txt'
mp3_filename = 'file://Example.mp3'

def getTextFromFile(filename='Example.txt'):
    text = ''
    with io.open(filename, mode="r", encoding="utf-8") as f:
        text = f.read()
    return text

def saveAudioFromText(pText, filename='Example.mp3'):
    file = gTTS(text=pText, lang='ES')
    file.save(filename)


def playSound(filename='file:Example.mp3'):
    player.playsound(filename, True)

print("Getting text from file")
text = getTextFromFile()
print("Generating .mp3 file")
saveAudioFromText(text)
print('Playing')
playSound(mp3_filename)
print('Finished!')


