from selenium import webdriver
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
name = "Whatsapp Bot"
input('Enter any key when you scan the qr code')
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

def sendText(msg, driver):
    msgBox = driver.find_element_by_xpath("//div[@spellcheck='true']")
    for ch in msg:
        if ch == "\n":
            ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
        else:
            msgBox.send_keys(ch)
    try:
        button = driver.find_element_by_xpath('//span[@data-icon="send"]')
        button.click()
    except:
        print('mensagem vazia')

msgSent=driver.find_elements_by_class_name('_3zb-j')
lastMsg = msgSent[-1].text
print(lastMsg)
executing=True
while executing:
    msgSent=driver.find_elements_by_class_name('_3zb-j')
    try:
        lastMsg = msgSent[-1].text
    except:
        print('erro ao ler mensagem')
    if lastMsg=='/ping google':
        os.system('ping google.com')
        sendText('Pingando google', driver)
    elif '/command' in lastMsg[0:8]:
        commandOutput = os.popen(lastMsg[8:]).read()
        sendText('Executando comando {}'.format(lastMsg[8:]), driver)
        commandOutput = str(commandOutput)
        sendText(commandOutput, driver)
    elif lastMsg=='/quit':
        sendText('Quitting...', driver)
        executing=False
