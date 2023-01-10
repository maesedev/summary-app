from pytube import YouTube
    

def get_youtube_audio(url):
    yt = YouTube(url)
    flujo_audio = yt.streams.filter(only_audio=True).first()
    flujo_audio.download(filename="audio.mp3")
    return
