from __future__ import unicode_literals
import youtube_dl
from colorama import Fore, Back, Style

class PyYTD:
    def __init__(self, link=""):
        self._link = link

    def download_video(self):
        ydl_opts = {
            'writethumbnail': True,
            'format': 'bestaudio/best',
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                },
                {'key': 'FFmpegMetadata'},
                {'key': 'EmbedThumbnail'}
            ],
            'outtmpl': 'output/%(title)s.%(ext)s'
        }
        if self._link:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                try:
                    ydl.download([self._link])
                except:
                    print(
                        Style.DIM + Back.RED + Fore.WHITE +
                        f"\n==> FAILURE {self._link} Failed!"
                    )

                    pass
