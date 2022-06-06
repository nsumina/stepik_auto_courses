from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)
#
input_firstname = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
input_firstname.send_keys("Natalee")

input_lastname = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
input_lastname.send_keys("Sumina")

input_email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
input_email.send_keys("email@email.com")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'empty_file.txt')

button_file = browser.find_element(By.ID, 'file')
button_file.send_keys(file_path)

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(5)
browser.quit()