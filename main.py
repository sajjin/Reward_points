#!/usr/bin/python3
import json
import os
import random
import time
import webbrowser
import PySimpleGUI as sg
import cv2
import pyautogui
import numpy as np

# Load the image of the object you want to detect
template = cv2.imread('object.png', 0)
w, h = template.shape[::-1]

start_time = time.time()
os.chdir("/home/rewards/Documents/Reward_points-master")
data = json.load(open("dictionary.json"))
words = list(data.keys())


def counter():
    with open('counter_timer.txt') as ft:
        counter = int(ft.read())
        with open('counter_timer.txt', 'w') as fh:
            counter += 1
            fh.write(str(counter))
        if counter == 49:
            with open('dictionary.txt', 'w') as fs:
                for line in words:
                    fs.write(line)
                    fs.write("\n")
            with open('counter_timer.txt', 'w') as fh:
                fh.write("0")


def firefox_browser():
    with open('dictionary.txt') as f:
        contents = f.read()
        contents = contents.lower()
        contents = contents.split("\n")
        remove_list = []
        a = 0

        browser = webbrowser.Mozilla("/snap/bin/firefox")
        browser.open("https://bing.com")
        time.sleep(5)
        while a != 40:
            word = random.choice(contents)
            if word not in remove_list:
                remove_list.append(word)
            elif word in remove_list:
                word = random.choice(contents)
            if a == 20:
                os.system("kill $(pidof firefox)")
                time.sleep(3)
            browser.open("https://bing.com/search?q=%s" % word)
            a += 1
            time.sleep(random.randint(5, 10))
        remove_words(contents, remove_list)


def edge_browser():
    with open('dictionary.txt') as f:
        contents = f.read()
        contents = contents.lower()
        contents = contents.split("\n")
        remove_list = []
        b = 0
        browser = webbrowser.Chrome("/opt/microsoft/msedge/msedge")
        browser.open("https://bing.com")
        while b != 60:
            word = random.choice(contents)
            if word not in remove_list:
                remove_list.append(word)
            elif word in remove_list:
                word = random.choice(contents)
            time.sleep(5)
            if b == 30:
                os.system("kill $(pidof msedge)")
                time.sleep(5)
            # Take a screenshot
            screenshot = pyautogui.screenshot()
            screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
            screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
            # Perform template matching
            res = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.8
            loc = np.where(res >= threshold)
            # Click and type on the detected object
            for pt in zip(*loc[::-1]):
                pyautogui.click(pt[0] + w/2, pt[1] + h/2)
                pyautogui.write(word)
                pyautogui.press('enter')
            browser.open_new_tab(home_url) # replace home_url with the URL of the home page
            b += 1
            time.sleep(random.randint(5, 10))
        remove_words(contents, remove_list)


def remove_words(contents, remove_list):
    keep_list = list(set(contents) - set(remove_list))
    with open('dictionary.txt', 'w') as fa:
        for line in keep_list:
            fa.write(line)
            fa.write("\n")

def GUI():
    layout = [
        [sg.Button("Run PC only")],
        [sg.Button("Run Mobile only")]
    ]

    window = sg.Window("Rewards", layout)
    while True:
        event, values = window.read(timeout = 1000 * 15)
        print(event, values)
        if event in ('__TIMEOUT__',):
            window.close()
            edge_browser()
            time.sleep(10)
            os.system("kill $(pidof msedge)")

            firefox_browser()
            time.sleep(10)
            os.system("kill $(pidof firefox)")
            
            os.system("shutdown")
        elif event == sg.WIN_CLOSED:
            window.close()
            break
        elif event == "Run PC only":
            window.close()
            edge_browser()
            time.sleep(10)
            os.system("kill $(pidof msedge)")
            os.system("shutdown")
            break
        elif event == "Run Mobile only":
            window.close()
            firefox_browser()
            time.sleep(10)
            os.system("kill $(pidof firefox)")
            os.system("shutdown")
            break
        

def main():
    counter()
    GUI()

if __name__ == '__main__':
    main()
