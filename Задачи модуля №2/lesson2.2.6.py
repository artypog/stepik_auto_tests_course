from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, 'input_value')
    x = float(x_element.text)
    y = math.log(abs(12*math.sin(x)))
    print(x)
    print(y)
    browser.execute_script("window.scrollBy(0, 100);")
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(str(y))
    RobotCheckBox = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    RobotCheckBox.click()
    RobotRules = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    RobotRules.click()
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
