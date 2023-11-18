from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1_element = browser.find_element(By.ID, 'num1')
    num1 = int(num1_element.text)
    num2_element = browser.find_element(By.ID, 'num2')
    num2 = int(num2_element.text)
    print(num1, num2)
    num_element = num1 + num2
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(num_element))  # ищем элемент с суммой чисел

    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()


# не забываем оставить пустую строку в конце файла