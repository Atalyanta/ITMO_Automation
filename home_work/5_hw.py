from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.CSS_SELECTOR, [id="user-name"])
password = driver.find_element(By.CSS_SELECTOR, body > div > div > div > div > div > div > form > div > input)
submit = driver.find_element(By.CSS_SELECTOR, "input#login-button.submit-button.btn_action")
if username is None:
    print('Элементы не найдены')
elif password is None:
    print('Элементы не найдены')
elif submit is None:
    print('Элементы не найдены')
else:
    print('Элементы найдены')