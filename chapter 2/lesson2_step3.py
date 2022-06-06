from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1_element = browser.find_element(By.CSS_SELECTOR, "span#num1")
    num1 = num1_element.text

    num2_element = browser.find_element(By.CSS_SELECTOR, "span#num2")
    num2 = num2_element.text

    sum = str(int(num1) + int(num2))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    #
    # input1 = browser.find_element(By.ID, "answer")
    # input1.send_keys(y)
    # #
    # option1 = browser.find_element(By.ID, "robotCheckbox")
    # option1.click()
    # #
    # option2 = browser.find_element(By.ID, "robotsRule")
    # option2.click()
    # #
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    print("first number is" , num1)
    print("first number is" , num2)
    print(sum)
    browser.quit()

