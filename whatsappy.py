from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
name = "Whatsapp Bot"
input('Enter any key when you scan the qr code')
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
msgBox = driver.find_element_by_xpath("//div[@spellcheck='true']")

msgBox.send_keys('Hello Selenium')
button = driver.find_element_by_xpath('//span[@data-icon="send"]')
button.click()
'''
def send(msg, count=0):
    global msgBox
    global button
    for i in range(count):
        msgBox.send_keys(msg)
        button = driver.find_element_by_xpath('//span[@data-icon="send"]')
        button.click()
send('oi')
'''
