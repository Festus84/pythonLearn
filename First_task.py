from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

from python_selenium import checkboxes

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()

# Launching the URL
driver.get("https://www.saucedemo.com/")

# Login into the application
driver.find_element(By.CLASS_NAME, "input_error").send_keys("standard_user")
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Adding items to cart
driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
driver.find_element(By. XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]').click()
driver.find_element(By.NAME, "add-to-cart-sauce-labs-bike-light").click()
driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()

time.sleep(5)

# Remove item from cart
driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]').click()
driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-onesie"]').click()
driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]').click()
time.sleep(3)

# continuous shopping
driver.find_element(By.XPATH, '//*[@id="continue-shopping"]').click()
time.sleep(2)

# Adding 2 more items'
# driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
time.sleep(3)

# Checkout
driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("Festus")
driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("Adewale")
driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys(110001)
driver.find_element(By.XPATH, '//*[@id="continue"]').click()
driver.find_element(By.XPATH, '//*[@id="finish"]').click()
time.sleep(5)


# Logout
driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]')

# Verifying the title page
act_title = driver.title
exp_title = "Swag Labs"
if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

time.sleep(5)
# Closing the browser
driver.quit()
print("Test Completed")
