from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time


def odd_one_out(lst):
    unique_set = set(lst)
    return next(item for item in unique_set if lst.count(item) == 1)


def start_spam(color_list):
    try:
        color_block = [color_rgb.value_of_css_property('background-color') for color_rgb in color_list]
    except StaleElementReferenceException:
        return 0
    else:
        odd = odd_one_out(color_block)
        for element in color_div:
            if element.value_of_css_property('background-color') == odd:
                element.click()
                break


tracking = 0
goal_wanted = input("Enter the score you want to achieve in integer, otherwise type something else or press enter: ")
try:
    goal_wanted = int(goal_wanted)
except ValueError:
    goal_wanted = None
driver_option = webdriver.ChromeOptions()
driver_option.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=driver_option)

driver.get('https://www.arealme.com/colors/en/')

while True:
    try:
        color_div = driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[2]').find_element(By.TAG_NAME,
                                                                                                  'div').find_elements(
            By.TAG_NAME, "span")
    except NoSuchElementException:
        time.sleep(0.5)
        pass
    else:
        spam_func_output = start_spam(color_div)
        if spam_func_output == 0 and goal_wanted is None:
            print("Done")
            break
        elif spam_func_output == 0 and goal_wanted is not None:
            print("Goal couldn't be reached")
            break
        tracking += 1
        if (goal_wanted is not None) and (goal_wanted == tracking):
            print(f"Goal reached: {goal_wanted}")
            break
