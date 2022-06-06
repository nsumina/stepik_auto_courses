from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  browser = webdriver.Chrome()
  link = "http://suninjuly.github.io/redirect_accept.html"
  browser.get(link)
  time.sleep(1)

  button = browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary")
  button.click()
  time.sleep(1)

  new_window = browser.window_handles[1]
  browser.switch_to.window(new_window)
  time.sleep(1)

  x_element = browser.find_element(By.ID, "input_value")
  x = x_element.text
  y = calc(x)

  input = browser.find_element(By.ID, 'answer')
  input.send_keys(y)

  button_submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
  button_submit.click()
  time.sleep(3)


finally:
  browser.quit()