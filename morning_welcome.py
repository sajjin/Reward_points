    
import webbrowser
from datetime import date
import mouse
import screen_brightness_control as sbc



def main():
    webbrowser.open("https://rewards.microsoft.com/")
    browser = webbrowser.Chrome("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
    browser.open("https://rewards.microsoft.com/")
    browser = webbrowser.Chrome("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    browser.open("https://rewards.microsoft.com/")
    today = date.today()
    weekday = today.weekday()

    if weekday == 6 or weekday == 0 or weekday == 1:
        sbc.set_brightness(0)
        mouse.wait(button='left', target_types=('up', 'down', 'right', 'left'))
        sbc.set_brightness(100)
    


if __name__ == '__main__':
    main()