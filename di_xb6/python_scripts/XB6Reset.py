#The script resets XB6 system
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

gateway_host = "http://192.168.0.1"

def set_param_reset(gh):
    gateway_host = gh

def run_reset():
    #driver = webdriver.Firefox(executable_path=r'C:/firefox/geckodriver.exe')
    driver = webdriver.Chrome(executable_path=r'C:/chrome/chromedriver.exe')
	#driver.implicitly_wait(30)
    base_url = gateway_host
    driver.get(base_url + "/")
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("admin") #GUI login
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("rogers123") #GUI password
    driver.find_element_by_css_selector("input.btn").click()
    driver.find_element_by_link_text("Troubleshooting").click()
    driver.find_element_by_link_text("Reset/Restore Gateway").click()
    driver.find_element_by_id("btn1").click()
    driver.find_element_by_id("popup_ok").click()
    time.sleep(3)
    
if __name__ == "__main__":
    #enable this to change gateway
    #set_param_reset("gateway ip here")
    
    run_reset()