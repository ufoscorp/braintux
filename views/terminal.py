import os

class Term:

    def __init__(self):

        pass
    
    def putTitle(self, title):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(r'''
        ____             _     ______          
       / __ )_________ _(_)___/_  __/_  ___  __
      / __  / ___/ __ `/ / __ \/ / / / / / |/_/
     / /_/ / /  / /_/ / / / / / / / /_/ />  <  
    /_____/_/   \__,_/_/_/ /_/_/  \__,_/_/|_|  
                                                                                                        
            ''')
        print(title)