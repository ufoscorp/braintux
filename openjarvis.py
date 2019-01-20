# Imports
import os
from whatsappy import Whatsappy
# Import fuctions
from functions.help import Help
from functions.quit import Quit
Help = Help()
Quit = Quit()

def puttingTitle(title):
    os.system('clear')
    print('''

  ___   ____   ___  ____        ____   ____  ____  __ __  ____ _____
 /   \ |    \ /  _]|    \      |    | /    ||    \|  |  ||    / ___/
|     ||  o  )  [_ |  _  |     |__  ||  o  ||  D  )  |  | |  (   \_ 
|  O  ||   _/    _]|  |  |     __|  ||     ||    /|  |  | |  |\__  |
|     ||  | |   [_ |  |  |    /  |  ||  _  ||    \|  :  | |  |/  \ |
|     ||  | |     ||  |  |    \  `  ||  |  ||  .  \\   /  |  |\    |
 \___/ |__| |_____||__|__|     \____j|__|__||__|\_| \_/  |____|\___|
                                                                    
        ''')
    print(title)

def textInput(question):

    puttingTitle(question)

    answer = input()

    if answer != "":
        return answer
    else:
        return textInput(question + "\n (PLEASE, TYPE SOMETHING)")

def multipleChoice(question, choicesInText):
    
    puttingTitle(question)

    choices = choicesInText.split(';')

    for i in range(len(choices)):
        choice = choices[i]
        print("{} - {}".format(i, choice))

    answer = input()

    if answer.isdigit():
        if int(answer) < len(choices):
            return choices[int(answer)]
        else:
            return multipleChoice(question + "\n (CHOOSE A VALID NUMBER)", choicesInText)
    else:
        return multipleChoice(question + "\n (CHOOSE A NUMBER)", choicesInText)

wantWhatsappy = multipleChoice(
    "You can control your Jarvis by your cellphone, using the Whatsapp Web. Do you want?",
    "Yes;No"
    )

if wantWhatsappy == "Yes":
    groupCreated = multipleChoice("Please, cetificate do you have a group with only yourself (The name of this group needs to be the name of your bot!) \n Everything ok?",
        "Ok!;No, I don't have :("
        )
    if groupCreated == "Ok!":
        browser = multipleChoice("Let we know your browser.",
            "Chrome;Firefox"
            )
        name = textInput("Choose a cute name to your bot :)")
        puttingTitle("Now you have to scan the QR CODE.")
        whatsappy = Whatsappy(browser, name)

    else:
        puttingTitle("Create one and come here one more time")
        exit()
else:
    puttingTitle("Ok! Type the commands from here.")
        
executing = True
output = "What do you want to do? To explore, use the help command."

while executing:

    command = ""

    if wantWhatsappy == "Yes":

        puttingTitle("All the communication is in your cellphone. To explore, use the /cmd help")

        newMessage = whatsappy.checkNewMessage()

        # whatsapp special commands

        if newMessage[0:5] == "/quit":

            whatsappy.sendMessage('Quitting...')
            exit()


        elif newMessage[0:6] == "/shell":

            shellCommand = newMessage[7:]
            whatsappy.sendMessage('Command received -> ' + shellCommand)
            output = os.popen(shellCommand).read()
            output = str(output)
            whatsappy.sendMessage('Command output -> \n' + output)

        elif newMessage[0:4] == "/cmd":

            command = newMessage[5:]

    else:

        command = textInput(output)

    if command != "":

        # the command list
        if command == "help":
            output = Help.text

        else:
            output = "Command doesn't exist!"

        if wantWhatsappy == "Yes":
            whatsappy.sendMessage(output)


