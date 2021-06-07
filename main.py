from selenium import webdriver
from time import sleep

username = "test"
password = "test"
url = "http://www.stealmylogin.com/demo.html"

driver = webdriver.Chrome("C:\chromedriver/chromedriver.exe")
driver.get(url)
sleep(3)
driver.find_element_by_name("username").send_keys(username)
sleep(1)
driver.find_element_by_name("password").send_keys(password)
sleep(1)
driver.find_element_by_css_selector("input[type=\"submit\" i]").click()
sleep(1)

print("Logged!")