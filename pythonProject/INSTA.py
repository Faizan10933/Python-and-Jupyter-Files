from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r'C:\Users\FAIZAN\Downloads/chromedriver.exe')
driver.get('https://www.instagram.com/')
sleep(2)

driver.maxmize_window()
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(2)

driver.find_element_by_name("username").send_keys('faizan10933')
sleep(2)

driver.find_element_by_name("password").send_keys('Faizan7479')
sleep(2)

driver.find_element_by_name("password").send_keys(u'\ue007')
sleep(2)
