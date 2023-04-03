import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS


def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)

def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio =  AudioSegment.from_mp3('Railway.mp3')
    start = 1000
    finish =2000
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3",format="mp3")
    
    audio =  AudioSegment.from_mp3('Railway.mp3')
    start = 8000
    finish =9000
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3",format="mp3")
    
    audio =  AudioSegment.from_mp3('Railway.mp3')
    start = 9000
    finish =11000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3",format="mp3")
    
    audio =  AudioSegment.from_mp3('Railway.mp3')
    start = 11000
    finish =16000
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3",format="mp3")
    
    audio =  AudioSegment.from_mp3('Railway.mp3')
    start = 16000
    finish =22000
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3",format="mp3")
    
    audio =  AudioSegment.from_mp3('Railway.mp3')
    start = 22000
    finish =29000
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3",format="mp3")

def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index,item in df.iterrows():
        textToSpeech(item['from'], '2_hindi.mp3')
        textToSpeech(item['via'], '4_hindi.mp3')
        textToSpeech(item['to'], '6_hindi.mp3')
        textToSpeech(item['train_no'] + " " + item['train_name'], '8_hindi.mp3')
        textToSpeech(item['platform'], '10_hindi.mp3')
        
        audios = [f"{i}_hindi.mp3" for i in range(1,12)]
        
        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format="mp3")

if __name__=="__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement("announce_hindi.xlsx")