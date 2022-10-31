import time
import config
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

c = driver.current_window_handle
parent = driver.window_handles[0]

def OneAns(points):
    index = 1
    while int(driver.find_element(By.XPATH, "//span[@class='rqPoints']/span[@class='rqEarnedPoints']/span[@class='rqECredits']").text) != points:
        try: 
            driver.find_element(By.XPATH, "//div[@id='b_notificationContainer_bop']/span[@id='bnp_hfly_cta2']").click()
        except:
            time.sleep(.05)
        a = driver.find_element(By.XPATH, f"//div[@class='textBasedMultiChoice']/div[{index}]")
        a.click()
        index += 1
    

def FiveAns(points):
    index = 1
    while int(driver.find_element(By.XPATH, "//span[@class='rqPoints']/span[@class='rqEarnedPoints']/span[@class='rqECredits']").text) != points:
        try: 
            driver.find_element(By.XPATH, "//div[@id='b_notificationContainer_bop']/span[@id='bnp_hfly_cta2']").click()
        except:
            time.sleep(.05)
        a = driver.find_element(By.XPATH, f"//div[@class='btOptions']/div[{index}]")
        a.click()
        time.sleep(.5)
        index += 1

def checker():
    driver.switch_to.window(parent)
    first_button = driver.find_element(By.XPATH,"/html[@class='ltr rewards-dashboard rewards js picture eventlistener k-webkit k-webkit107']/body/div[@id='page-wrapper']/div[@id='main-content-landing']/main[@id='rewards-dashboard']/div[@id='app-host']/ui-view[@class='ng-scope']/mee-rewards-dashboard[@class='ng-scope ng-isolate-scope']/main[@id='rewardsAngular']/div[@class='rewardsContent']/mee-rewards-daily-set-section[@class='ng-scope ng-isolate-scope']/div[@id='daily-sets']/mee-card-group[@class='ng-scope ng-isolate-scope mobileViewMode']/div[@class='m-card-group']/mee-card[@class='ng-scope ng-isolate-scope c-card f-double']/div[@class='c-card-content']/card-content[@class='ng-scope']/mee-rewards-daily-set-item-content[@class='ng-isolate-scope']/div[@class='text-align-center rewards-card-container min-dimension']/a[@class='ds-card-sec ng-scope']/mee-rewards-points[@class='ng-isolate-scope']/div[@class='points clearfix']/div[@class='ng-scope']/span[1]")
        
    second_button = driver.find_element(By.XPATH, "/html[@class='ltr rewards-dashboard rewards js picture eventlistener k-webkit k-webkit107']/body/div[@id='page-wrapper']/div[@id='main-content-landing']/main[@id='rewards-dashboard']/div[@id='app-host']/ui-view[@class='ng-scope']/mee-rewards-dashboard[@class='ng-scope ng-isolate-scope']/main[@id='rewardsAngular']/div[@class='rewardsContent']/mee-rewards-daily-set-section[@class='ng-scope ng-isolate-scope']/div[@id='daily-sets']/mee-card-group[@class='ng-scope ng-isolate-scope mobileViewMode']/div[@class='m-card-group']/mee-card[@class='ng-scope ng-isolate-scope c-card f-single'][1]/div[@class='c-card-content']/card-content[@class='ng-scope']/mee-rewards-daily-set-item-content[@class='ng-isolate-scope']/div[@class='text-align-center rewards-card-container min-dimension']/a[@class='ds-card-sec ng-scope']/mee-rewards-points[@class='ng-isolate-scope']/div[@class='points clearfix']/div[@class='ng-scope']/span[1]")

    third_button = driver.find_element(By.XPATH,"/html[@class='ltr rewards-dashboard rewards js picture eventlistener k-webkit k-webkit107']/body/div[@id='page-wrapper']/div[@id='main-content-landing']/main[@id='rewards-dashboard']/div[@id='app-host']/ui-view[@class='ng-scope']/mee-rewards-dashboard[@class='ng-scope ng-isolate-scope']/main[@id='rewardsAngular']/div[@class='rewardsContent']/mee-rewards-daily-set-section[@class='ng-scope ng-isolate-scope']/div[@id='daily-sets']/mee-card-group[@class='ng-scope ng-isolate-scope mobileViewMode']/div[@class='m-card-group']/mee-card[@class='ng-scope ng-isolate-scope c-card f-single'][2]/div[@class='c-card-content']/card-content[@class='ng-scope']/mee-rewards-daily-set-item-content[@class='ng-isolate-scope']/div[@class='text-align-center rewards-card-container min-dimension']/a[@class='ds-card-sec ng-scope']/mee-rewards-points[@class='ng-isolate-scope']/div[@class='points clearfix']/div[@class='ng-scope']/span[1]")

    first_button_x = first_button.get_attribute("class").split()
    second_button_x = second_button.get_attribute("class").split()
    third_button_x = third_button.get_attribute("class").split()

    for i in first_button_x:
        if i == "mee-icon-AddMedium":
            first_button_x = i
        elif i == 'mee-icon-SkypeCircleCheck':
            first_button_x = i
    print(first_button_x)

    for i in second_button_x:
        if i == "mee-icon-AddMedium":
            second_button_x = i
        elif i == 'mee-icon-SkypeCircleCheck':
            second_button_x = i
    print(second_button_x)

    for i in third_button_x:
        if i == "mee-icon-AddMedium":
            third_button_x = i
        elif i == 'mee-icon-SkypeCircleCheck':
            third_button_x = i
    print(third_button_x)

    while first_button_x == "mee-icon-AddMedium" or second_button_x == "mee-icon-AddMedium" or third_button_x == "mee-icon-AddMedium":
        driver.refresh()

        first_button = driver.find_element(By.XPATH,"/html[@class='ltr rewards-dashboard rewards js picture eventlistener k-webkit k-webkit107']/body/div[@id='page-wrapper']/div[@id='main-content-landing']/main[@id='rewards-dashboard']/div[@id='app-host']/ui-view[@class='ng-scope']/mee-rewards-dashboard[@class='ng-scope ng-isolate-scope']/main[@id='rewardsAngular']/div[@class='rewardsContent']/mee-rewards-daily-set-section[@class='ng-scope ng-isolate-scope']/div[@id='daily-sets']/mee-card-group[@class='ng-scope ng-isolate-scope mobileViewMode']/div[@class='m-card-group']/mee-card[@class='ng-scope ng-isolate-scope c-card f-double']/div[@class='c-card-content']/card-content[@class='ng-scope']/mee-rewards-daily-set-item-content[@class='ng-isolate-scope']/div[@class='text-align-center rewards-card-container min-dimension']/a[@class='ds-card-sec ng-scope']/mee-rewards-points[@class='ng-isolate-scope']/div[@class='points clearfix']/div[@class='ng-scope']/span[1]")
        
        second_button = driver.find_element(By.XPATH, "/html[@class='ltr rewards-dashboard rewards js picture eventlistener k-webkit k-webkit107']/body/div[@id='page-wrapper']/div[@id='main-content-landing']/main[@id='rewards-dashboard']/div[@id='app-host']/ui-view[@class='ng-scope']/mee-rewards-dashboard[@class='ng-scope ng-isolate-scope']/main[@id='rewardsAngular']/div[@class='rewardsContent']/mee-rewards-daily-set-section[@class='ng-scope ng-isolate-scope']/div[@id='daily-sets']/mee-card-group[@class='ng-scope ng-isolate-scope mobileViewMode']/div[@class='m-card-group']/mee-card[@class='ng-scope ng-isolate-scope c-card f-single'][1]/div[@class='c-card-content']/card-content[@class='ng-scope']/mee-rewards-daily-set-item-content[@class='ng-isolate-scope']/div[@class='text-align-center rewards-card-container min-dimension']/a[@class='ds-card-sec ng-scope']/mee-rewards-points[@class='ng-isolate-scope']/div[@class='points clearfix']/div[@class='ng-scope']/span[1]")

        third_button = driver.find_element(By.XPATH,"/html[@class='ltr rewards-dashboard rewards js picture eventlistener k-webkit k-webkit107']/body/div[@id='page-wrapper']/div[@id='main-content-landing']/main[@id='rewards-dashboard']/div[@id='app-host']/ui-view[@class='ng-scope']/mee-rewards-dashboard[@class='ng-scope ng-isolate-scope']/main[@id='rewardsAngular']/div[@class='rewardsContent']/mee-rewards-daily-set-section[@class='ng-scope ng-isolate-scope']/div[@id='daily-sets']/mee-card-group[@class='ng-scope ng-isolate-scope mobileViewMode']/div[@class='m-card-group']/mee-card[@class='ng-scope ng-isolate-scope c-card f-single'][2]/div[@class='c-card-content']/card-content[@class='ng-scope']/mee-rewards-daily-set-item-content[@class='ng-isolate-scope']/div[@class='text-align-center rewards-card-container min-dimension']/a[@class='ds-card-sec ng-scope']/mee-rewards-points[@class='ng-isolate-scope']/div[@class='points clearfix']/div[@class='ng-scope']/span[1]")

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

        if "mee-icon-AddMedium" in first_button.get_attribute("class").split():
            first_daily_task()
            time.sleep(2)

        if "mee-icon-AddMedium" in second_button.get_attribute("class").split():
            secound_daily_task()
            time.sleep(2)
        
        if "mee-icon-AddMedium" in third_button.get_attribute("class").split():
            final_daily_task()
    if first_button_x == 'mee-icon-SkypeCircleCheck' and second_button_x == 'mee-icon-SkypeCircleCheck' and third_button_x == 'mee-icon-SkypeCircleCheck':
        return True
    

