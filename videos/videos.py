import yt_dlp

def descargar_audio_con_yt_dlp(url: str, nombre_archivo: str = "mi_audio_descargado.mp3"):
    opciones = {
        'format': 'bestaudio/best',
        'outtmpl': nombre_archivo,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
        'noplaylist': True
    }

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            print(f"Descargando audio de: {url}")
            ydl.download([url])
            print(f" Audio descargado como: {nombre_archivo}")
    except Exception as e:
        print(" Ocurrió un error durante la descarga:", e)

url_video = "https://youtu.be/aZwnaCxb-Xo?list=RDaZwnaCxb-Xo"
descargar_audio_con_yt_dlp(url_video)
