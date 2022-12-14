import json
import os
import random
import time
from datetime import date
import webbrowser


os.chdir("C:/Users/sajji/Code_Files/Reward_points")
data = json.load(open("dictionary.json"))
words = list(data.keys())


def counter():
    with open('counter_timer.txt') as ft:
        counter = int(ft.read())
        with open('counter_timer.txt', 'w') as fh:
            counter += 1
            fh.write(str(counter))
        if counter > 50:
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

        browser = webbrowser.Mozilla("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        browser.open("https://bing.com")
        time.sleep(5)
        while a != 20:
            word = random.choice(contents)
            if word not in remove_list:
                remove_list.append(word)
            elif word in remove_list:
                word = random.choice(contents)
            browser.open("https://bing.com/search?q=%s" % word)
            a += 1
            time.sleep(random.randint(1, 2))
        remove_words(contents, remove_list)


def chrome_browser():
    with open('dictionary.txt') as f:
        contents = f.read()
        contents = contents.lower()
        contents = contents.split("\n")
        remove_list = []
        b = 0

        browser = webbrowser.Chrome("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        browser.open("https://bing.com")
        time.sleep(5)
        while b != 20:
            word = random.choice(contents)
            if word not in remove_list:
                remove_list.append(word)
            elif word in remove_list:
                word = random.choice(contents)
            browser.open("https://bing.com/search?q=%s" % word)
            b += 1
            time.sleep(random.randint(2, 3))
        remove_words(contents, remove_list)


def edge_browser():
    with open('dictionary.txt') as f:
        contents = f.read()
        contents = contents.lower()
        contents = contents.split("\n")
        remove_list = []
        b = 0
        browser = webbrowser.Chrome("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
        browser.open("https://bing.com")
        while b != 50:
            word = random.choice(contents)
            if word not in remove_list:
                remove_list.append(word)
            elif word in remove_list:
                word = random.choice(contents)
            browser.open_new_tab("https://bing.com/search?q=%s" % word)
            b += 1
            time.sleep(random.randint(1, 2))
        remove_words(contents, remove_list)


def remove_words(contents, remove_list):
    keep_list = list(set(contents) - set(remove_list))
    with open('dictionary.txt', 'w') as fa:
        for line in keep_list:
            fa.write(line)
            fa.write("\n")

def main():
    # counter()
    # edge_browser()
    # time.sleep(2)
    # os.system("taskkill /im msedge.exe /f")
           
    # firefox_browser()
    # time.sleep(2)
    # os.system("taskkill /im firefox.exe /f")
           
    # chrome_browser()
    # time.sleep(2)
    # os.system("taskkill /im chrome.exe /f")
        


    webbrowser.open("https://rewards.microsoft.com/")
    browser = webbrowser.Chrome("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
    browser.open("https://rewards.microsoft.com/")
    browser = webbrowser.Chrome("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    browser.open("https://rewards.microsoft.com/")

    today = date.today()
    weekday = today.weekday()

    if weekday == 6 or weekday == 0 or weekday == 1:
        os.system('"C:\\Users\\sajji\\AppData\\Local\\Programs\\twinkle-tray\\Twinkle Tray.exe" --All --Set=0')
        time.sleep(3600)
        os.system('"C:\\Users\\sajji\\AppData\\Local\\Programs\\twinkle-tray\\Twinkle Tray.exe" --All --Set=100')

    
    os.system("taskkill /im cmd.exe /f")


main()
