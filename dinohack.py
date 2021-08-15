import pyautogui
from PIL import Image, ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)

def isCollide(data):
    for x in range(250, 440):
        for y in range(390, 450):
            if (data[x, y] <= 207 and data[x, y] >= 127) or (data[x, y] < 100 and data[x, y] > 10):
                return True
    return False

if __name__ == "__main__":
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("Go")
    time.sleep(1)

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        if isCollide(data):
            hit("up")


