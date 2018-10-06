import json
from selenium import webdriver
import time

# Path of chromedriver for selenium
driver = webdriver.Chrome("D:\\Programming Files\\chromedriver.exe")
url = 'https://www.presearch.org/login'
driver.get(url)
headers = {'User-Agent': 'Chrome/67.0.3396.99'}

filePath = 'C:\\Users\\HP123\\Documents\\VS Code Projects\\PythonPractice\\WebScraping Practice\\MaleNameData.json'  # Path of json
nameList = []
with open(filePath) as file:
    data = json.load(file)
for i in range(len(data)):
    nameList.append(data[i]['Male'])
print(nameList)

driver.find_element_by_name('email').send_keys(
    "xyz@gmail.com")  # enter your email
driver.find_element_by_name('password').send_keys(
    "123")  # enter your password
driver.find_element_by_xpath(
    '//*[@id="login-form"]/form/div[3]/div[2]/button').click()

for i in nameList:
    time.sleep(2)
    driver.find_element_by_id('search').send_keys(i)
    driver.find_element_by_xpath(
        '//*[@id="search-input"]/div/span/button').click()
    time.sleep(5)
    driver.get(url)
