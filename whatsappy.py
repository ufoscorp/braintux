# Imports
from selenium import webdriver
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
import pynput
import time

class Whatsappy:

    # Creating an instance of Whatsappy
    def __init__(self, browser, name):

        self.keyboard = Controller()
        # Creating a variable to the lastMessage
        self.lastMessage = ""
        # Receiving the name
        self.name = name

        # Choosing the browser and creating the driver
        if browser == "Chrome":
            self.driver = webdriver.Chrome()

        elif browser == "Firefox":
            self.driver = webdriver.Firefox()

        else:
            print("Error! This browser don't exist in our list.")
            exit()

        # Entering on the Whatsapp Web site
        self.driver.get("https://web.whatsapp.com")

        # waiting the QR CODE scan
        while True:
            try:
                user = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
                user.click()
                break
            except:
                pass

        # Getting the username using whoami command
        username = os.popen("whoami").read()
        username = str(username)[:len(username)-1]

        # Waiting the loading of the page
        time.sleep(2)

        # Sending the initial message
        self.sendMessage("{} connected your Jarvis named by {}.".format(username, self.name))

    # Function to send messages
    def sendMessage(self, message):

        # Searching the text box
        textBox = self.driver.find_element_by_xpath("//div[@spellcheck='true']")
        # Checking if the message isn't empty
        if message != "":
            # Adding the bot name to the message
            message = self.name + ": \n" + str(message) + "\n"
            # Sending the characteres
            textBox.send_keys(message)
            
    # davi q fez, nem sei como funciona, é noix
    def send_attachment(self, path):

        # Attachment Drop Down Menu
        clipButton = self.driver.find_element_by_xpath('//div[@title="Anexar"]')
        clipButton.click()
        time.sleep(1)

        # To send Videos and Images.
        mediaButtons = self.driver.find_elements_by_class_name('GK4Lv')
        mediaButtons[0].click()
        self.keyboard.type(path)
        self.keyboard.press(pynput.keyboard.Key.enter)
        self.keyboard.release(pynput.keyboard.Key.enter)
        time.sleep(2)
        self.keyboard.press(pynput.keyboard.Key.enter)
        self.keyboard.release(pynput.keyboard.Key.enter)
        time.sleep(2)
        self.keyboard.press(pynput.keyboard.Key.enter)
        self.keyboard.release(pynput.keyboard.Key.enter)


    # Checking if have a new message
    def checkNewMessage(self):

        # Catching all the messages
        messages = self.driver.find_elements_by_class_name('_3zb-j')
        # Supposed new message is the last message
        newMessage = messages[-1].text

        # Checking if the new message isn't igual to the last message
        if newMessage != self.lastMessage:
            # We have a new message
            self.lastMessage = newMessage
            return newMessage

        else:
            # No new message
            return ""
