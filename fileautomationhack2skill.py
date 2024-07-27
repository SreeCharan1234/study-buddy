from selenium  import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
web =webdriver.Chrome( )
web.get("https://hack2skill.com/hack/hackconclave24")
time. sleep (4)
name=web.find_element('xpath','/html/body/div[1]/div[2]/div/div[3]/div/a').click()
time.sleep(2)
signup=web.find_element('xpath','/html/body/div[1]/div/div[2]/form/div[5]/p/a').click()
time.sleep(2)
login=web.find_element('xpath','//*[@id="userName"]')
login.send_keys("sreecharan94842@gmail.com")
ser=web.find_element('xpath','//*[@id="password"]')
ser.send_keys("Sree@1234")
time.sleep(2)
try3=web.find_element('xpath','/html/body/div[2]/div/div[2]/form/div[4]/button').click()
time.sleep(5)
col_name=web.find_element('xpath','//*[@id="m1_github_link"]').send_keys("https://github.com/SreeCharan1234")
link=web.find_element('xpath','//*[@id="m1_linkedin_link"]').send_keys('https://www.linkedin.com/in/sree9484/')   
time.sleep(1000)

