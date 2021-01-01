import tkinter as tk
import os

from custom_actions import CustomizeWindow
from custom_widgets import TitleBar, TaskBar, BackButton



class MainApplication(tk.Frame):

	def __init__(self, master, *args, **kwargs):  # implement (Saved_login)

		super().__init__(master, *args, **kwargs)

		# Here starts the party
		self.master = master
		self.master.title('Here is your title')
		self.master.configure(bg='white')
		self.cwindow = CustomizeWindow(self.master)
		# Geometry management
		self.height = 1200
		self.width = 800
		self.cwindow.set_position(self.height, self.width, self.master)
		
		# Setting up our main window and overwritten actions	
	def main_titlebar(self):

		self.title_bar = TitleBar(self.master)
		self.title_bar.create_title_bar()
		# self.title_bar.set_icon('./media/images/{your_image_here}')
		
		if os.name == 'nt':
	
			self.title_bar.set_close_button()
			self.title_bar.set_minimize_button()

	def main_menubar(self, isLogged=False, testing=False):
		
		try:
			
			self.title_bar.clear_menubar()
			self.title_bar.create_menubar(isLogged, testing)
		
		except AttributeError as error:

			print(f'Otra vez has mandado al Garbage collector la title_bar:\n{error}')

		
		
		from scene_director import Scene
		self.scene = Scene(self.master)
		self.scene.inicial_scene()
		


		
#	<<<<<<<<<<<<<<---------------------------- Main program ------------------------------>>>>>>>>>>>>>>>>>>>

if __name__ == '__main__':
	
	# Calling Tkinter class and creating a new title bar
	main_screen = tk.Tk()

	# Instanciating main_app...
	my_app = MainApplication(main_screen)
	my_app.main_titlebar()
	my_app.main_menubar()

	# Running the mainloop method... It's like a while True:) !!
	main_screen.mainloop()

