from selenium import webdriver
import time

browser = webdriver.Chrome()

url = 'https://google.com'

browser.get(url)

# name = 'q'
search_el = browser.find_element_by_name("q")
# print(search_el)

search_el.send_keys('selenium python')

time.sleep(2)
submit_btn_el = browser.find_element_by_css_selector("input[type='submit']")
# print(submit_btn_el.get_attribute('name')) 
submit_btn_el.click()