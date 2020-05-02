
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')

name = input('Enter name of user or group : ')

msg = input('Enter message : ')

count = int(input('Enter count : '))

input('Enter anything after scanning QR code .....')


user = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[16]/div/div/div[2]/div[1]/div[1]/span/span')

user.click()

msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

for i in range (count):
	msg_box.send_keys(msg)
	button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
	button.click()
