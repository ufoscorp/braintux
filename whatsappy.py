from selenium import webdriver
import os

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
name = "Whatsapp Bot"
input('Enter any key when you scan the qr code')
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

def sendText(msg, driver):
    msgBox = driver.find_element_by_xpath("//div[@spellcheck='true']")
    msgBox.send_keys(msg)
    button = driver.find_element_by_xpath('//span[@data-icon="send"]')
    button.click()

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
    elif '/command' in lastMsg:
        commandOutput = os.popen(lastMsg[8:]).read()
        sendText('Executando comando {}'.format(lastMsg[8:]), driver)
        commandOutput = str(commandOutput).replace('\n', '')
        sendText(commandOutput, driver)
    elif lastMsg=='/quit':
        sendText('Quitting...', driver)
        executing=False
