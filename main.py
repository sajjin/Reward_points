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

os.chdir("/home/rewards/Documents/Reward_points-master/")
template = cv2.imread('assets/object.png',0)
w, h = template.shape[::-1]

start_time = time.time()
data = json.load(open("assets/dictionary.json"))
words = list(data.keys())

def move_and_click(x, y):
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.3))
    pyautogui.click()

def counter():
    with open('assets/counter_timer.txt') as ft:
        counter = int(ft.read())
        with open('assets/counter_timer.txt', 'w') as fh:
            counter += 1
            fh.write(str(counter))
        if counter == 49:
            with open('assets/dictionary.txt', 'w') as fs:
                for line in words:
                    fs.write(line)
                    fs.write("\n")
            with open('assets/counter_timer.txt', 'w') as fh:
                fh.write("0")

def firefox_browser():
    with open('assets/dictionary.txt') as f:
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
    with open('assets/dictionary.txt') as f:
        contents = f.read()
        contents = contents.lower()
        contents = contents.split("\n")
        remove_list = []
        b = 0
        browser = webbrowser.Chrome("/opt/microsoft/msedge/msedge")
        browser.open("https://bing.com")
        template = cv2.imread('assets/object.png',0)
        w, h = template.shape[::-1]
        while b != 60:
            word = random.choice(contents)
            if word not in remove_list:
                remove_list.append(word)
            elif word in remove_list:
                word = random.choice(contents)
            time.sleep(5)
            try:
                screenshot = pyautogui.screenshot()
            except:
                screenshot = pyautogui.screenshot()
            screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
            screenshot_grey = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
            res = cv2.matchTemplate(screenshot_grey, template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.8
            loc = np.where(res >= threshold)
            for pt in zip(*loc[::-1]):
                move_and_click(pt[0] - 20, pt[1])
                pyautogui.write(word)
                time.sleep(1)
                if b == 0:
                    pyautogui.press('enter')
                move_and_click(pt[0] - 100, pt[1] + 100)
            time.sleep(random.randint(1, 5))
            template = cv2.imread('assets/mic.png',0)
            w, h = template.shape[::-1]
            b += 1
            time.sleep(random.randint(5, 10))
        remove_words(contents, remove_list)

def remove_words(contents, remove_list):
    keep_list = list(set(contents) - set(remove_list))
    with open('assets/dictionary.txt', 'w') as fa:
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