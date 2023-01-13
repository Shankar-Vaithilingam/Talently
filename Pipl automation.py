import command
import subprocess
import os
import signal
import selenium as selenium
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
import requests
from bs4 import BeautifulSoup

# 18-20 - I have already opened a chrome browser in debugging mode and I'm running it in the cmd line to start it as a server 
pro = subprocess.Popen(
    "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9986 --user-data-dir=/Users/shankar/Documents/pipl_cookies/",
    stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)

path = r"/Users/shankar/Desktop/ChromeDriver/chromedriver" #path of my downloaded chromedriver

chrome_options = Options() # Initializing chrome options
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9986") #invoke "add experimental options" function and pass the debugger address as the port number in which the chrome browser is opened
chrome_driver = path
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options) 

try:
    driver.get("https://pipl.com/search/") # trying to pen the search module
    login_text = driver.find_element("xpath", ".//span[contains(@class,'o-loginuser__title desktop')]").text #find a logged in user icon
except:
    # login code
    driver.get("https://pipl.com/accounts/login/")
    time.sleep(3)
    username = driver.find_element("xpath", "//input[@name='email']")
    password = driver.find_element("xpath", "//input[@name='password']")
    username.send_keys('heather@talentlyrecruiting.com')
    password.send_keys('Talently123!!!')
    driver.find_element("xpath", "//button[@type='submit']").click()
    time.sleep(3)

driver.get("https://pipl.com/search/")
time.sleep(3)
parse_profiles = ["https://www.linkedin.com/in/roymonroy/", "https://www.linkedin.com/in/shankar-vaithilingam/", "https://www.linkedin.com/in/justinpgibbons", "justinpgibbons@twitter"]
for profile in parse_profiles:
    print(profile)
    query_input = driver.find_element("xpath", "//input[@name='pipl-search-box']")
    time.sleep(5)
    query_input.send_keys(profile)
    time.sleep(2)
    driver.find_element("xpath", "//button[@class='search-button ']").click()
    time.sleep(5)
    try:
        check_result = driver.find_element("xpath", "//div[test-id='no-results-found-title']")
        driver.find_element("xpath", ".//span[contains(@test-id,'clear-search-bar-x')]").click()
        continue
    except:
        phone_elements = driver.find_elements("xpath", ".//span[contains(@test-id,'phone-field-value-')]") # get all elements against the phone class
        for count, element in enumerate(phone_elements, start=0):
            num = element.text # Phone number
            try:
                text_concat = ".//span[contains(@test-id,'phone-field-value-"+str(count)+"')]/following-sibling::span"
                num_type = driver.find_element("xpath", text_concat).text
                print(num, num_type)
            except:
                print(num)
        email_elements = driver.find_elements("xpath", ".//span[contains(@test-id,'email-field-value-')]")
        for count1, element in enumerate(email_elements, start=0):
            emailadd = element.text
            try:
                text_concat1 = ".//span[contains(@test-id,'email-field-value-" + str(count1) + "')]/../following-sibling::span"
                email_type = driver.find_element("xpath", text_concat1).text
                print(emailadd, email_type)
            except:
                print(emailadd)
        try:
            address_place = driver.find_element("xpath", ".//span[contains(@test-id,'address-field-value-0')]").text
            print(address_place)
        except:
            pass
        driver.find_element("xpath", ".//span[contains(@test-id,'clear-search-bar-x')]").click()
