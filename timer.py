import os
import sys
import time as t

from pygame import mixer

mixer.init()

BASE_DIR = (
    os.path.dirname(sys.executable)
    if getattr(sys, "frozen", False)
    else os.path.dirname(os.path.abspath(__file__))
)

symbols = {
    "0": ["       ", " @ @ @ ", " @   @ ", " @   @ ", " @   @ ", " @ @ @ ", "       "],
    "1": ["     ", "  @@ ", " @ @ ", "   @ ", "   @ ", "   @ ", "     "],
    "2": ["       ", " @ @ @ ", "     @ ", " @ @ @ ", " @     ", " @ @ @ ", "       "],
    "3": ["       ", " @ @ @ ", "     @ ", " @ @ @ ", "     @ ", " @ @ @ ", "       "],
    "4": ["       ", " @   @ ", " @   @ ", " @ @ @ ", "     @ ", "     @ ", "       "],
    "5": ["       ", " @ @ @ ", " @     ", " @ @ @ ", "     @ ", " @ @ @ ", "       "],
    "6": ["       ", " @ @ @ ", " @     ", " @ @ @ ", " @   @ ", " @ @ @ ", "       "],
    "7": ["       ", " @ @ @ ", "    @  ", "   @   ", "  @    ", " @     ", "       "],
    "8": ["       ", " @ @ @ ", " @   @ ", " @ @ @ ", " @   @ ", " @ @ @ ", "       "],
    "9": ["       ", " @ @ @ ", " @   @ ", " @ @ @ ", "     @ ", " @ @ @ ", "       "],
    ":": ["       ", "       ", "   @   ", "       ", "   @   ", "       ", "       "],
}


def play_alarm():
    mixer.music.load(os.path.join(BASE_DIR, "media", "timeout.mp3"))
    mixer.music.play()


def play_ticking():
    mixer.music.load(os.path.join(BASE_DIR, "media", "ticking.mp3"))
    mixer.music.play(loops=-1)


def print_time(time):
    print("\n\033[92m")
    for i in range(7):
        print("\n", end="")
        for j in time:
            print(symbols[j][i], end=" ")
    print("\n\n\033[0m")


def is_correctformat(lst: list):
    if len(lst) == 3 and all([i.strip().isdigit() for i in lst]):
        return True
    return False


def timer():
    os.system("cls")
    msg = ""

    while True:
        os.system("cls")
        print(
            "\n\n\n\033[93mEnter the time in format : HH.MM.SS | 'q' to quit\n\n\033[0m"
        )
        print(msg)
        T = "0:0:0".split(":")
        time = input("\n\033[96m>>> \033[0m").strip()

        if time.lower() == "q":
            msg = "\n\033[34mThanks for using the Timer\n"
            break

        time = time.split(".")
        if not is_correctformat(time):
            msg = "\033[31mError: Invalid time format\033[0m"
            continue

        while True:
            play_ticking()
            try:
                for i in range(
                    int(time[0]) * 60 * 60 + int(time[1]) * 60 + int(time[2]), -1, -1
                ):
                    os.system("cls")

                    tm = f"{i // 3600}:{(i % 3600) // 60}:{(i % 3600) % 60}"

                    print_time(tm)
                    print("\n\n\033[93mPress Ctrl+C to stop the timer\033[0m\n")

                    T = tm.split(":")
                    t.sleep(0.9999)

                print("\n\033[31mTIME IS UP !!!")

                mixer.music.stop()
                play_alarm()

                input(
                    "\n\033[33mThe alarm will automaticlly be stoped in 30 seconds.\n\n\033[0mPress \033[93mEnter\033[0m to Reset..."
                )

                mixer.music.stop()
                break

            except KeyboardInterrupt:
                mixer.music.stop()
                time = T
                resume = False
                while True:
                    os.system("cls")
                    print_time(":".join(time))

                    print(
                        "\033[93mTimer Paused\033[0m\n\n'r' : to Resume the timer\n'q' : to reset the timer\n\n"
                    )

                    i = input("\033[96m>>> \033[0m").strip()

                    if i.lower() == "r":
                        resume = True
                        break

                    if i.lower() == "q":
                        break

                if not resume:
                    break
            msg=""


if __name__ == "__main__":
    timer()