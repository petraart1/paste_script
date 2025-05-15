import time
import random
import keyboard
import pyperclip


def main():
    text = pyperclip.paste()
    for i in text:
        keyboard.write(i)
        time.sleep(random.uniform(.01, .5))


if __name__ == '__main__':
    main()