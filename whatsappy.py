# Imports
from selenium import webdriver
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
import pynput
import time

class Whatsappy:

    def __init__(self, browser, name):

        self.keyboard = Controller()
        self.lastMessage = ""
        self.name = name

        if browser == "Chrome":
            self.driver = webdriver.Chrome()

        elif browser == "Firefox":
            self.driver = webdriver.Firefox()

        else:
            print("Error! This browser don't exist in our list.")
            exit()

        self.driver.get("https://web.whatsapp.com")

        # waiting the QR CODE scan

        while True:
            try:
                user = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
                user.click()
                break
            except:
                pass

        username = os.popen("whoami").read()
        username = str(username)[:len(username)-1]

        self.sendMessage("{} connected your Jarvis named by {}.".format(username, self.name))

    def sendMessage(self, message):

        textBox = self.driver.find_element_by_xpath("//div[@spellcheck='true']")
        if len(message)>0:
            message = self.name + ": \n" + message + "\n"
            textBox.send_keys(message)
            

    def send_attachment(self, path):

        # Attachment Drop Down Menu
        clipButton = self.driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span')
        clipButton.click()
        time.sleep(1)

        # To send Videos and Images
        mediaButton = self.driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button')
        mediaButton.click()
        self.keyboard.type(path)
        self.keyboard.press(pynput.keyboard.Key.enter)
        self.keyboard.release(pynput.keyboard.Key.enter)
        self.keyboard.press(pynput.keyboard.Key.enter)
        self.keyboard.release(pynput.keyboard.Key.enter)

    def checkNewMessage(self):

        messages = self.driver.find_elements_by_class_name('_3zb-j')
        newMessage = messages[-1].text

        if newMessage != self.lastMessage:
            # We have a new message
            self.lastMessage = newMessage

            return newMessage

        else:

            return ""