from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import math
import time

def calc(x):
    """Вычисляем значение математической функции"""
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/alert_accept.html")
    
    browser.find_element(By.TAG_NAME, "button").click()
    
    alert = browser.switch_to.alert
    alert.accept()
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    result = calc(x)
    
    browser.find_element(By.ID, "answer").send_keys(result)
    
    browser.find_element(By.TAG_NAME, "button").click()
    
    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

finally:
    time.sleep(15)
    browser.quit()
