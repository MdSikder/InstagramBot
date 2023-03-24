import time
from telnetlib import EC

import self as self
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import pyautogui
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# Locators
username = "//input[@name='username']"
password = "//input[@name='password']"
submit = "//button[@type='submit']"
Create_button = "//html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[7]/div[1]/div[1]/a[1]/div[1]/div[2]/div[1]/div[1]"
upload_button = "//button[text()='Select from computer']"
next_button = "//div[contains(text(),'Next')]"
share_button = "//div[contains(text(),'Share')]"
notification = "//button[contains(text(),'Not Now')]"
write = "//div[@aria-label='Write a caption...']"

file_path = "C:\\Users\\KloverCloud\\PycharmProjects\\project\\WebBots\\instagram\\upload\\filpng.png"

###############################   Start   ##################################

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.instagram.com/")
time.sleep(5)

try:
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
except:
    print("no cookies Alert")

try:
    driver.switch_to.alert.accept()
    print("Alert accepted")
except:
    print("no Alert found")

driver.find_element(By.XPATH, username).send_keys("usemany5@gmail.com")
time.sleep(2)

driver.find_element(By.XPATH, password).send_keys("Qwer1234@@!!")
time.sleep(2)

driver.find_element(By.XPATH, submit).click()
time.sleep(20)

try:
    driver.switch_to.alert.dismiss()
    print("Alert accepted")
except:
    print("no Alert found")

pyautogui.press('tab')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

# create = WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, Create_button)))
try:
    # create.click()
    driver.find_element(By.XPATH, Create_button).click()
    time.sleep(5)

except NoSuchElementException as e:
    print("NoSuchElementException error :\n", e, "\n")
except TimeoutException as e:
    print("TimeoutException error", e)
except InvalidSessionIdException as e:
    print("InvalidSessionIdException", e)

driver.find_element(By.XPATH, "//button[text()='Select from computer']").click()
time.sleep(5)

pyautogui.typewrite(file_path)
time.sleep(2)

pyautogui.press('enter')
time.sleep(3)

driver.find_element(By.XPATH, next_button).click()
time.sleep(2)

driver.find_element(By.XPATH, next_button).click()
time.sleep(3)

driver.find_element(By.XPATH, write).send_keys('hello dear window')
time.sleep(5)

driver.find_element(By.XPATH, share_button).click()
time.sleep(30)
