from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
print("sample test case started")
driver_service = Service(executable_path="c:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
#maximize the window size
driver.maximize_window()
#navigate to the url
driver.get("https://www.google.com/")
#identify the Google search text box and enter the value
driver.find_element('name', 'q').send_keys("javatpoint")
time.sleep(3)
#click on the Google search button
driver.find_element('name', 'btnK').send_keys(Keys.ENTER)
time.sleep(3)
#close the browser
driver.close()
print("sample test case successfully completed")