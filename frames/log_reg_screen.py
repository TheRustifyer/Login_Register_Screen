import tkinter as tk
from tkinter import messagebox
from user import User
from scene_director import Scene
from custom_widgets import BackButton

class LoginRegister():

    def __init__(self, master):

        # super().__init__(master)
        self.master = master

        self.black_bg = '#2c2c2c'

        self.current_user = User()

        self.new_scene = Scene().new_scene

        self.back_button = BackButton().back_button
        self.back_acc = BackButton().back_acc


    def registration_screen(self):

        def on_entry_click(event, entry_variable):
            """function that gets called whenever entry is clicked"""

            if entry_variable.get() == '' or entry_variable.cget('fg') == 'grey':
                
                entry_variable.delete(0, "end")  # Delete all the text in the entry

                entry_variable.insert(0, '')  # Insert blank for user input

                entry_variable.config(fg='black')

        def on_focusout(event, entry_variable, entry_placeholder):

            if entry_variable.get() == '' or entry_variable.cget('fg') == 'grey':
                
                entry_variable.insert(0, entry_placeholder)

                entry_variable.config(fg='grey')

        # The new blueprint! The most important step on the code... and same for al methods that manage different the different windows
        frame = tk.Frame(self.master, bg='white')
        frame.pack()

        # New user data
        username = ''
        password = ''
        password_match = ''

        # Requiring an action
        tk.Label(frame, text="Complete the requested data to registrate your account",
                 bg="lightblue", width="300", height="2", font=("Verdana", 25)).pack()
        tk.Label(frame, text="", bg='white').pack(pady=70)

        # Username
        username_register_entry = tk.Entry(frame, width=20, textvariable=username, font=('Verdana', 25), bd=1,
                                           relief='solid')
        username_register_entry.placeholder = 'Username'

        username_register_entry.insert(0, username_register_entry.placeholder)
        username_register_entry.bind('<FocusIn>', lambda event: on_entry_click(event, username_register_entry))
        username_register_entry.bind('<FocusOut>', lambda event: on_focusout(event, username_register_entry,
                                                                             username_register_entry.placeholder))
        username_register_entry.config(fg='grey')
        username_register_entry.pack(pady=(0, 50))  # Only applies padding on bottom on vertical axis

        # Password
        password_register_entry = tk.Entry(frame, width=20, textvariable=password, font=('Verdana', 25), show='*', bd=1,
                                           relief='solid')
        password_register_entry.placeholder = 'Password'

        password_register_entry.insert(0, password_register_entry.placeholder)
        password_register_entry.bind('<FocusIn>', lambda event: on_entry_click(event, password_register_entry))
        password_register_entry.bind('<FocusOut>', lambda event: on_focusout(event, password_register_entry,
                                                                             password_register_entry.placeholder))
        password_register_entry.config(fg='grey')
        password_register_entry.pack()

        # Password match
        password_match_register_entry = tk.Entry(frame, width=20, textvariable=password_match, font=('Verdana', 25),
                                                 show='*', bd=1, relief='solid')
        password_match_register_entry.placeholder = 'Password'

        password_match_register_entry.insert(0, password_match_register_entry.placeholder)
        password_match_register_entry.bind('<FocusIn>',
                                           lambda event: on_entry_click(event, password_match_register_entry))
        password_match_register_entry.bind('<FocusOut>', lambda event: on_focusout(event, password_match_register_entry,
                                                                                   password_match_register_entry.placeholder))
        password_match_register_entry.config(fg='grey')
        password_match_register_entry.pack(pady=20)

        # Calling the register accion
        reg_img = tk.PhotoImage(file='./media/images/rare_foward.png')
        reg_acc = tk.Button(frame, image=reg_img, bg='white', relief='flat', activebackground='white', bd=0, height=256,
                            width=256,
                            command=lambda: register_user())
        reg_acc.image = reg_img
        reg_acc.pack(pady=30)

        # Back to main screen button...
        self.back_button('login_register_decision_screen', frame)

        def register_user():

            # Getting the user data from the father method
            username = username_register_entry.get()
            password = password_register_entry.get()
            pass_checker = password_match_register_entry.get()

            # Erase all dirty labels!
            for label in frame.winfo_children():

                if label['fg'] == 'red':
                    label.destroy()

            # Validating password strenght
            if len(password) < 8 or password.islower() or username == 'Username' or password == 'Password':

                short_password = tk.Label(frame, text="Password have to had at least 8 characters long and start with a capital letter.",
                                          fg="red", bg='white', font=("Verdana", 15))
                short_password.pack(pady=30)

                # Erasing the entried data from the screen
                username_register_entry.pack_forget()
                password_register_entry.pack_forget()
                password_match_register_entry.pack_forget()
                self.back_acc.place_forget()
                reg_acc.pack_forget()

                # Trying again...
                trying_again_button = tk.Button(frame, text='TRY AGAIN', font=("Verdana", 18), fg='white', width=20,
                                                height=2, bg=self.black_bg, activebackground='white',
                                                command=lambda: self.new_scene('registration_screen', frame))
                trying_again_button.pack()

            elif password != pass_checker:

                password_unmatch_notification = tk.Label(frame, fg='red', bg='white', text='Password do not match. Please, try again!', 
                                                        font=('Verdana', 20))
                password_unmatch_notification.pack()

                password_register_entry.delete(0, tk.END)
                password_match_register_entry.delete(0, tk.END)
                password_match_register_entry.delete(0, tk.END)

            # Grabbing all the things and finally registring an user
            else:

                self.current_user.set_user(username, password)

                my_data = self.current_user.check_user_in_db()

                if my_data == []:

                    # Cheking if user are sure about entried data...
                    response = messagebox.askokcancel("User credentials", "This will be your credentials. \nAre you sure?")

                    if response:

                        self.current_user.new_user()

                        reg_succ = tk.Label(frame, text='Registration Success', bg='white', fg='green',
                                            font=('Verdana', 15))
                        reg_succ.pack(pady=20)

                        continue_button = tk.Button(frame, text='CONTINUE', fg='white', width=20, height=2,
                                                    bg=self.black_bg, activebackground='white',
                                                    command=lambda: self.new_scene('login_register_decision_screen',
                                                                                   frame))
                        continue_button.pack(pady=20)

                        # Erasing the entried data from the screen
                        username_register_entry.delete(0, len(username))
                        password_register_entry.delete(0, len(password))
                        password_match_register_entry.delete(0, tk.END)

                        # Erasing the registry and back buttons if registry goes correctly
                        reg_acc.pack_forget()
                        # back_acc.pack_forget()

                        self.current_user.new_user()

                    else:

                        # Aborting registration
                        reg_aborted = tk.Label(frame, text="Another chance", fg="red", font=("comicsans", 15))
                        reg_aborted.pack()

                        # Erasing the entried data from the screen
                        username_register_entry.delete(0, len(username))
                        password_register_entry.delete(0, len(password))
                        password_match_register_entry.delete(0, tk.END)

                else:  # If data != []

                    # Error label because username is already on DB
                    reg_failed = tk.Label(frame, text="Username already taken. Choose another one.", fg="red",
                                          font=("Verdana", 15))
                    reg_failed.pack()

                    # Erasing the entried data from the screen
                    username_register_entry.pack_forget()
                    password_register_entry.pack_forget()
                    password_match_register_entry.pack_forget()
                    self.back_acc.place_forget()
                    reg_acc.pack_forget()

                    # Trying again...
                    trying_again_button = tk.Button(frame, text='TRY AGAIN', fg='yellow', width=20, height=2, bg='red',
                                                    activebackground='white',
                                                    command=lambda: self.new_scene('registration_screen', frame))
                    trying_again_button.pack()

    # As a notation, if u don't use lambda as the command function, Buttom appers executed before do anything on previous frame.

    #    <<<<<<<<<<<<<<---------------------------- Login methods ------------------------------>>>>>>>>>>>>>>>>>>>

    # Making the screen where the users log in
    def login_screen(self):

        def on_entry_click(event, entry_variable):
            """function that gets called whenever entry is clicked"""

            if entry_variable.get() == '' or entry_variable.cget('fg') == 'grey':
                
                entry_variable.delete(0, "end")  # delete all the text in the entry
                
                entry_variable.insert(0, '')  # Insert blank for user input
                
                entry_variable.config(fg='black')

        def on_focusout(event, entry_variable, entry_placeholder):

            if entry_variable.get() == '' or entry_variable.cget('fg') == 'grey':
                
                entry_variable.insert(0, entry_placeholder)
                
                entry_variable.config(fg='grey')

        # The new blueprint! The most important step on the code...
        frame = tk.Frame(self.master, bg='white')
        frame.pack()

        # Cheking user credentials
        username_verify = ''
        password_verify = ''

        # Required action
        tk.Label(frame, text="Enter your username and password", bg="lightblue", bd=1, relief='solid',
                 width="300", height="2", font=('Verdana', 25)).pack()
        tk.Label(frame, text="", bg='white').pack(pady=75)

        # # Username
        username_login_entry = tk.Entry(frame, width=20, textvariable=username_verify, font=('Verdana', 25), bd=1,
                                        relief='solid')
        username_login_entry.placeholder = 'Username'

        username_login_entry.insert(0, username_login_entry.placeholder)
        username_login_entry.bind('<FocusIn>', lambda eventa: on_entry_click(eventa, username_login_entry))
        username_login_entry.bind('<FocusOut>', lambda eventa: on_focusout(eventa, username_login_entry,
                                                                           username_login_entry.placeholder))
        username_login_entry.config(fg='grey')
        username_login_entry.pack(pady=(0, 50))  # Only applies padding on bottom on vertical axis

        # # Password
        password_login_entry = tk.Entry(frame, width=20, textvariable=password_verify, font=('Verdana', 25), show='*', bd=1, relief='solid')
        password_login_entry.placeholder = 'Password'

        password_login_entry.insert(0, password_login_entry.placeholder)
        password_login_entry.bind('<FocusIn>', lambda eventa: on_entry_click(eventa, password_login_entry))
        password_login_entry.bind('<FocusOut>', lambda eventa: on_focusout(eventa, password_login_entry, password_login_entry.placeholder))
        password_login_entry.config(fg='grey')
        password_login_entry.pack()

        # Calling the verify login action
        login_img = tk.PhotoImage(file='./media/images/rare_foward.png')
        login_acc = tk.Button(frame, image=login_img, bg='white', relief='flat', activebackground='white', bd=0,
                              height=256, width=256,
                              command=lambda: login_verify())
        login_acc.image = login_img
        login_acc.pack(pady=30)

        # Back to main screen button...
        self.back_button('login_register_decision_screen', frame)

        def login_verify():

            username_verify = username_login_entry.get()
            password_verify = password_login_entry.get()

            # Erasing entered data from the screen
            username_login_entry.delete(0, len(username_verify))
            password_login_entry.delete(0, len(password_verify))

            self.current_user.set_user(username_verify, password_verify)
            
            data = self.current_user.check_user_in_db(True)

            if data:    

                login_succ = tk.Label(frame, text="Logged successfully!", bg='white', fg="green",
                                      font=('Verdana', 25))
                login_succ.pack(pady=(50, 50))

                continue_button = tk.Button(frame, text='CONTINUE', fg='white', width=20, height=2,
                                            bg=self.black_bg, font=('Verdana', 15),
                                            activebackground='white',
                                            command=lambda: self.new_scene('main_client_window',
                                                                           frame))
                continue_button.pack()

                # Cleaning the screen to avoid to repeat entering data
                username_login_entry.pack_forget()
                password_login_entry.pack_forget()
                login_acc.pack_forget()
                self.back_acc.pack_forget()

            else:

                # Cleaning the screen to avoid to repeat entering data
                username_login_entry.pack_forget()
                password_login_entry.pack_forget()
                login_acc.pack_forget()
                self.back_acc.pack_forget()

                login_failed = tk.Label(frame,
                                        text="SOMETHING WENT WRONG!\n Please, introduce your credentials again.",
                                        fg="red", bg='white', font=("Verdana", 15))
                login_failed.pack(pady=30)

                try_again_button = tk.Button(frame, text='TRY AGAIN', fg='white', width=20,
                                             height=2, bg=self.black_bg, activebackground='white',
                                             command=lambda: self.new_scene('login_screen', frame))
                try_again_button.pack(pady=(30))

            
    def login_register_decision_screen(self):

        # for widget in self.title_bar.winfo_children():

        #     if type(widget) != tk.Label and type(widget) != tk.Button:
        #         widget.destroy()


        # The new blueprint! The most important step on the code...
        frame = tk.Frame(self.master, bg='white')
        frame.pack(fill='both')

        # Labels and buttons to choose the login/register action
        tk.Label(frame, text="WELCOME! Select Your Choice", bg="lightblue", width="300", height="2",
                 font=("Verdana", 20)).pack()
        tk.Label(frame, text="", bg='white').pack(pady='90')

        tk.Button(frame, text="Login", width="25", height="2", fg='white', bg=self.black_bg, relief='flat', bd=1,
                  activebackground='white', font=("Verdana", 20),
                  command=lambda: self.new_scene('login_screen', frame)).pack(anchor='e', side='top', padx='50')

        tk.Button(frame, text="Register", height="2", width="25", fg='white', bg=self.black_bg, relief='flat', bd=1,
                  activebackground='white', font=("Verdana", 20),
                  command=lambda: self.new_scene('registration_screen', frame)).pack(anchor='e', side='top', padx='50',
                                                                                     pady='50')

        # Placing a corporative image if you want
        # background_img = tk.PhotoImage(file='./media/images/0dcmainsmall.png')
        # background_label = tk.Label(frame, image=background_img, bg='white')
        # background_label.image = background_img
        # background_label.place(x=0, y=190, relwidth=0.5, relheight=0.5)

        # tk.Label(frame, text="", bg='white').pack(pady='150')

    #    <<<<<<<<<<<<<<<<----------------------------------------- End of the LOGIN SCREEN CODE! ----------------------------------------->>>>>>>>>>>>>>>>>>>
