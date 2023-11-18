from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, 'treasure')
    x = float(x_element.get_attribute("valuex"))
    y = math.log(abs(12*math.sin(x)))
    print(x)
    print(y)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(str(y))
    RobotCheckBox = browser.find_element(By.ID, "robotCheckbox")
    RobotCheckBox.click()
    RobotRules = browser.find_element(By.ID, "robotsRule")
    RobotRules.click()
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()


# не забываем оставить пустую строку в конце файла