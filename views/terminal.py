import os, subprocess

class Terminal:

    def __init__(self):

        pass
    
    def putTitle(self, title):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''
        ____             _     ______          
       / __ )_________ _(_)___/_  __/_  ___  __
      / __  / ___/ __ `/ / __ \/ / / / / / |/_/
     / /_/ / /  / /_/ / / / / / / / /_/ />  <  
    /_____/_/   \__,_/_/_/ /_/_/  \__,_/_/|_|  
                                                                                                        
            ''')
        print(title)

terminal = Terminal()

executing = True

while True:

    # checking send new message
    try:
        with open(os.getcwd()+"/chat.tmp") as chat:
            message = chat.read()
            print(message)
            messageType = message[0:8]

            if messageType == "sendtext":
                putTitle(message[8:])

            if messageType == "sendfile":
                putTitle('New file in: ' + os.getcwd() + '/' + message[8:])
    except:
        pass