def first_daily_task():
    try:
        driver.switch_to.window(parent)
    except:
        time.sleep(.05)
    driver.find_element(By.XPATH, "/html[@class='ltr rewards-dashboard rewards js picture eventlistener k-webkit k-webkit107']/body/div[@id='page-wrapper']/div[@id='main-content-landing']/main[@id='rewards-dashboard']/div[@id='app-host']/ui-view[@class='ng-scope']/mee-rewards-dashboard[@class='ng-scope ng-isolate-scope']/main[@id='rewardsAngular']/div[@class='rewardsContent']/mee-rewards-daily-set-section[@class='ng-scope ng-isolate-scope']/div[@id='daily-sets']/mee-card-group[@class='ng-scope ng-isolate-scope mobileViewMode']/div[@class='m-card-group']/mee-card[@class='ng-scope ng-isolate-scope c-card f-double']/div[@class='c-card-content']/card-content[@class='ng-scope']/mee-rewards-daily-set-item-content[@class='ng-isolate-scope']/div[@class='text-align-center rewards-card-container min-dimension']/a[@class='ds-card-sec ng-scope']/div[@class='actionLink x-hidden-vp1']/span[@class='pointLink ng-binding']").click()

    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(parent)


def secound_daily_task():
    try:
        driver.switch_to.window(parent)
    except:
        time.sleep(.05)
    pointer_checker = driver.find_element(By.XPATH, "/html[@class='ltr rewards-dashboard rewards js picture eventlistener k-webkit k-webkit107']/body/div[@id='page-wrapper']/div[@id='main-content-landing']/main[@id='rewards-dashboard']/div[@id='app-host']/ui-view[@class='ng-scope']/mee-rewards-dashboard[@class='ng-scope ng-isolate-scope']/main[@id='rewardsAngular']/div[@class='rewardsContent']/mee-rewards-daily-set-section[@class='ng-scope ng-isolate-scope']/div[@id='daily-sets']/mee-card-group[@class='ng-scope ng-isolate-scope mobileViewMode']/div[@class='m-card-group']/mee-card[@class='ng-scope ng-isolate-scope c-card f-single'][1]/div[@class='c-card-content']/card-content[@class='ng-scope']/mee-rewards-daily-set-item-content[@class='ng-isolate-scope']/div[@class='text-align-center rewards-card-container min-dimension']/a[@class='ds-card-sec ng-scope']/mee-rewards-points[@class='ng-isolate-scope']/div[@class='points clearfix']/div[@class='ng-scope']/span[@class='c-heading pointsString ng-binding ng-scope']").text

    if int(pointer_checker) == 10:
        driver.find_element(By.XPATH, "/html[@class='ltr rewards-dashboard rewards js picture eventlistener k-webkit k-webkit107']/body/div[@id='page-wrapper']/div[@id='main-content-landing']/main[@id='rewards-dashboard']/div[@id='app-host']/ui-view[@class='ng-scope']/mee-rewards-dashboard[@class='ng-scope ng-isolate-scope']/main[@id='rewardsAngular']/div[@class='rewardsContent']/mee-rewards-daily-set-section[@class='ng-scope ng-isolate-scope']/div[@id='daily-sets']/mee-card-group[@class='ng-scope ng-isolate-scope mobileViewMode']/div[@class='m-card-group']/mee-card[@class='ng-scope ng-isolate-scope c-card f-single'][1]/div[@class='c-card-content']/card-content[@class='ng-scope']/mee-rewards-daily-set-item-content[@class='ng-isolate-scope']/div[@class='text-align-center rewards-card-container min-dimension']/a[@class='ds-card-sec ng-scope']/div[@class='actionLink x-hidden-vp1']/span[@class='pointLink ng-binding']").click()

        driver.switch_to.window(driver.window_handles[1])
        driver.close()
    
    elif int(pointer_checker) == 50:
        final_daily_task()

    else:
        driver.find_element(By.XPATH, "/html[@class='ltr rewards-dashboard rewards js picture eventlistener k-webkit k-webkit107']/body/div[@id='page-wrapper']/div[@id='main-content-landing']/main[@id='rewards-dashboard']/div[@id='app-host']/ui-view[@class='ng-scope']/mee-rewards-dashboard[@class='ng-scope ng-isolate-scope']/main[@id='rewardsAngular']/div[@class='rewardsContent']/mee-rewards-daily-set-section[@class='ng-scope ng-isolate-scope']/div[@id='daily-sets']/mee-card-group[@class='ng-scope ng-isolate-scope mobileViewMode']/div[@class='m-card-group']/mee-card[@class='ng-scope ng-isolate-scope c-card f-single'][1]/div[@class='c-card-content']/card-content[@class='ng-scope']/mee-rewards-daily-set-item-content[@class='ng-isolate-scope']/div[@class='text-align-center rewards-card-container min-dimension']/a[@class='ds-card-sec ng-scope']/div[@class='actionLink x-hidden-vp1']/span[@class='pointLink ng-binding']").click()

        time.sleep(2)
        chld = driver.window_handles[1]
        driver.switch_to.window(chld)
        time.sleep(1)

        try: # this is to press the sign in button if there
            driver.find_element(By.XPATH,"/html/body[@class='b_respl']/div[@class='simpleSignIn']/div[@class='signInOptions']/span[@class='identityOption']/a").click()
        except: # this is to press the start quiz if it dosent as for the sign in botton
            time.sleep(.05)
        try:
            driver.find_element(By.ID, "id_a").click()
        except:
            time.sleep(.05)
        finally:
            try:
                time.sleep(2)
                driver.find_element(By.ID,"rqStartQuiz").click()
            except:
                time.sleep(2)

        try: # this is fot the five answer correct questions
            WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='btOptions']/div[@class='slide']")))
            count_of_filled_circles =  driver.find_element(By.XPATH, "//span[@class='btCorOps']/span[@class='bt_corOpStat']/span[@id='bt_corOpCnt']")
            print(count_of_filled_circles)
            i = 0
            x = 3
            points = 0
            time.sleep(8)
            while i != x:
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
            x = 3
            time.sleep(8)
            while i != x:
                points += 10
                OneAns(points)
                i += 1
                time.sleep(8)
            driver.close()
    driver.switch_to.window(parent)


