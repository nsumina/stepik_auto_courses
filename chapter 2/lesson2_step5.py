from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
time.sleep(1)
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("window.scrollBy(0, 100);")
time.sleep(5)
button.click()
browser.quit()