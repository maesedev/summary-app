from time import perf_counter
from hooks.is_youtube_url import is_youtube_url
from hooks.get_youtube_audio import get_youtube_audio
from hooks.get_video_audio import get_video_audio
import os


def get_audio(request):

    start = perf_counter()
    url = request.headers.get('url')

    print(f"file exists --> {os.path.exists('audio.mp3')}")
    if os.path.exists("audio.mp3"):
        print("removing audio")
        os.remove("audio.mp3")

    if url is None:
        return 'No se proporcionó una URL en los headers', 400

    if is_youtube_url(url):
        try:
            get_youtube_audio(url)
        except Exception as e:
            return f"Error al procesar el video \n{e}"
        end = perf_counter()
        return f'Video procesado correctamente en {round(end - start,3)}s'
        
    try:
        get_video_audio(url)
        end = perf_counter()
        return f'Video procesado correctamente en {round(end - start,3)}s'
    
    except Exception as e:
        return f'Video procesado con Error {e}', 500
