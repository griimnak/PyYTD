PyYTD - Python YouTube Downloader
--------------
*TODO:* Add codec / exntension decision (currently only supports MP3/M4A)
![Alt Text](https://image.prntscr.com/image/csBedHDTQm2OEaoYIT93_Q.png)

<b>Python 3.6+</b>
#### Usage

Install 2 requirements, colorama and youtube_dl

```sh
$ pip install -r requirements.txt
```

Launch

```sh
$ python main.py
```

Add youtube URLs to queue

```sh
> queadd https://youtu.be/cuuhsqA95iA
```

Download all in queue or single

```sh
> dl
```


#### Available Commands

help - Displays this dialog.

clear - Clears the console screen.

exit - Exit the PyYTD application.

qadd [link] - Add a link to download que.

dl - Triggers the video downloader.
