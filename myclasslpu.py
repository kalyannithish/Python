from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
options = webdriver.ChromeOptions() 
options.add_argument("start-minimized")
browser = webdriver.Chrome(options=options, executable_path=r'C:\\Users\\kalya\\Documents\\chromedriver')
browser.get('https://myclass.lpu.in/')
browser.implicitly_wait(3)
inputElement = browser.find_element_by_name("i")
inputElement.send_keys("11911809")
inputElement = browser.find_element_by_name("p")
inputElement.send_keys("Kalyan@0033")
loginButton= browser.find_element_by_xpath("/html/body/div[2]/div/form/div[7]/button").click()
browser.implicitly_wait(3)
#link.send_keys(Keys.ENTER)
View_meeting = browser.find_element_by_xpath("/html/body/div[9]/div/div[1]/div/div/div[1]/div/div[2]/a").click()
#Enterclass = browser.find_element_by_id("calendar").click()
Enterclass = browser.find_element_by_css_selector("#calendar > div.fc-view-container > div > table > tbody > tr > td > div > div > div.fc-content-skeleton > table > tbody > tr > td:nth-child(2) > div > div:nth-child(2) > a:nth-child(1)").click()
datetime.datetime.now()
