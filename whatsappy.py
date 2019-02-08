#Imports
from selenium import webdriver
import os
import urllib.request
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pynput.keyboard import Key, Controller
import pynput
import time
import speech_recognition as sr
import ffmpeg

class Whatsappy:

    # Creating an instance of Whatsappy
    def __init__(self, browser, groupname):

        try:
            files = os.listdir('audios')
        except:
            os.makedirs('audios')
            files = os.listdir('audios')
        for file in files:
            os.remove('audios/'+file)

        self.keyboard = Controller()
        # Creating a variable to the lastMessage
        self.lastMessage = ""
        self.lastAudio = ""
        # Receiving the groupname
        self.groupname = groupname

        # Choosing the browser and creating the driver
        if browser == "Chrome":
                self.driver = webdriver.Chrome()

        elif browser == "Firefox":

            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("browser.download.dir", os.getcwd()+'/audios')
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "audio/ogg")
            
            self.driver = webdriver.Firefox(firefox_profile=profile)

        else:
            print("Error! This browser don't exist in our list.")
            exit()

        # Entering on the Whatsapp Web site
        self.driver.get("https://web.whatsapp.com")

        # waiting the QR CODE scan
        while True:
            try:
                user = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(groupname))
                user.click()
                break
            except:
                pass

        # Getting the username using whoami command
        username = os.popen("whoami").read()
        username = str(username)[:len(username)-1]

        # Waiting the loading of the page
        time.sleep(10)

        # Sending the initial message
        self.sendMessage("{} connected your BrainTux".format(username))

    # Function to send messages
    def sendMessage(self, message):

        # Searching the text box
        textBox = self.driver.find_element_by_xpath("//div[@spellcheck='true']")
        # Checking if the message isn't empty
        if message != "":
            # Adding the bot name to the message
            message = "BrainTux: \n" + str(message) + "\n"
            # Sending the characteres
            textBox.send_keys(message)
            
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
    def youtubeSearch(self, search):
        pass
        
    def checkNewMessage(self):

        # Catching all the audios
        audios = self.driver.find_elements_by_class_name('_2jfIu')

        # Verifying if there is no audios
        if len(audios) != 0:

            # if audios is not empty, audiosLink cannot be empty
            audiosLink = self.driver.find_elements_by_tag_name('audio')

            while True:
                if len(audiosLink) == 0:
                    time.sleep(1)
                    audiosLink = self.driver.find_elements_by_tag_name('audio')
                else:
                    break

            newAudio = audiosLink[-1].get_attribute('src')

            try:
                # Mouse hover on the last audio
                ActionChains(self.driver).move_to_element(audios[-1]).perform()
                inScreen = True
            except:
                inScreen = False

            if newAudio != self.lastAudio and inScreen:

                self.lastAudio = newAudio

                # Finding the options button
                optionsButton = self.driver.find_elements_by_xpath('//div[@data-js-context-icon="true"]')

                while True:
                    try:
                        # Clicking this
                        optionsButton[-1].click()
                        # Finding the download button
                        downloadButton = self.driver.find_element_by_xpath("//div[@title='Baixar']")
                        break
                    except:
                        # Wait
                        time.sleep(1)

                # Clicking this
                downloadButton.click()
                # Waiting the download
                time.sleep(3)
                # Converting ogg to wav
                os.popen("ffmpeg -i audios/* audios/audio.wav -loglevel panic")
                # Waiting the conversion
                time.sleep(1)
                # GO
                
                r = sr.Recognizer()
                with sr.AudioFile("audios/audio.wav") as source:
                    audio = r.record(source)

                try:
                    # This is the result
                    speech = r.recognize_google(audio)
                    speech = '/audio ' + speech
                    # Removing the audio
                    files = os.listdir('audios')
                    for file in files:
                        os.remove('audios/'+file)
                    return speech
                except Exception as e:
                    print("Exception: "+str(e))
                    exit()

        

        # Catching all the messages
        messages = self.driver.find_elements_by_class_name('_3zb-j')
        if len(messages) != 0:
            # Supposed new message is the last message
            newMessage = messages[-1].text

            # Checking if the new message isn't iqual to the last message
            if newMessage != self.lastMessage:
                # We have a new message
                self.lastMessage = newMessage
                return newMessage

            else:
                # No new message
                return ""
        
        return ""