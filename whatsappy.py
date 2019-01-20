from selenium import webdriver
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
import pynput
import time
keyboard = Controller()

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
name = "Whatsapp Bot"
input('Enter any key when you scan the qr code')
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

def sendText(msg, driver):
    msgBox = driver.find_element_by_xpath("//div[@spellcheck='true']")
    msgBox.send_keys(msg)
    if len(msg)>1:
        button = driver.find_element_by_xpath('//span[@data-icon="send"]')
        button.click()
    except:
        print('Empty messagee')

def send_attachment(path):
    global driver
    # Attachment Drop Down Menu
    clipButton = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span')
    clipButton.click()
    time.sleep(1)

    # To send Videos and Images.
    mediaButton = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button')
    mediaButton.click()
    keyboard.type(path)
    keyboard.press(pynput.keyboard.Key.enter)
    keyboard.release(pynput.keyboard.Key.enter)
    keyboard.press(pynput.keyboard.Key.enter)
    keyboard.release(pynput.keyboard.Key.enter)


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
