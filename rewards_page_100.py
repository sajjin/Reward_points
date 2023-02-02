import time
import os
import json
import keyboard
import threading
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import PySimpleGUI as sg

sg.ChangeLookAndFeel('Dark')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

f = open('login_info.json')

c = driver.current_window_handle
parent = driver.window_handles[0]

def OneAns(points):
    index = 1
    while int(driver.find_element(By.XPATH, "//span[@class='rqPoints']/span[@class='rqEarnedPoints']/span[@class='rqECredits']").text) != points:
        try: 
            driver.find_element(By.XPATH, "//div[@id='b_notificationContainer_bop']/span[@id='bnp_hfly_cta2']").click()
        except Exception:
            pass
        a = driver.find_element(By.XPATH, f"//div[@class='textBasedMultiChoice']/div[{index}]")
        a.click()
        index += 1
    

def FiveAns(points):
    index = 1
    while int(driver.find_element(By.XPATH, "//span[@class='rqPoints']/span[@class='rqEarnedPoints']/span[@class='rqECredits']").text) != points:
        try: 
            driver.find_element(By.XPATH, "//div[@id='b_notificationContainer_bop']/span[@id='bnp_hfly_cta2']").click()
        except Exception:
            pass
        a = driver.find_element(By.XPATH, f"//div[@class='btOptions']/div[{index}]")
        a.click()
        time.sleep(1)
        index += 1


def secound_daily_task():
    try:
        driver.switch_to.window(parent)
    except Exception:
        pass

    try:

        actions = ActionChains(driver)
        
        try:
            e = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-punch-cards/div/mee-carousel/div/div[1]/div/button[1]")
            actions.move_to_element(e).perform()
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-punch-cards/div/mee-carousel/div/div[1]/div/button[1]").click()
        except Exception:
            pass
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-punch-cards/div/mee-carousel/div/div[2]/ul/li[1]/a/mee-hero-item/section/div").click()
        time.sleep(10)

        time.sleep(2)
        chld = driver.window_handles[1]
        driver.switch_to.window(chld)
        time.sleep(1)

        try: # this is to press the sign in button if there
            driver.find_element(By.XPATH,"/html/body[@class='b_respl']/div[@class='simpleSignIn']/div[@class='signInOptions']/span[@class='identityOption']/a").click()
        except Exception: # this is to press the start quiz if it dosent as for the sign in botton
            pass
        try:
            driver.find_element(By.ID, "id_a").click()
        except Exception:
            pass
        finally:
            try:
                time.sleep(2)
                driver.find_element(By.ID,"rqStartQuiz").click()
            except Exception:
                pass

        try: # this is fot the five answer correct questions
            WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='btOptions']/div[@class='slide']")))
            points = 0
            time.sleep(8)
            for i in range(0, 10):
                points += 10
                FiveAns(points)
                time.sleep(8)
            driver.close()
        except Exception: # this is for the one answer correct questions
            WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='textBasedMultiChoice']/div[@class='rq_button']")))
            points = 0
            time.sleep(8)
            for i in range(0, 10):
                points += 10
                OneAns(points)
                time.sleep(8)
            driver.close()
    except Exception:
        pass
    chld = driver.window_handles[1]
    driver.switch_to.window(chld)
    driver.close()
    driver.switch_to.window(parent)

def main():
    data = json.load(f)
    driver.get("https://rewards.microsoft.com/")
    for key in data:
        value = data[key]
        driver.find_element(By.ID,"raf-signin-link-id").click()
        time.sleep(1)
        username = driver.find_element("name", "loginfmt")
        username.send_keys(value[0])
        driver.find_element(By.ID,"idSIButton9").click()
        time.sleep(1)
        password = driver.find_element("name", "passwd")
        password.send_keys(value[1])
        time.sleep(1)
        driver.find_element(By.ID,"idSIButton9").click()
        time.sleep(1)
        driver.find_element(By.ID,"idSIButton9").click()
        time.sleep(5)
        secound_daily_task()
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div/div[2]/a[2]").click()
        driver.find_element(By.XPATH,"//a[@href='/Signout']").click()
        time.sleep(8)
        
    
    driver.quit()
    os.system("taskkill /im chromedriver.exe /f")


if __name__ == '__main__':

    main()