def final_daily_task():

    try:
        driver.switch_to.window(parent)
    except:
        time.sleep(1)
    driver.find_element(By.XPATH, "/html[@class='ltr rewards-dashboard rewards js picture eventlistener k-webkit k-webkit107']/body/div[@id='page-wrapper']/div[@id='main-content-landing']/main[@id='rewards-dashboard']/div[@id='app-host']/ui-view[@class='ng-scope']/mee-rewards-dashboard[@class='ng-scope ng-isolate-scope']/main[@id='rewardsAngular']/div[@class='rewardsContent']/mee-rewards-daily-set-section[@class='ng-scope ng-isolate-scope']/div[@id='daily-sets']/mee-card-group[@class='ng-scope ng-isolate-scope mobileViewMode']/div[@class='m-card-group']/mee-card[@class='ng-scope ng-isolate-scope c-card f-single'][2]/div[@class='c-card-content']/card-content[@class='ng-scope']/mee-rewards-daily-set-item-content[@class='ng-isolate-scope']/div[@class='text-align-center rewards-card-container min-dimension']").click()
    try: # this is to press the sign in button if there
        chld = driver.window_handles[1]
        driver.switch_to.window(chld)
        driver.find_element(By.XPATH,"/html/body[@class='b_respl']/div[@class='simpleSignIn']/div[@class='signInOptions']/span[@class='identityOption']/a").click()
    except:
        time.sleep(.05)
    finally:
        time.sleep(2)
        try:
            driver.find_element(By.XPATH, "//div[@class='bt_poll']/div[@class='btOptions2 bt_pollOptions']/div[@id='btoption0']").click()
        except:
            time.sleep(.05)
        finally:
            time.sleep(2)
            driver.close()
    driver.switch_to.window(parent)

