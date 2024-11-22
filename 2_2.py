import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
link = "https://SunInJuly.github.io/execute_script.html"
driver = webdriver.Chrome()
try:
    driver.get(link)
    x_element = driver.find_element(By.ID, "input_value")
    x = x_element.text
    result = calc(x)
    
    answer_field = driver.find_element(By.ID, "answer")
    driver.execute_script("arguments[0].scrollIntoView(true);", answer_field)
    
    answer_field.send_keys(result)
    
    checkbox = driver.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    
    radiobutton = driver.find_element(By.ID, "robotsRule")
    radiobutton.click()
    
    submit_button = driver.find_element(By.TAG_NAME, "button")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()
    alert = WebDriverWait(driver, 15).until(EC.alert_is_present())
    print(alert.text.split()[-1])  # Получение числа из окна алерта

finally:
    driver.quit()
