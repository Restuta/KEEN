##test scenario
# Given I filled in account fields with first and last name
# When I click the "Save" button
# Then I should see message "Your member information has been successfully saved."

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

test_user_email = "test02@example.com" #Change it before test +1!!!
test_user_password = "123456"

## open browser and login page
driver = webdriver.Chrome()
driver.get("http://mb.test.ingenio.com/index.html#/login")

wait = WebDriverWait(driver, 10)
user_name_field = wait.until(EC.element_to_be_clickable((By.ID, "userName")))
user_name_field.send_keys(test_user_email)

password_field = driver.find_element_by_id("password")
password_field.send_keys(test_user_password)

login_button = driver.find_element_by_id("btnLogin")
login_button.click()



driver.quit()

