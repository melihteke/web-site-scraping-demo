from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url="https://practicetestautomation.com/practice-test-login/"

driver = webdriver.Chrome()  # or the browser of your choice
#driver.get("login_page_url")

driver.get("https://my.cloudtalk.io/login")


email = driver.find_element(By.ID, "UserEmail")
email.send_keys("melihteke@gmail.com")

password = driver.find_element(By.ID, "UserPassword")
password.send_keys("password")

submit_button = driver.find_element(By.CSS_SELECTOR, "input.btn.btn-success.col-xs-12")
submit_button.click()

# New code to get and print the webpage content
page_content = driver.page_source
print(page_content)

# Optionally, you can use BeautifulSoup to parse and interact with the content
soup = BeautifulSoup(page_content, 'html.parser')
print(soup.prettify())