def extra_activities():
    driver.switch_to.window(parent)
    
    try:
        driver.find_element(By.XPATH,"/html[@class='ltr rewards-dashboard rewards js picture eventlistener k-webkit k-webkit107']/body/div[@id='page-wrapper']/div[@id='main-content-landing']/main[@id='rewards-dashboard']/div[@id='app-host']/ui-view[@class='ng-scope']/mee-rewards-dashboard[@class='ng-scope ng-isolate-scope']/main[@id='rewardsAngular']/div[@class='rewardsContent']/mee-rewards-more-activities-card[@class='ng-scope ng-isolate-scope']/mee-card-group[@id='more-activities']/div[@class='m-card-group']/mee-card[@class='ng-scope ng-isolate-scope c-card f-double']/div[@class='c-card-content']/card-content[@class='ng-scope']/mee-rewards-more-activities-card-item[@class='ng-isolate-scope']/div[@class='text-align-center rewards-card-container']/a[@class='ds-card-sec']/div[@id='ma-card-link']/span[@class='pointLink ng-binding']").click()

        
        chld = driver.window_handles[1]
        driver.switch_to.window(chld)
        time.sleep(3)
        driver.close()
        driver.switch_to.window(parent)
    except:
        time.sleep(.5)

    try:
        driver.find_element(By.XPATH, "/html[@class='ltr rewards-dashboard rewards js picture eventlistener k-webkit k-webkit107']/body/div[@id='page-wrapper']/div[@id='main-content-landing']/main[@id='rewards-dashboard']/div[@id='app-host']/ui-view[@class='ng-scope']/mee-rewards-dashboard[@class='ng-scope ng-isolate-scope']/main[@id='rewardsAngular']/div[@class='rewardsContent']/mee-rewards-more-activities-card[@class='ng-scope ng-isolate-scope']/mee-card-group[@id='more-activities']/div[@class='m-card-group']/mee-card[@class='ng-scope ng-isolate-scope c-card f-single'][1]/div[@class='c-card-content']/card-content[@class='ng-scope']/mee-rewards-more-activities-card-item[@class='ng-isolate-scope']/div[@class='text-align-center rewards-card-container']/a[@class='ds-card-sec']/div[@id='ma-card-link']/span[@class='pointLink ng-binding']").click()

        chld = driver.window_handles[1]
        driver.switch_to.window(chld)
        time.sleep(3)
        driver.close()
        driver.switch_to.window(parent)
    except:
        time.sleep(.5)

    try:
        driver.find_element(By.XPATH, "/html[@class='ltr rewards-dashboard rewards js picture eventlistener k-webkit k-webkit107']/body/div[@id='page-wrapper']/div[@id='main-content-landing']/main[@id='rewards-dashboard']/div[@id='app-host']/ui-view[@class='ng-scope']/mee-rewards-dashboard[@class='ng-scope ng-isolate-scope']/main[@id='rewardsAngular']/div[@class='rewardsContent']/mee-rewards-more-activities-card[@class='ng-scope ng-isolate-scope']/mee-card-group[@id='more-activities']/div[@class='m-card-group']/mee-card[@class='ng-scope ng-isolate-scope c-card f-single'][2]/div[@class='c-card-content']/card-content[@class='ng-scope']/mee-rewards-more-activities-card-item[@class='ng-isolate-scope']/div[@class='text-align-center rewards-card-container']/a[@class='ds-card-sec']/div[@id='ma-card-link']/span[@class='pointLink ng-binding']").click()

        chld = driver.window_handles[1]
        driver.switch_to.window(chld)
        time.sleep(3)
        driver.close()
        driver.switch_to.window(parent)
    except:
        time.sleep(.5)
    driver.switch_to.window(parent)
    


