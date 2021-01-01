import tkinter as tk
from custom_actions import CustomizeWindow
from scene_director import Scene
from user import User
import os


class TitleBar:
    '''Creates a new fully customizable TitleBar and events for'''
    def __init__(self, master, *args, **kwags):
        
        self.master = master

        self.win_control = 1
        self._offsetx = 0
        self._offsety = 0

        self.cwindow = CustomizeWindow(self.master)
    
    def create_title_bar(self):
        
        self.title_bar = tk.Frame(self.master, bg='black')
        self.title_bar.pack(fill='x')
        
        if os.name == 'nt':

            self.task_bar = TaskBar()
                    # Here we destroy the title bar provided by default for WINDOWS10 window manager and let's start to create a new one
            self.master.overrideredirect(True)
            self.master.after(10, lambda: self.task_bar.set_appwindow(self.master))
            
            def frame_mapped(event=None):

                self.master.overrideredirect(True)

                if self.win_control == 1:

                    self.task_bar.set_appwindow(self.master)
                    
                    self.win_control = 0


            def window_drag(event):
                
                x = self.master.winfo_pointerx() - self._offsetx
                y = self.master.winfo_pointery() - self._offsety

                self.master.geometry(f'+{x}+{y}')

            def click_window(event):
                
                self._offsetx = event.x
                self._offsety = event.y

            # Binding functions to hardware actions
            self.master.bind("<Map>", frame_mapped) # This brings back the window
            self.title_bar.bind('<Button-1>', click_window)
            self.title_bar.bind('<B1-Motion>', window_drag)

    def set_icon(self, path):

        background_img = tk.PhotoImage(file=path)
        background_label = tk.Label(self.title_bar, image=background_img)
        background_label.image = background_img  # U have to reference the img or the garbage collector will flip it away
        background_label.pack(side='left', padx=3)
    
    def create_button(self, action, text):
    
        button = tk.Button(self.title_bar, text=text, command = action, bg="#2e2e2e", padx=3, pady=3, 
        activebackground='red', width=4, bd=0, font="bold", fg='white', highlightthickness=0)
        
        button.pack(side='right')
        
        return button
    
    def change_color_on_hovering(self, event, button, color='red'):
            
            if button:
                
                button['bg'] = color

    def return_color_to_normalstate(self, event, button, color='#2c2c2c'):
            
            if button:
                
                button['bg'] = color


    def set_close_button(self):

        def close_button_actions():
            
            if User.want_exit_popup_anymore:
            
                response = tk.messagebox.askokcancel("Salir", "Esta acción cerrará esta ventana. \nEstás seguro?")

                if response:
                
                    self.master.destroy()

            else:

                self.master.destroy()

        close_button = self.create_button(close_button_actions, 'X')
        close_button.bind('<Enter>', lambda event: self.change_color_on_hovering(event, close_button))
        close_button.bind('<Leave>', lambda event: self.return_color_to_normalstate(event, close_button))
    
    def set_minimize_button(self):

        def minimize_window():

            self.master.withdraw()
            self.master.overrideredirect(False)
            self.master.iconify()

            self.win_control = 1

        minimize_button = self.create_button(minimize_window, '_')
        minimize_button.bind('<Enter>', lambda event: self.change_color_on_hovering(event, minimize_button))
        minimize_button.bind('<Leave>', lambda event: self.return_color_to_normalstate(event, minimize_button))

    
    
    def create_menubar(self, isLogged=None,testing=False):
        
        self.menubar = MenuBar(self.title_bar)

    def clear_menubar(self):
        
        for children in self.title_bar.winfo_children():
            
            if type(children) == tk.Menubutton:
                children.destroy()


# # <<<<<<<<<<<<<<<<<<< --------------- Custom Buttons ----------------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class BackButton:

    def __init__(self):
        
        from scene_director import Scene
        
        self.scene = Scene()
        self.back_acc = None
	
    def back_button(self, scene, frame):

        btn_img = tk.PhotoImage(file='./media/images/backbutton1.png')
        self.back_acc = tk.Button(frame, image=btn_img, width=60, height=60, relief='flat', bg='white', activebackground='red', 
            command=lambda: self.scene.new_scene(scene, frame))
        self.back_acc.image = btn_img
        self.back_acc.place(x=12, y=12)



# <<<<<<<<<<<<<<<<<<< --------------- Menu Bar ----------------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class MenuBar:


    def __init__(self, parent, logged = None, *args, **kwargs):

        self.master = parent
       
        self.about = About(self.master)


# About
class About(TitleBar):

    def __init__(self, parent):

        super().__init__(parent)

        self.master = parent

        self.about_menu_button = tk.Menubutton(self.master, text="Your text here", relief='flat',bg='black', fg='white')

        self.about_menu_button.menu = tk.Menu(self.about_menu_button, tearoff=0)
        self.about_menu_button["menu"] = self.about_menu_button.menu

        self.about_menu_button.menu.add_command(label="Help", command=self.helpy)
        self.about_menu_button.menu.add_separator()
        self.about_menu_button.menu.add_command(label="Version", command=self.version)
        self.about_menu_button.menu.add_command(label="Your business here", command=self.zerodaycode) # Always feel free to change this!

        self.about_menu_button.pack(side='left', padx=10)


    def helpy(self):  # Change it and make it like a real help window

        helpy_window = tk.Toplevel()

        self.cwindow.set_position(600, 150, helpy_window)

        helpy_label = tk.Label(helpy_window, text='''For see a complete guide of the program, please, visit our page www.zerodaycode.eu,
            and u will find all the references to completly use all the features''', font=('Verdana', 12))
            
        helpy_label.pack()


    def version(self):  # Make a @classmethod from setputools that autoupdate this top level every patch

        version_window = tk.Toplevel()

        version_label = tk.Label(version_window, text='''
            Version 1.0, released on 26/10/2020''', font=('Verdana', 12))

        version_label.pack()

    def zerodaycode(self):

        zerodaycode_window = tk.Toplevel()

        zerodaycode_label = tk.Label(zerodaycode_window, text=""" Hey there """,
                                    font=('Verdana', 12))

        zerodaycode_label.pack()

    
# <<<<<<<<<<<<<<<<<<< --------------- Task Bar ----------------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class TaskBar:

    def __init__(self):

        pass

    # Some WindowsOS styles, required for task bar integration
    def set_appwindow(self, mainWindow):
        
        try:
            
            from ctypes import windll
            import ctypes

        except:

            print('If Windows is not the OS, this will not work.')
        
        def set_taskbar_icon():
            '''This function just allows developer to replace the Python generic 
            taskbar icon setting an unique task ID'''
            
            myappid = 'zerodaycode.socialmediamanagement.1.0' # Feel free to put your desired name here. It's just for windows be able to identify the PID of this window
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
            

        set_taskbar_icon()

        GWL_EXSTYLE = -20
        WS_EX_APPWINDOW = 0x00040000
        WS_EX_TOOLWINDOW = 0x00000080

        hwnd = windll.user32.GetParent(mainWindow.winfo_id())
        stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        stylew = stylew & ~WS_EX_TOOLWINDOW
        stylew = stylew | WS_EX_APPWINDOW
        windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)

        # re-assert the new window style
        mainWindow.wm_withdraw()
        mainWindow.after(10, lambda: mainWindow.wm_deiconify())
