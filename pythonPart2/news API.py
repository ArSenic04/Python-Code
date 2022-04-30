import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
    speak("News For the day is ");
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=908bedd597f74cc78b76d19db138871e"
    news=requests.get(url).text
    news_dict=json.loads(news)
    print(news_dict["articles"])
    arts= news_dict['articles']
    for articles in arts:
        speak(articles["title"])