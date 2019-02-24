import os, subprocess

class Terminal:

    def __init__(self):

        pass
    
    def sendMessage(self, title):
        print("Braintux: "+title)

terminal = Terminal()

executing = True
oldMessage = ""

while True:

    # checking send new message
    try:
        with open(os.getcwd()+"/chat.tmp", "r", os.O_NONBLOCK) as chat:
            message = chat.read()
            
            if message != oldMessage:

                messageType = message[0:8]

                if messageType == "sendtext":
                    terminal.sendMessage(message[8:])

                if messageType == "sendfile":
                    terminal.sendMessage('New file in: ' + os.getcwd() + '/' + message[8:])
            
            oldMessage = str(message)
    except:
        pass