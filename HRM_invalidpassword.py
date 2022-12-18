from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#Test case : 2 (Invalid Credentials)

class username_1():
    def name_password(self):
        driver=webdriver.Chrome()
        url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(url)
        time.sleep(5)
        driver.maximize_window()
        time.sleep(3)
#Testcase-2

#xpath for username
        username_xpath='//input[@name="username"]'
        username=driver.find_element(By.XPATH,username_xpath).send_keys("Admin")
        time.sleep(4)

#xpath for password
        password_xpath='//input[@name="password"]'
        password=driver.find_element(By.XPATH,password_xpath).send_keys("admin100")
        time.sleep(4)

#xpath to click login button
        login_xpath = '//button[@type="submit"]'
        submit = driver.find_element(By.XPATH, login_xpath).click()
        time.sleep(10)

#xpath for password error
        error_xpath="//div[@class='oxd-alert oxd-alert--error']"
        error=driver.find_element(By.XPATH,error_xpath)
        print(error.text)

#possible to use
        #if password=="admin123":
            #print("The password is correct")
        #else:
            #print("The password is incorrect")
            #time.sleep(4)

a=username_1()
a.name_password()
