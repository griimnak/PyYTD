import os
import time
from colorama import init
from colorama import Fore, Back, Style
from source.downloader import PyYTD

init(autoreset=True)
_pretty = Style.DIM + Fore.CYAN
_count = 0
_queue = dict()

os.system("cls" if os.name == "nt" else "clear")
print(_pretty + "Welcome to PyYTD".center(60))
print(_pretty + "Python YouTube Downloader".center(60))
print(_pretty + "https://github.com/griimnak\n".center(60))

def add_to_queue(link):
    global _count
    _count += 1
    if link != "":
        _queue[f'url{_count}'] = link
        print(f"\n{link} Successfully added to que list.\n")
        print(_pretty+ f"(There are now {_count} urls queued.)\n")
        query_inputs()
    else:
        print(_pretty + "Please enter a valid link to add to queue.\n")
        query_inputs()

def trigger_download():
    global _queue, _count

    if not _queue:
        print("\nQueue is empty, resorting to individual download mode.\n")
        link = input("Video link: ")
        dl = PyYTD(link)
        dl.download_video()
    elif _queue:
        stop_watch = time.time()
        for url in _queue.items():
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
    _queue = dict()
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
        print(_pretty+ "qadd :link: - Add a link to download que.")
        print(_pretty+ "dl - Triggers the video downloader.\n")
        query_inputs()
    elif _cmd == "clear":
        os.system("cls" if os.name == "nt" else "clear")
        query_inputs()
    elif _cmd == "exit":
        print(_pretty + "Thanks for using PyYTD.\n")
        exit()

    elif _cmd[:4] == "qadd":
        link = _cmd.replace(_cmd[:5], "")
        add_to_queue(link)

    elif _cmd == "dl":
        trigger_download()

    elif _cmd == "" or " ":
        print(_pretty + "Please enter a valid command.\n")
        query_inputs()

