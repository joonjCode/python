from conf import INSTA_PASSWORD, INSTA_USERNAME
from urllib.parse import urlparse
from selenium import webdriver
import time
import requests
import os
from PIL import Image

browser = webdriver.Chrome()

url = 'https://www.instagram.com'
browser.get(url)


# Login Automation
time.sleep(2)
username_el = browser.find_element_by_name("username")
username_el.send_keys(INSTA_USERNAME)
passwor_el = browser.find_element_by_name("password")
passwor_el.send_keys(INSTA_PASSWORD)

time.sleep(1.5)
submit_btn_el = browser.find_element_by_css_selector("button[type='submit']")
submit_btn_el.click()

body_el = browser.find_element_by_css_selector("body")
html_text = body_el.get_attribute("innerHTML")


# xpath
# my_button_xpath = '//button'
# browser.find_elements_by_xpath(my_button_path)


def follow_account(browser):
    my_follow_button_xpath = '//button[contains(text,"Follow")][not (contains(text(), "Following"))]'
    follow_btn_el = browser.find_elements_by_xpath(my_follow_button_xpath)

    for btn in follow_btn_el:
        time.sleep(2) # Self- throttle
        try:
            btn.click()
        except:
            pass


# new_user_url = 'https://www.instagram.com/ted/'
# browser.get(new_user_url)

# Scrape all posts
time.sleep(2)
the_rock_url = 'https://www.instagram.com/therock/'
browser.get(the_rock_url)

pst_url_pattern = 'https://www.instagram.com/p/<post-slug-id>'
post_xpath_str = '//a[contains(@href, "/p/")]'

post_links = browser.find_elements_by_xpath(post_xpath_str)
post_link_el = None
if len(post_links)>0:
    post_link_el = post_links[0]
if post_link_el != None:
    post_href = post_link_el.get_attribute('href')
    browser.get(post_href)


video_els = browser.find_elements_by_xpath('//video')
image_els = browser.find_elements_by_xpath('//img')
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, 'data')
os.makedirs(data_dir, exist_ok = True)

# PIL to verify the size of the images. 

def scrape_and_save(elements):
    for el in elements:
        url = el.get_attribute('src')
        base_url = urlparse(url).path
        filename = os.path.basename(base_url)
        filepath = os.path.join(data_dir,filename)
        if os.path.exists(filepath):
            continue
        with requests.get(url, stream=True) as r:
            try:
                r.raise_for_status()
            except:
                continue
            with open(filepath, 'wb') as f:
                # For fastser download by reducing size
                for chunk in r.iter_content(chunk_size=8192): 
                    if chunk:
                        f.write(chunk)
 

# scrape_and_save(video_els)
# scrape_and_save(image_els)

'''
LONG TERM GOAL
Use machine learning to classify the post's images or video
and then comment in a relevant fashion
'''

def automate_comment(content= 'That is cool!'):
    comment_xpath_str = '//textarea[contains(@placeholder, "Add a comment")]'
    comment_el = browser.find_element_by_xpath(comment_xpath_str)
    comment_el.send_keys("Awesome!!!")

    submit_btns_xpath = 'button[type ="submit"]'
    submit_btns_els = browser.find_element_css_selector(submit_btns_xpath)
    for btn in submit_btns_els:
        try:
            btn.click()
        except:
            pass
 