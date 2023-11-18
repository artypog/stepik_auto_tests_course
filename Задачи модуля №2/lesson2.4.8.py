from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    #EC = browser.find_element(By.ID, "price")
    price = '1'

    while price != '$100':
        price = WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.ID, 'price'))).text
        print(price)

    button1 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button1.click()


    x_element = browser.find_element(By.ID, 'input_value')
    x = float(x_element.text)
    y = math.log(abs(12*math.sin(x)))
    print(x)
    print(y)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(str(y))
    button2 = browser.find_element(By.ID, "solve")
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
