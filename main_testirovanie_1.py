from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
#при написании ссылки на драйвер не забыть изменить слэш в обратную сторону!!!
s = Service('C:/Downloads/chromedriver-win64')
driver = webdriver.Chrome(service=s)
driver.get("https://idemo.bspb.ru/")
driver.set_window_size(1366, 768)
driver.find_element(By.NAME, "username").clear()#удаляем строчку с логином
driver.find_element(By.NAME, "username").send_keys("demo")#вводим новый логин
driver.find_element(By.NAME, "password").clear()
driver.find_element(By.NAME, "password").send_keys("demo")
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.ID, "otp-code").click()#двухфакторная авторизация, очищаем строку
driver.find_element(By.ID, "otp-code").send_keys("0000")#вводим код
driver.find_element(By.ID, "login-otp-button").click()
time.sleep(3)

