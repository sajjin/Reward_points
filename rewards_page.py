import time
from pyautogui import click
import config
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome("C:\\Users\\sajji\\Code_Files\\Reward_points\\chromedriver.exe")

def OneAns(points):
    index = 1
    while int(driver.find_element(By.XPATH, "//span[@class='rqPoints']/span[@class='rqEarnedPoints']/span[@class='rqECredits']").text) != points:
            a = driver.find_element(By.XPATH, f"//div[@class='textBasedMultiChoice']/div[{index}]")
            a.click()
            index += 1
    

def FiveAns(points):
    index = 1
    while int(driver.find_element(By.XPATH, "//span[@class='rqPoints']/span[@class='rqEarnedPoints']/span[@class='rqECredits']").text) != points:
        a = driver.find_element(By.XPATH, f"//div[@class='btOptions']/div[{index}]")
        a.click()
        time.sleep(.5)
        index += 1
    

def rewards():
    c = driver.current_window_handle
    parent = driver.window_handles[0]
    driver.find_element(By.XPATH, "/html[@class='ltr rewards-dashboard rewards js picture eventlistener k-webkit k-webkit106']/body/div[@id='page-wrapper']/div[@id='main-content-landing']/main[@id='rewards-dashboard']/div[@id='app-host']/ui-view[@class='ng-scope']/mee-rewards-dashboard[@class='ng-scope ng-isolate-scope']/main[@id='rewardsAngular']/div[@class='rewardsContent']/mee-rewards-daily-set-section[@class='ng-scope ng-isolate-scope']/div[@id='daily-sets']/mee-card-group[@class='ng-scope ng-isolate-scope mobileViewMode']/div[@class='m-card-group']/mee-card[@class='ng-scope ng-isolate-scope c-card f-double']/div[@class='c-card-content']/card-content[@class='ng-scope']/mee-rewards-daily-set-item-content[@class='ng-isolate-scope']/div[@class='text-align-center rewards-card-container min-dimension']/a[@class='ds-card-sec ng-scope']/div[@class='actionLink x-hidden-vp1']/span[@class='pointLink ng-binding']").click()

    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(c)

    driver.find_element(By.XPATH, "/html[@class='ltr rewards-dashboard rewards js picture eventlistener k-webkit k-webkit106']/body/div[@id='page-wrapper']/div[@id='main-content-landing']/main[@id='rewards-dashboard']/div[@id='app-host']/ui-view[@class='ng-scope']/mee-rewards-dashboard[@class='ng-scope ng-isolate-scope']/main[@id='rewardsAngular']/div[@class='rewardsContent']/mee-rewards-daily-set-section[@class='ng-scope ng-isolate-scope']/div[@id='daily-sets']/mee-card-group[@class='ng-scope ng-isolate-scope mobileViewMode']/div[@class='m-card-group']/mee-card[@class='ng-scope ng-isolate-scope c-card f-single'][1]/div[@class='c-card-content']/card-content[@class='ng-scope']/mee-rewards-daily-set-item-content[@class='ng-isolate-scope']/div[@class='text-align-center rewards-card-container min-dimension']/a[@class='ds-card-sec ng-scope']/div[@class='actionLink x-hidden-vp1']/span[@class='pointLink ng-binding']").click()

    time.sleep(2)
    chld = driver.window_handles[1]
    driver.switch_to.window(chld)
    time.sleep(1)

    try: # this is to press the sign in button if there
        driver.find_element(By.XPATH,"/html/body[@class='b_respl']/div[@class='simpleSignIn']/div[@class='signInOptions']/span[@class='identityOption']/a").click()
    except: # this is to press the start quiz if it dosent as for the sign in botton
        time.sleep(2)
    finally:
        time.sleep(2)
        driver.find_element(By.ID,"rqStartQuiz").click()

    try: # this is fot the five answer correct questions
        WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='btOptions']/div[@class='slide']")))
        count_of_filled_circles =  driver.find_element(By.XPATH, "//span[@class='btCorOps']/span[@class='bt_corOpStat']/span[@id='bt_corOpCnt']")
        print(count_of_filled_circles)
        i = 0
        points = 0
        while i != 3:
            points += 10
            FiveAns(points)
            i += 1
            time.sleep(8)
        driver.close()

    except: # this is for the one answer correct questions
        WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='textBasedMultiChoice']/div[@class='rq_button']")))
        count_of_filled_circles =  driver.find_element(By.XPATH, "//span[@class='rqPoints']/span[@class='rqEarnedPoints']/span[@class='rqECredits']")
        print(count_of_filled_circles)
        points = 0
        i = 0
        while i != 3:
            points += 10
            OneAns(points)
            i += 1
            time.sleep(8)
        driver.close()
    finally:
    
        driver.switch_to.window(parent)

        driver.find_element(By.XPATH, "/html[@class='ltr rewards-dashboard rewards js picture eventlistener k-webkit k-webkit106']/body/div[@id='page-wrapper']/div[@id='main-content-landing']/main[@id='rewards-dashboard']/div[@id='app-host']/ui-view[@class='ng-scope']/mee-rewards-dashboard[@class='ng-scope ng-isolate-scope']/main[@id='rewardsAngular']/div[@class='rewardsContent']/mee-rewards-daily-set-section[@class='ng-scope ng-isolate-scope']/div[@id='daily-sets']/mee-card-group[@class='ng-scope ng-isolate-scope mobileViewMode']/div[@class='m-card-group']/mee-card[@class='ng-scope ng-isolate-scope c-card f-single'][2]/div[@class='c-card-content']/card-content[@class='ng-scope']/mee-rewards-daily-set-item-content[@class='ng-isolate-scope']/div[@class='text-align-center rewards-card-container min-dimension']").click()

        chld = driver.window_handles[1]
        driver.switch_to.window(chld)

        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='bt_poll']/div[@class='btOptions2 bt_pollOptions']/div[@id='btoption0']").click()

        time.sleep(2)
        driver.close()