def main():
    
    driver.get("https://rewards.microsoft.com/")
    driver.find_element(By.ID,"raf-signin-link-id").click()
    time.sleep(1)
    username = driver.find_element("name", "loginfmt")
    username.send_keys(config.login_reward)
    driver.find_element(By.ID,"idSIButton9").click()
    time.sleep(1)
    password = driver.find_element("name", "passwd")
    password.send_keys(config.password_reward)
    time.sleep(1)
    driver.find_element(By.ID,"idSIButton9").click()
    time.sleep(1)
    driver.find_element(By.ID,"idSIButton9").click()
    time.sleep(4)
    a = checker()
    if a == True:
        driver.find_element(By.XPATH, "/html[@class='ltr rewards-dashboard rewards js picture eventlistener k-webkit k-webkit107']/body/div[@id='page-wrapper']/div[@id='site-header']/header/div[@id='rewards-header']/div[@class='l_header_container']/div[@class='l_header_right']/a[@class='redirect_link additional_info']").click()
        driver.find_element(By.XPATH,"//a[@href='/Signout']").click()

    time.sleep(8)

    driver.find_element(By.ID,"raf-signin-link-id").click()
    time.sleep(1)
    username = driver.find_element("name", "loginfmt")
    username.send_keys(config.login_gmail)
    driver.find_element(By.ID,"idSIButton9").click()
    time.sleep(1)
    password = driver.find_element("name", "passwd")
    password.send_keys(config.password_gmail)
    time.sleep(1)
    driver.find_element(By.ID,"idSIButton9").click()
    time.sleep(1)
    driver.find_element(By.ID,"idSIButton9").click()
    a = checker()
    if a == True:
        driver.find_element(By.XPATH, "/html[@class='ltr rewards-dashboard rewards js picture eventlistener k-webkit k-webkit107']/body/div[@id='page-wrapper']/div[@id='site-header']/header/div[@id='rewards-header']/div[@class='l_header_container']/div[@class='l_header_right']/a[@class='redirect_link additional_info']").click()
        driver.find_element(By.XPATH,"//a[@href='/Signout']").click()

    time.sleep(8)

    driver.find_element(By.ID,"raf-signin-link-id").click()
    time.sleep(1)
    username = driver.find_element("name", "loginfmt")
    username.send_keys(config.login_outlook)
    driver.find_element(By.ID,"idSIButton9").click()
    time.sleep(1)
    password = driver.find_element("name", "passwd")
    password.send_keys(config.password_outlook)
    time.sleep(1)
    driver.find_element(By.ID,"idSIButton9").click()
    time.sleep(1)
    driver.find_element(By.ID,"idSIButton9").click()
    a = checker()
    if a == True:
        driver.find_element(By.XPATH, "/html[@class='ltr rewards-dashboard rewards js picture eventlistener k-webkit k-webkit107']/body/div[@id='page-wrapper']/div[@id='site-header']/header/div[@id='rewards-header']/div[@class='l_header_container']/div[@class='l_header_right']/a[@class='redirect_link additional_info']").click()
        driver.find_element(By.XPATH,"//a[@href='/Signout']").click()
    driver.quit()


if __name__ == '__main__':

    main()