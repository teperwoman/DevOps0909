#A
from selenium import webdriver
my_driver = webdriver.Chrome(executable_path="/Users/bennyronen/Desktop/chromedriver")
my_driver.get("http://www.walla.co.il")

#B
from selenium import webdriver
my_fire_driver = webdriver.Firefox(executable_path="/Users/bennyronen/Desktop/geckodriver")
my_fire_driver.get("http://www.ynet.co.il")