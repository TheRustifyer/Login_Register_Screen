import tkinter as tk


class CustomizeWindow:

    def __init__(self, parent):

        self.master = parent

    def set_position(self, win_width, win_height, screen):

        # Using winfo_screenheight and winfo_screenwidth we get the screen's resolution
        screen_resolution_height = screen.winfo_screenheight()
        screen_resolution_width = screen.winfo_screenwidth()
        
        # Window's position is based on the top left corner of the window so we need to calculate where that corner must me to center the window
        x_cordinate = screen_resolution_width // 2 - win_width // 2
        y_cordinate = screen_resolution_height // 2 - win_height // 2

        # First and second parameter are the window's resolution (widthxheight)
        # Third and fourth parameter are the horizontal axis (X) and the vertical axis (y) coordinates where the top left corner of the window will be placed
        screen.geometry(f"{win_width}x{win_height}+{x_cordinate}+{y_cordinate}")
