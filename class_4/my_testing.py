from selenium import webdriver
from time import sleep
# my_driver = webdriver.Chrome(executable_path="c:/Users/avielb/Downloads/chromedriver.exe")
my_driver = webdriver.Chrome(executable_path="/Users/bennyronen/Desktop/chromedriver")
my_driver.get("file:///Users/bennyronen/Desktop/tip_calc/index.html")
my_driver.find_element_by_id("billamt").send_keys("100")
my_driver.find_element_by_xpath("//*[@id=\"serviceQual\"]/option[3]").click()
my_driver.find_element_by_id("peopleamt").send_keys("5")
my_driver.find_element_by_id("musicamt").send_keys("5")
my_driver.find_element_by_id("calculate").click()
expected = "9.00"
actual = my_driver.find_element_by_id("tip").text
if expected == actual:
    print("all good")

