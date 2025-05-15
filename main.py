import time
import random
import keyboard
import pyperclip

def hotkey():
    text = pyperclip.paste()
    for i in text:
        keyboard.write(i)
        time.sleep(random.uniform(.01, .5))


def main():
    keyboard.add_hotkey('ctrl+alt+v', hotkey)
    keyboard.wait()


if __name__ == '__main__':
    main()