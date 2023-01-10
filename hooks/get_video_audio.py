import youtube_dl
def get_video_audio(url):
    ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': 'audio.mp3',
                'quiet': True,
            }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])