from pydub import AudioSegment
if __name__ == "__main__":
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 174800
    finish = 179000
    audioProcessed = audio[start:finish]
    audioProcessed.export("check1.mp3", format="mp3")