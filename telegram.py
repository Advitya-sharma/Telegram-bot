from selenium import webdriver
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome(executable_path="C:/Users/Advitya/Downloads/c.exe")
driver.get('https://web.telegram.im/')

print("Enter group or contact names saparated by commas\n")

name = input('enter names: ')
name = name.split(",")

msg = input("enter message: ")

input('press enter after entering QR code')
for i in name:
	user = driver.find_element_by_xpath('//span[@my-peer-link="dialogMessage.peerID" and text()="{}"]'.format(i))
	user.click()
	msg_box = driver.find_element_by_xpath('//div[@class="composer_rich_textarea"]')
	msg_box.send_keys(msg)
	driver.find_element_by_xpath('//button[@type="submit"]').click()