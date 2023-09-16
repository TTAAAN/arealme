from selenium.webdriver.common.by import By
from selenium import webdriver
import time


def odd_one_out(lst):
    unique_set = set(lst)
    for item in unique_set:
        if lst.count(item) == 1:
            return item


driver = webdriver.Chrome()

driver.get('https://www.arealme.com/colors/en/')
start_button = driver.find_element(By.XPATH, '//*[@id="start"]')

# Wait for the start button to load
time.sleep(2)
start_button.click()
start_time = int(time.time())
end_time = int(start_time + 59)

# Start clicking
while True:
    color_div = driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[2]').find_element(By.TAG_NAME, 'div').find_elements(By.TAG_NAME, "span")
    color_block = [color_rgb.value_of_css_property('background-color') for color_rgb in color_div]
    odd = odd_one_out(color_block)
    for element in color_div:
        if element.value_of_css_property('background-color') == odd:
            element.click()
            break
    if int(time.time()) == end_time:
        break
