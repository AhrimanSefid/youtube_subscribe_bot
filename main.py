from selenium import webdriver
import random

driver = webdriver.Chrome(executable_path='chromedriver')
driver.get("https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Fwww.google.com%2F%3Fgws_rd%3Dssl&hl=hy&dsh=S-1509018558%3A1599071561230994&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp")

names = open('names.txt', 'r')
names_opened = names.read()
nameList = names_opened.split('\n')
names.close()

choosenName = nameList[random.randrange(1, 400)]
choosenLastName = nameList[random.randrange(1, 400)]

password = choosenName + str(random.randrange(10000, 100000))

firstName = driver.find_element_by_name("firstName")
lastName = driver.find_element_by_name("lastName")

username = driver.find_element_by_name("Username")

firstPasswd = driver.find_element_by_name("Passwd")
secondPasswd = driver.find_element_by_name("ConfirmPasswd")

firstBtn = driver.find_element_by_id("accountDetailsNext")

firstName.send_keys(choosenName)
lastName.send_keys(choosenLastName)

username.send_keys(str(random.randrange(10000, 100000)) + choosenName)

firstPasswd.send_keys(password)
secondPasswd.send_keys(password)

firstBtn.click()

numDriver = webdriver.Chrome(executable_path='chromedriver')
numDriver.get("https://temp-sms.org/")

number = numDriver.find_element_by_css_selector('.number.black-text')
number_txt = number.text

number.click()

numInp = driver.find_element_by_id('phoneNumberId')
numInp.send_keys(number_txt)

secondBtn = driver.find_element_by_css_selector('.VfPpkd-RLmnJb')
secondBtn.click()

#numDriver.quit()
#driver.quit()
