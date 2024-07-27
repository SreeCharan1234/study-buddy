from selenium  import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

web = webdriver . Chrome ( )
web.get("https://unstop.com/competitions/1082682/register")
time. sleep (4)
login=web.find_element('xpath','//*[@id="email"]')
login.send_keys("sreecharan94842@gmail.com")
ser=web.find_element('xpath','//*[@id="pwd"]')
ser.send_keys("Sree@1234")
time.sleep(19)
print("Dfdsf")
name=web.find_element('xpath','//*[@id="s_menu"]/app-root/div/main/app-registration-stepper/div/div[2]/div/div/app-player-registration-form/div[1]/div/div/div[2]/div[3]/div[8]/div').click()

time.sleep(10)

