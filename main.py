import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

"""
    pip install pyaudio
    pip install pydub
    pip install pandas
    pip install gTTS
"""
def textToSpeechInEng(text, filename):
    """
    this is just to conversion
    """
    mytext = str(text)
    language = 'en-in'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)

def textToSpeech(text, filename):
    """
    this is just to conversion
    """
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)


def mergeAudios(audios):
    """
    This fn returns pydubs audio segment
    """
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    """
    This will cut audio into pieces
    """
    audio = AudioSegment.from_mp3('railway.mp3')
    # 1- Generate Kripya dhyan dijiye
    start = 88000
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format="mp3")

    # 2- is from-city

    # 3- Generate se chalkar
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format="mp3")

    # 4- is via-city
    
    # 5- Generate ke raste
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format="mp3")

    # 6- is to-city

    # 7- Generate ko jaane wali gaadi sankhya
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3")

    # 8- Train number and name

    # 9- Generate kch hi samay mein platform sankhya
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format="mp3")

    # 10- Platform number
    
    # 11- Generate par aa rahi hai
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3", format="mp3")

    # 12- Generate May i have......train number
    start = 157000
    finish = 162500
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_english.mp3", format="mp3")

    # 13- train number and name of train

    # 14- Generate from
    start = 168700
    finish = 169800
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_english.mp3", format="mp3")

    # 15- from station

    # 16- Generate to
    start = 170400
    finish = 171100
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_english.mp3", format="mp3")

    # 17- to station

    # 18- Generate  Via
    start = 171800
    finish = 173300
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_english.mp3", format="mp3")

    # 19- via station

    # 20- Generate is arriving shortly......number
    start = 174800
    finish = 179000
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_english.mp3", format="mp3")

    # 21- p.f. number

def generateAnnouncement(filename):
    """
    docstring
    """
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2- is from-city
        textToSpeech(item['from'], '2_hindi.mp3')
        # 4- is via-city
        textToSpeech(item['via'], '4_hindi.mp3')
        # 6- is to-city
        textToSpeech(item['to'], '6_hindi.mp3')
        # 8- Train number and name
        textToSpeech(item['train_no'] + "   " + item['train_name'], '8_hindi.mp3')
        # 10- Platform number
        textToSpeech(item['platform'], '10_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1,12)]
        
        # 13- train number and name of train
        textToSpeechInEng(item['train_no'] + "   " + item['train_name'], '2_english.mp3')
        # 15- from station
        textToSpeechInEng(item['from'], '4_english.mp3')
        # 17- to station
        textToSpeechInEng(item['to'], '6_english.mp3')
        # 19- via station
        textToSpeechInEng(item['via'], '8_english.mp3')
        # 21- p.f. number
        textToSpeechInEng(item['platform'], '10_english.mp3')
        
        eng_audio = [f"{i}_english.mp3" for i in range(1,11)]
        audios.extend(eng_audio)

        announcement = mergeAudios(audios)
        announcement.export(f'announcement_{item["train_no"]}_{index+1}.mp3', format='mp3')

if __name__ == "__main__":
    print("Generating Skeletons...")
    generateSkeleton()
    print("Now generating Announcement...")
    generateAnnouncement("announce_hindi.xlsx")
