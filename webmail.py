
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
url ="https://webmail.yuntech.edu.tw/cgi-bin/login"
browser=webdriver.Chrome()#open browser
def login():
    browser.get(url)
    print("[System]",time.strftime(" %I:%M:%S %p",time.localtime()), "Webmail Linked ")
    # username = os.getenv('username')
    # password = os.getenv('password')
    username = "B10923057"
    password = "cxz123499"
    elem = browser.find_element_by_css_selector("input[name='USERID']")
    elem.send_keys(username)#key in username
    elem = browser.find_element_by_css_selector("input[name='PASSWD']")
    elem.send_keys(password)#key in username
    # elem.send_keys(Keys.RETURN)

if __name__ == "__main__":
    login()
