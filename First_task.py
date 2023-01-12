from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.saucedemo.com/")
driver.find_element(By.CLASS_NAME, "input_error").send_keys("standard_user")
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

act_title = driver.title
exp_title = "Swag Labs"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

time.sleep(5)
driver.close()
driver.quit()
print("Test Completed")
