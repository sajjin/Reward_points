import time
import json
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

os.chdir("C:\\Users\\sajji\\Code_Files\\Reward_points")

f = open('login_info.json')

c = driver.current_window_handle
parent = driver.window_handles[0]

def close_child_tab():
        chld = driver.window_handles[1]
        driver.switch_to.window(chld)
        time.sleep(3)
        driver.close()
        driver.switch_to.window(parent)


def OneAns(points):
    index = 1
    while int(driver.find_element(By.XPATH, "//span[@class='rqPoints']/span[@class='rqEarnedPoints']/span[@class='rqECredits']").text) != points:
        time.sleep(1)
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
        time.sleep(1)
        try: 
            driver.find_element(By.XPATH, "//div[@id='b_notificationContainer_bop']/span[@id='bnp_hfly_cta2']").click()
        except Exception:
            pass
        a = driver.find_element(By.XPATH, f"//div[@class='btOptions']/div[{index}]")
        a.click()
        time.sleep(1)
        index += 1


def checker(value):
    driver.switch_to.window(parent)

    first_button = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[1]/div/card-content/mee-rewards-daily-set-item-content/div/a/mee-rewards-points/div/div/span[1]")
    
    second_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[2]/div/card-content/mee-rewards-daily-set-item-content/div/a/mee-rewards-points/div/div/span[1]")

    third_button = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[3]/div/card-content/mee-rewards-daily-set-item-content/div/a/mee-rewards-points/div/div/span[1]")

    first_button_x = first_button.get_attribute("class").split()
    second_button_x = second_button.get_attribute("class").split()
    third_button_x = third_button.get_attribute("class").split()

    for i in first_button_x:
        if i == "mee-icon-AddMedium":
            first_button_x = i
        elif i == 'mee-icon-SkypeCircleCheck':
            first_button_x = i

    for i in second_button_x:
        if i == "mee-icon-AddMedium":
            second_button_x = i
        elif i == 'mee-icon-SkypeCircleCheck':
            second_button_x = i

    for i in third_button_x:
        if i == "mee-icon-AddMedium":
            third_button_x = i
        elif i == 'mee-icon-SkypeCircleCheck':
            third_button_x = i

    a = 1

    while first_button_x == "mee-icon-AddMedium" or second_button_x == "mee-icon-AddMedium" or third_button_x == "mee-icon-AddMedium":
        driver.refresh()

        first_button = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[1]/div/card-content/mee-rewards-daily-set-item-content/div/a/mee-rewards-points/div/div/span[1]")
        
        second_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[2]/div/card-content/mee-rewards-daily-set-item-content/div/a/mee-rewards-points/div/div/span[1]")

        third_button = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[3]/div/card-content/mee-rewards-daily-set-item-content/div/a/mee-rewards-points/div/div/span[1]")
       

        first_button_x = first_button.get_attribute("class").split()
        second_button_x = second_button.get_attribute("class").split()
        third_button_x = third_button.get_attribute("class").split()

        

        for i in first_button_x:
            if i == "mee-icon-AddMedium":
                first_button_x = i
            elif i == 'mee-icon-SkypeCircleCheck':
                first_button_x = i

        for i in second_button_x:
            if i == "mee-icon-AddMedium":
                second_button_x = i
            elif i == 'mee-icon-SkypeCircleCheck':
                second_button_x = i

        for i in third_button_x:
            if i == "mee-icon-AddMedium":
                third_button_x = i
            elif i == 'mee-icon-SkypeCircleCheck':
                third_button_x = i
        
        print(f"{value[0]}, check {a}\n {first_button_x}\n {second_button_x}\n {third_button_x}\n")

        if "mee-icon-AddMedium" in first_button.get_attribute("class").split():
            first_daily_task()
            time.sleep(2)

        if "mee-icon-AddMedium" in second_button.get_attribute("class").split():
            secound_daily_task()
            time.sleep(2)
        
        if "mee-icon-AddMedium" in third_button.get_attribute("class").split():
            final_daily_task()
        a += 1
    if first_button_x == 'mee-icon-SkypeCircleCheck' and second_button_x == 'mee-icon-SkypeCircleCheck' and third_button_x == 'mee-icon-SkypeCircleCheck':
        return True
    

def first_daily_task():
    try:
        driver.switch_to.window(parent)
    except Exception:
        pass
    driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[1]/div/card-content/mee-rewards-daily-set-item-content/div/a").click()

    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(parent)


def secound_daily_task():
    try:
        driver.switch_to.window(parent)
    except Exception:
        pass
    
    pointer_checker = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[2]/div/card-content/mee-rewards-daily-set-item-content/div/a/mee-rewards-points/div/div/span[2]").text

    if int(pointer_checker) == 10 or int(pointer_checker) == 50:
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[2]/div/card-content/mee-rewards-daily-set-item-content/div/a").click()

        driver.switch_to.window(driver.window_handles[1])
    else:
        
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[2]/div/card-content/mee-rewards-daily-set-item-content/div/a").click()

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
                time.sleep(2)

        try: # this is fot the five answer correct questions
            WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='btOptions']/div[@class='slide']")))
            points = int(driver.find_element(By.XPATH, "//span[@class='rqPoints']/span[@class='rqEarnedPoints']/span[@class='rqECredits']").text)
            time.sleep(8)
            while points != 30:
                points += 10
                FiveAns(points)
                time.sleep(8)
        except Exception: # this is for the one answer correct questions
            WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='textBasedMultiChoice']/div[@class='rq_button']")))
            points = int(driver.find_element(By.XPATH, "//span[@class='rqPoints']/span[@class='rqEarnedPoints']/span[@class='rqECredits']").text)
            time.sleep(8)
            while points != 30:
                points += 10
                OneAns(points)
                time.sleep(8)
    driver.close()
    driver.switch_to.window(parent)


def final_daily_task():
    try:
        driver.switch_to.window(parent)
    except Exception:
        pass
   
    driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[3]/div/card-content/mee-rewards-daily-set-item-content/div/a").click()
    try: # this is to press the sign in button if there
        time.sleep(2)
        chld = driver.window_handles[1]
        driver.switch_to.window(chld)
    except Exception:
        pass
    finally:
        time.sleep(2)
        try:
            try:
                driver.find_element(By.XPATH,"/html/body[@class='b_respl']/div[@class='simpleSignIn']/div[@class='signInOptions']/span[@class='identityOption']/a").click()
            except Exception:
                driver.find_element(By.ID,"id_a").click()
        except Exception:
             pass
        try:
            time.sleep(2)
            driver.find_element(By.XPATH, "//div[@class='bt_poll']/div[@class='btOptions2 bt_pollOptions']/div[@id='btoption0']").click()
        except Exception:
            pass
        finally:
            time.sleep(10)
            driver.close()
    driver.switch_to.window(parent)


def extra_activities():
    driver.switch_to.window(parent)
    
    try:
            
        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[1]/div/card-content/mee-rewards-more-activities-card-item/div/a").click()
        close_child_tab()
    except Exception:
        pass

    try:    
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[2]/div/card-content/mee-rewards-more-activities-card-item/div/a").click()
        close_child_tab()
    except Exception:
        pass

    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[3]/div/card-content/mee-rewards-more-activities-card-item/div/a").click()
        close_child_tab()
    except Exception:
        pass

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
        time.sleep(4)
        a = checker(value)
        extra_activities()
        if a == True:
            driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div/div[2]/a[2]").click()
            driver.find_element(By.XPATH,"//a[@href='/Signout']").click()
        time.sleep(8)
    
    driver.quit()
    os.system("taskkill /im chromedriver.exe /f")


if __name__ == '__main__':

    main()