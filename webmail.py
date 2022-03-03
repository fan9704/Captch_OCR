
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import urllib
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
    
    #Download Image
    local_path = 'img'
    elem=browser.find_elements_by_css_selector("img#CaptQuiz")[0]
    print(elem)
    img_url = elem.get_attribute('src')
    filename = 'images.gif'
    print(filename)
    urllib.request.urlretrieve(img_url, os.path.join(local_path , filename))
    
    from muggle_ocr.muggle_ocr import SDK,ModelType
    text=""
    sdk = SDK(model_type=ModelType.Captcha)
    with open("./img/images.gif", "rb") as f:
        b = f.read()
        text = sdk.predict(image_bytes=b)
        print(text)

    elem = browser.find_element_by_css_selector("input.captchaInput")
    elem.send_keys(text)#key in username
    elem.send_keys(Keys.RETURN) #Send info


if __name__ == "__main__":
    login()
