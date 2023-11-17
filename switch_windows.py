from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = 'http://suninjuly.github.io/redirect_accept.html'

def calc(a):
    return str(math.log(abs(12 * math.sin(int(a)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.TAG_NAME, 'button').click()
    browser.switch_to.window(browser.window_handles[1])
    n = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(n))
    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
finally:
    time.sleep(10)
    browser.quit()