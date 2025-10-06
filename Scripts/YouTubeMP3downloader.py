import os
import time

import yt_dlp

def download_audio_from_youtube(url, output_path=f"./downloads/session_{int(time.time())}"):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    ydl_opts = {
        'format': 'bestaudio/best',                # выбираем лучшее аудио
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # название файла = название видео
        'noplaylist': False,                       # разрешаем плейлисты
        'extractaudio': True,
        'audioformat': 'mp3',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',             # качество звука
        }],
        'quiet': False,                            # можно сделать True если хочешь тишину
        'progress_hooks': [lambda d: print(f"⬇️ {d['filename']}") if d['status'] == 'downloading' else None]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = input("🎧 Вставь ссылку на видео или плейлист YouTube: ").strip()
    download_audio_from_youtube(url)
