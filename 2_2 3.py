import os
from selenium import webdriver
from selenium.webdriver.common.by import By

file_name = "test.txt"
file_path = os.path.join(os.getcwd(), file_name)
with open(file_path, "w") as file:
    file.write("This is a test file.")

link = "http://suninjuly.github.io/file_input.html"
driver = webdriver.Chrome()
try:
    driver.get(link)

    driver.find_element(By.NAME, "firstname").send_keys("John")
    driver.find_element(By.NAME, "lastname").send_keys("Doe")
    driver.find_element(By.NAME, "email").send_keys("john.doe@example.com")

    file_input = driver.find_element(By.ID, "file")
    file_input.send_keys(file_path)

    submit_button = driver.find_element(By.TAG_NAME, "button")
    submit_button.click()
    alert = driver.switch_to.alert
    print(alert.text.split()[-1])  # Вывод числа из окна alert
    alert.accept()

finally:
    if os.path.exists(file_path):
        os.remove(file_path)
    driver.quit()
