import pyautogui
from numpy import *
import time
from PIL import ImageGrab, ImageOps


def key_press():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')


# ImageGrab.grab(x, y, x1, y1) creates a square on the screen
# sum of all the pixel would suggest if there is anything on the screen


def hurdle(box_x, box_y, box_x1, box_y1):
    image = ImageGrab.grab(bbox=(box_x, box_y, box_x1, box_y1))
    grey = ImageOps.grayscale(image)
    a = array(grey.getcolors())
    return a.sum()


def main():
    count = 0
    box_x = 530  # 80 pixel away from Dino head
    box_y = 393  # 40 pixel above the ground
    box_y1 = 423  # 10 pixel above the ground
    box_x1 = 560  # 110 pixel away from Dino head

    time.sleep(5)
    pyautogui.click(680, 360)
    while True:
        if hurdle(box_x, box_y, box_x1, box_y1) != 1147 or hurdle(525, box_y, 555, box_y1) != 1147:
            # 1147 is the sum of pixel of square without any hurdles
            # if the bot keep jumping use print(hrdle) and replace 1147 with the most repeted number
            key_press()
            time.sleep(0.05)
        # shifting square as speed increases
        if count > 100 and box_x1<630:
            if count % 20 == 0:
                box_x += 1
                box_x1 += 1
            if count % 75 == 0:
                box_x += 1
                box_x1 += 1

        if count > 900 and box_x1<630:
            if count % 25 == 0:
                box_x += 2
                box_x1 += 2
        count += 1


main()
