from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager , Screen
import json , glob
import random
from hoverable import HoverBehavior
from datetime import datetime
from pathlib import Path
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

Builder.load_file('gui.kv')


class LoginScreen(Screen):
    def signup(self):
        self.manager.current = "sign_up_screen"
    
    def login(self , user , pswd):
        with open("users.json") as file:
            users  = json.load(file)
        if user in users and users[user] ['password'] == pswd:
            self.manager.current = "login_screen_cmplt"
        self.ids.wrong.text = "User id or Password is Wrong Try Again" 


class SignUpScreen(Screen):
    def add_user(self ,emal, uname , pswd):
       with open("users.json") as file:
           userz = json.load(file)
           self.manager.current = "sign_up_screen_cmplt"
           userz[uname] = { 'username':uname , 'email': emal, 'password': pswd,
           'Created At:': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}

           with open("users.json" , 'w') as file:
               json.dump(userz, file)


class SignUpScreenCmplt(Screen):
    def home(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"


class LoginScreenCmplt(Screen):
    def logout(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"
    def take_quote(self , feel): 
        feel = feel.lower()
        allfeelings = glob.glob("quotes/*txt")
        allfeelings = [Path(filename).stem for filename in allfeelings]
        
        if feel in allfeelings:
            with open(f"quotes/{feel}.txt", encoding="utf-8") as file:
                quotee = file.readlines()   
                self.ids.quotez.text = random.choice(quotee)
        else: 
            self.ids.quotez.text = "Currently Its not there please try another:)"


class ImageButton(ButtonBehavior,HoverBehavior,Image ):
    pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
