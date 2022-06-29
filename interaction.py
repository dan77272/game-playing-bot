from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

path = "C:\Development\chromedriver.exe"
s = Service(path)

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("http://orteil.dashnet.org/experiments/cookie/")



timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes

while time.time() < timeout:
    button = driver.find_element(By.ID, "cookie")
    money = driver.find_element(By.ID, "money")
    cursor = driver.find_element(By.ID, "buyCursor")
    grandma = driver.find_element(By.ID, "buyGrandma")
    factory = driver.find_element(By.ID, "buyFactory")
    mine = driver.find_element(By.ID, "buyMine")
    shipment = driver.find_element(By.ID, "buyShipment")
    alchemy = driver.find_element(By.ID, "buyAlchemy lab")
    portal = driver.find_element(By.ID, "buyPortal")
    time_machine = driver.find_element(By.ID, "buyTime machine")
    button.click()
    if time.time() > timeout:
        if int(money.text) > 123456789:
            time_machine.click()
            timeout = time.time() + 5
        elif int(money.text) > 1000000:
            portal.click()
            timeout = time.time() + 5
        elif int(money.text) > 50000:
            alchemy.click()
            timeout = time.time() + 5
        elif int(money.text) > 7000:
            shipment.click()
            timeout = time.time() + 5
        elif int(money.text) > 2000:
            mine.click()
            timeout = time.time() + 5
        elif int(money.text) > 500:
            factory.click()
            timeout = time.time() + 5
        elif int(money.text) > 100:
            grandma.click()
            timeout = time.time() + 5
        elif int(money.text) > 15:
            cursor.click()
            timeout = time.time() + 5
        else:
            timeout = time.time() + 5
