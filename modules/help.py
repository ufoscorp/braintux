class Help:

	def __init__(self):
		self.text = '''
		Here you can explore all the commands!

		Whatsapp exclusives:
			/help - Will open this command list
			/send <directory> - Will send an archive
			/shell <command> - Will execute a command in the 
			/quit - Will close the program

			/cmd <command> - Will execute a non whatsapp exclusive command

		help - Will open this command list
		quit - Will close the program
		    '''

	def echo(self):

		print(self.text)