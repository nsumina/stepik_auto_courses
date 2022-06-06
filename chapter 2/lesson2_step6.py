from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value.nowrap")
x = x_element.text
y = calc(x)

browser.execute_script("window.scrollBy(0, 100);")

input1 = browser.find_element(By.CSS_SELECTOR, "#answer.form-control")

input1.send_keys(y)
browser.execute_script("window.scrollBy(0, 100);")

option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
option1.click()

option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
option2.click()

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
#
#
time.sleep(10)
# button = browser.find_element(By.TAG_NAME, "button")
# browser.execute_script("window.scrollBy(0, 100);")
# time.sleep(5)
# button.click()
browser.quit()