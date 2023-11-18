from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_window = browser.window_handles[0]

    button = browser.find_element(By.CLASS_NAME, "trollface.btn-primary")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, 'input_value')
    x = float(x_element.text)
    y = math.log(abs(12 * math.sin(x)))
    print(x)
    print(y)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(str(y))
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