def main():
    driver.get("https://rewards.microsoft.com/")
    driver.find_element(By.ID,"raf-signin-link-id").click()
    time.sleep(1)
    username = driver.find_element("name", "loginfmt")
    username.send_keys(config.login_reward)
    driver.find_element(By.ID,"idSIButton9").click()
    password = driver.find_element("name", "passwd")
    password.send_keys(config.password_reward)
    time.sleep(.5)
    driver.find_element(By.ID,"idSIButton9").click()
    time.sleep(.5)
    driver.find_element(By.ID,"idSIButton9").click()
    rewards()
    driver.quit()

    driver.get("https://rewards.microsoft.com/")
    driver.find_element(By.ID,"raf-signin-link-id").click()
    time.sleep(1)
    username = driver.find_element("name", "loginfmt")
    username.send_keys(config.login_gmail)
    driver.find_element(By.ID,"idSIButton9").click()
    password = driver.find_element("name", "passwd")
    password.send_keys(config.password_gmail)
    time.sleep(.5)
    driver.find_element(By.ID,"idSIButton9").click()
    time.sleep(.5)
    driver.find_element(By.ID,"idSIButton9").click()
    rewards()
    driver.quit()

    driver.get("https://rewards.microsoft.com/")
    driver.find_element(By.ID,"raf-signin-link-id").click()
    time.sleep(1)
    username = driver.find_element("name", "loginfmt")
    username.send_keys(config.login_outlook)
    driver.find_element(By.ID,"idSIButton9").click()
    password = driver.find_element("name", "passwd")
    password.send_keys(config.password_outlook)
    time.sleep(.5)
    driver.find_element(By.ID,"idSIButton9").click()
    time.sleep(.5)
    driver.find_element(By.ID,"idSIButton9").click()
    rewards()

main()