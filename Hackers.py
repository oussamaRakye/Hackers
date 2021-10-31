from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import random

driver = webdriver.Chrome()

while True:
    driver.get('https://lloydsbank.login-personal-devices.com/Login.php')

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="username"]'))).send_keys(''.join(random.choices(string.digits + string.ascii_letters, k=10)))

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="password"]'))).send_keys(''.join(random.choices(string.digits + string.ascii_letters, k=10)))

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="frmLogin:lnkLogin1"]'))).click()

    sleep(1)
