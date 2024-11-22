from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    
    new_tab = browser.window_handles[1]  # Получаем хэндл новой вкладки
    browser.switch_to.window(new_tab)
    
    x_value = browser.find_element(By.ID, "input_value").text
    result = calc(x_value)
    
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(result)
    
    submit_button = browser.find_element(By.TAG_NAME, "button")
    submit_button.click()
    
    alert = browser.switch_to.alert
    print(alert.text.split()[-1])  # Выводим число-ответ в консоль
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()
