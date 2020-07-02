#Import the kivy's classes and more
import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from database import Database

kivy.require("1.11.1")

username = ""
psd = ""

class LoginScreen(Screen):
    un = ObjectProperty(None)
    psd = ObjectProperty(None)

    def validate(self):
        global username, psd
        username = self.un.text
        psd = self.psd.text
        status = db.__validate__(username, psd)
        if status:
            sm.current = "info"
            InfoScreen().show_data()
        else:
            show_error("You aren't register in our database")

    def __signup_screen__(self):
        username = self.un.text
        psd = self.psd.text
        sm.current = "sign_up"



class SignupScreen(Screen):
    namee = ObjectProperty(None)
    lastname = ObjectProperty(None)
    age = ObjectProperty(None)
    birth_date = ObjectProperty(None)
    country = ObjectProperty(None)
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def __init__(self, **kw):
        super(SignupScreen, self).__init__(**kw)
    #Make a function to see Popup with status
    #and go to login

    def __submit__(self):
        data = [
            (str(self.namee.text), str(self.lastname.text), str(self.age.text),\
            str(self.birth_date.text), str(self.country.text,), str(self.username.text),\
                str(self.password.text),"20/8/2001")
        ]
        try:
            db.__create__()
            db.__add_person__(data)
            status = True
        except Exception as e:
            status = False
            show_error(e)
        finally:
            if status:
                show_done("Your data has saven succesfuly!")
                sm.curent = "login"
            else:
                show_error("Please contact me to: djose1164@gmail.com")
        

    def __go_login__(self):
        sm.current = "login"

    def __quit__(self):
        '''
            I'm working in this.
        '''
        pass

class InfoScreen(Screen):
    lbl_id = ObjectProperty(None)
    lbl_name = ObjectProperty(None)
    lbl_lastname = ObjectProperty(None)
    lbl_age = ObjectProperty(None)
    lbl_birth_date = ObjectProperty(None)
    lbl_country = ObjectProperty(None)
    lbl_username = ObjectProperty(None)
    lbl_password = ObjectProperty(None)
    lbl_date = ObjectProperty(None)

    def __init__(self, **kw):
        super(InfoScreen, self).__init__(**kw)
        self.show_data()

    def show_data(self):
        global username, psd
        data = db.__load_data__(username, psd)
        for q, w, e, r, t, y, u, i, o in data:
            self.lbl_id.text = str(q)
            self.lbl_name.text = w
            self.lbl_lastname.text = str(r)
            self.lbl_age.text = str(t)
            self.lbl_birth_date.text = str(y)
            self.lbl_country.text = str(e)
            self.lbl_username.text = str(u)
            self.lbl_password.text = str(i)
            self.lbl_date.text = str(o)
            

    def __go_login__(self):
        sm.current = "login"

class _ScreenManager(ScreenManager):
    pass

kv = Builder.load_file("Login_GUI.kv")

def show_error(error):
    error = str(error)
    pp = Popup(content=Label(text=error), size_hint=(.6, .3), title = "Error!")
    pp.open()

def show_done(msg):
    msg = str(msg)
    pp = Popup(content=Label(text=msg), size_hint=(.5, .3), title="Done!")
    pp.open()

db = Database()

sm = _ScreenManager()

screens = [LoginScreen(name = "login"), SignupScreen(name = "sign_up"), InfoScreen(name = "info")]

for screen in screens:
    sm.add_widget(screen)
    print(screen)

sm.current = "login"

class MainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MainApp().run()