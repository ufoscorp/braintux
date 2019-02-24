#Imports
import sys, pwd, os, time, pynput, ffmpeg, subprocess

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pynput.keyboard import Key, Controller
import speech_recognition as sr

class Whatsapp:

    # Creating an instance of Whatsappy
    def __init__(self, browser, groupname):

        try:
            files = os.listdir('audios')
            for file in files:
                os.remove('audios/'+file)
        except:
            os.makedirs('audios')
        
        try:
            files = os.listdir('videos')
        except:
            os.makedirs('videos')

        self.keyboard = Controller()
        # Creating a variable to the lastMessage
        self.lastMessage = ""
        self.lastAudio = ""
        # Receiving the groupname
        self.groupname = groupname

        # Choosing the browser and creating the driver
        if browser == "Chrome":
            try:
                self.driver = webdriver.Chrome()
            except:
                if os.name=='posix':
                    if not os.path.isfile('/usr/local/bin/chromedriver'):
                        os.system('wget https://chromedriver.storage.googleapis.com/2.46/chromedriver_linux64.zip -O /usr/local/bin/cdriver.zip')
                        os.system('unzip /usr/local/bin/cdriver.zip -d /usr/local/bin')
                        self.driver = webdriver.Chrome()
                    else:
                        raise EnvironmentError("Selenium error. Tip: do not run this script as root.")
                elif os.name == 'nt':
                    print('You need to install a corresponding version of the Chrome driver at http://chromedriver.chromium.org/downloads')
                    raise EnvironmentError("Chrome driver not installed.")
        elif browser == "Firefox":

            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("browser.download.dir", os.getcwd()+'/audios')
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "audio/ogg")
            try:
                self.driver = webdriver.Firefox(firefox_profile=profile)
            except:
                if os.name =='posix':
                    if not os.path.isfile('/usr/local/bin/geckodriver'):
                        os.system('sudo wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz -O /usr/local/bin/gecko.tar.gz')
                        os.system('sudo tar xf /usr/local/bin/gecko.tar.gz -C /usr/local/bin/')
                        self.driver = webdriver.Firefox(firefox_profile=profile)
                    else:
                        raise EnvironmentError("Selenium error. Tip: don't run this script as root.")
                elif os.name == 'nt':
                    print("You need to install the lastest version of gecko driver at: https://github.com/mozilla/geckodriver/releases")
                    raise EnvironmentError("Gecko driver not installed")
                
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
        username = pwd.getpwuid(os.getuid())[0]

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

        while True:
            try:
                sendButton = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div')
                sendButton.click()
                break
            except:
                pass

        clipButton.click()

    # Checking if have a new message
  
        
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

if sys.argv[1] == "start":
    whatsapp=Whatsapp(sys.argv[2], sys.argv[3])

executing = True

while executing:

    # checking receive new message
    newMessage = whatsapp.checkNewMessage();
    if len(newMessage) > 0:
        if "/" in newMessage[0]:
            p = subprocess.Popen("python3 {}/braintux-core.py {}".format(os.getcwd(), newMessage[1:]), shell=True)
        
    # checking send new message
    try:
        with open(os.getcwd()+"/chat.tmp") as chat:
            message = chat.readlines()
            messageType = message[0]

            if messageType == "sendtext":
                whatsapp.sendMessage(message[1])

            if messageType == "sendfile":
                whatsapp.send_attachment(os.getcwd() + '/' + message[1])
    except:
        pass
