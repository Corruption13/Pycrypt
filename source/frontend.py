# Front end of Pycrypt
import backend
import utilityfunc
import pyperclip


'''
python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
python -m pip install kivy.deps.gstreamer
'''
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.popup import Popup


Window.clearcolor = (0.042, 0.0069, 0.0666, 1)


class Front(Widget):
    key_fail = Popup(title='Please Enter Valid Key!',
                     content=Label(text='Key must be:\n+Longer than 2 characters. \n+Less than infinity characters.'),
                     size_hint=(None, None), size=(400, 400))
    key_len_fail = Popup(title='Please Enter length!',
                     content=Label(text='Please Enter Length of Key to be generated!'),
                     size_hint=(None, None), size=(400, 400))
    #class Touch(Widget):
        #pass
    btn = ObjectProperty(None)

    #def on_touch_down(self, touch):
        #print("Mouse Down", touch)


    #def on_touch_move(self, touch):
        #print("Mouse Move", touch)

    #def on_touch_up(self, touch):
        #print("Mouse UP", touch)


    class Button_Normal_Vert(Button):
        pass


    encr = ObjectProperty(None)
    decr = ObjectProperty(None)
    key = ObjectProperty(None)
    key_len = ObjectProperty(None)

    '''
    def __init__(self, **kwargs):
        super(LoginApp, self).__init__(**kwargs)
        self.textfield = GridLayout()
        self.textfield.cols = 2
        self.cols = 1
        self.textfield.input = TextInput()
        self.textfield.output = TextInput()
        self.textfield.add_widget(self.textfield.input)
        self.textfield.add_widget(self.textfield.output)
        self.button = Button(text="Encrypt!")
        self.button.bind(on_press=self.enc)

        self.text = Label(text="Please input the details below:")
        self.Login = Label(text="Login iD:")
        self.Login_Text = TextInput(multiline=False)
        #self.add_widget(self.text)
        #self.add_widget(self.Login, index=3)
        #self.add_widget(self.Login_Text, index=4)
        self.add_widget(self.textfield)
        self.add_widget(self.button)

    '''
    def print(self):
        print("Check!!!!!!!!!!!!")

    def enc(self):
        inputs = self.encr.text
        obj = backend.ED()
        if len(self.key.text) > 2:
            obj.ed_mastermethod(input=inputs, key=self.key.text, mode="encrypt")
            self.decr.text = obj.encrypt_string
            self.encr.text = ""
        else:
            self.key_fail.open()


    def dec(self):
        inputs = self.decr.text
        obj = backend.ED()
        if len(self.key.text) > 2:
            obj.ed_mastermethod(input=inputs, key=self.key.text, mode="decrypt")
            self.encr.text = obj.decrypt_string
            self.decr.text = ""
        else:
            self.key_fail.open()

    def copy(self, text):
        pyperclip.copy(text)
    def enc_paste(self):
        self.encr.text = pyperclip.paste()
    def dec_paste(self):
        self.decr.text = pyperclip.paste()

    def key_generator(self):
        if self.key_len.text != "" and self.key_len.text.isdigit():
            length = int(self.key_len.text)
            self.key.text = utilityfunc.key_gen(length)
        else:
            self.key_len_fail.open()

class PycryptPrototypeApp(App):
    def build(self):
        return Front()

PycryptPrototypeApp().run()