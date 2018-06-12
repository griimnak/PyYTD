import os
import time
from colorama import init
from colorama import Fore, Back, Style
from source.downloader import PyYTD

init(autoreset=True)
_pretty = Style.DIM + Fore.CYAN
_count = 0
_que = dict()

os.system("cls" if os.name == "nt" else "clear")
print(_pretty + "Welcome to PyYTD".center(60))
print(_pretty + "Python YouTube Downloader".center(60))
print(_pretty + "https://github.com/griimnak\n".center(60))

def add_to_que(link):
    global _count
    _count += 1
    if link != "":
        _que[f'url{_count}'] = link
        print(f"\n{link} Successfully added to que list.\n")
        print(_pretty+ f"(There are now {_count} urls qued.)\n")
        query_inputs()
    else:
        print(_pretty + "Please enter a valid link to add to que.\n")
        query_inputs()

def trigger_download():
    global _que, _count

    if not _que:
        print("\nQue is empty, resorting to individual download mode.\n")
        link = input("Video link: ")
        dl = PyYTD(link)
        dl.download_video()
    elif _que:
        stop_watch = time.time()
        for url in _que.items():
            print(
                Style.DIM + Back.GREEN + Fore.WHITE +
                "\n==> Working on " + url[1] + Style.RESET_ALL
            )
            #link = input("Video link: ")
            dl = PyYTD(url[1])
            dl.download_video()
        print(
            _pretty +
            f"\nFinished {_count} requests in {time.time() - stop_watch}s\n"
        )

    """ Clean up """
    _count = 0
    _que = dict()
    query_inputs()

""" Query inputs """
def query_inputs():
    _cmd = input(
        Back.CYAN +
        Fore.WHITE +
        "(type help for command list) >" +
        Style.RESET_ALL + " "
    )

    if _cmd == "help":
        print(_pretty+ "help - Displays this dialog.")
        print(_pretty+ "clear - Clears the console screen.")
        print(_pretty+ "exit - Exit the PyYTD application.")
        print(_pretty+ "queadd :link: - Add a link to download que.")
        print(_pretty+ "dl - Triggers the video downloader.\n")
        query_inputs()
    elif _cmd == "clear":
        os.system("cls" if os.name == "nt" else "clear")
        query_inputs()
    elif _cmd == "exit":
        print(_pretty + "Thanks for using PyYTD.\n")
        exit()

    elif _cmd[:6] == "queadd":
        link = _cmd.replace(_cmd[:7], "")
        add_to_que(link)

    elif _cmd == "dl":
        trigger_download()

    elif _cmd == "" or " ":
        print(_pretty + "Please enter a valid command.\n")
        query_inputs()

