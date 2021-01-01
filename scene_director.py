# Creating a director mode, instead using top level and end having multiple widgets, we put a 'paper over a paper'

class Scene:

    def __init__(self, master=None):

        self.master = master

        # Instanciating our User Class, who acts as an intermediate handling data, or checking user current status
        from user import User
        self.logged_user = User().is_logged()

    def inicial_scene(self):

        if not self.logged_user:
            
            from frames.log_reg_screen import LoginRegister
            self._lr = LoginRegister(self.master)
            
            self._lr.login_register_decision_screen()

        else:
            
            pass
            # Feel free to upgrade if you have an active session of your user or whatever
            

    def new_scene(self, scene, frame):

        frame.destroy()  # Destroys the previous frame, which holds all buttons, labels, entries, etc
        
        from frames.log_reg_screen import LoginRegister
        self._lr = LoginRegister(self.master)
        

        # A dictionary with references to all your scenes. Add each new scene function to here
        go_to = {

            'login_register_decision_screen': self._lr.login_register_decision_screen,
            'login_screen': self._lr.login_screen,
            'registration_screen': self._lr.registration_screen,
        }

        # Pointing to the right function
        go_to[scene]()