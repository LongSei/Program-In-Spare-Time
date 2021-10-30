from selenium import webdriver
import time

test_driver = webdriver.Chrome()
test_driver.get("https://www.facebook.com/messages")

email_input = test_driver.find_element_by_id("email")
password_input = test_driver.find_element_by_id("pass")
login_button = test_driver.find_element_by_id("loginbutton")

email = ""
password = ""


email_input.send_keys(email)
password_input.send_keys(password)
login_button.click()

time.sleep(5)
name = ""
massage_to = test_driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div/label/input")
massage_to.send_keys(name)

time.sleep(5)
choose = test_driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[1]/ul/li[2]/div/a/div/div[2]/div/div/span/span/span")
choose.click()

time.sleep(5)
message = ""
message_box = test_driver.find_element_by_css_selector('.notranslate')
message_box.send_keys(message)

time.sleep(3)
button = test_driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div")
button.click()
