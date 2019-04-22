# Front end of Pycrypt
import backend
import utilityfunc

########################################################################################################################

'''
DO THESE TO RUN THIS APPLICATION: 

python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
python -m pip install kivy.deps.gstreamer

python -m pip install pyperclip

'''

########################################################################################################################
# External Modules #
import pyperclip
import codecs
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window

from  kivy.uix.filechooser import FileChooserListView
from kivy.properties import StringProperty
import os
import time
import webbrowser
URL = 'github.com/Corruption13'
########################################################################################################################
Theme0 = (0.042, 0.0069, 0.1666, 1)
Theme1 = (0,0,0,0)
Theme2 = (0.0866, 0.042, 0.1169, 1)
Window.clearcolor = Theme1
class PycryptApp(App):


    ######################################################
    # Popup Function                                     #
    ######################################################

    def showpop(self, item, extra = ""):
        objf = backend.FileManager()
        if item == 1:
            Title = 'Please Enter Valid Key!'
            Text = 'Key must be:\n+Longer than 2 characters. \n+Less than infinity characters.'
        elif item == 2:
            Title = 'Please Enter length!'
            Text = 'Please Enter Length of Key to be generated!\nAccepted Range: 2 to Infinity'
        elif item == 3:
            Title = 'ERROR!'
            Text = extra

        box = BoxLayout(orientation = 'vertical', padding = (10))
        label = Label(text=Text, halign="justify", valign="center")
        btn1 = Button(text="Ok", size_hint=(0.1, 0.15), pos_hint={'x':0.45})
        box.add_widget(label)
        box.add_widget(btn1)

        pop = Popup(title=Title, title_align='left', title_color=(0.8, 0.2, 0.2, 1),
                    content=box, size_hint=(0.5, 0.5), background_color=(0.025, 0, 0, 0.9))
        btn1.bind(on_press=pop.dismiss)

        pop.open()


    ##########################################################
    # General Functions                                      #
    ##########################################################

    def currentscreen(self, Screen):
        self.current = Screen
    def changecolor(self, type):

        if type == 0:
            Window.clearcolor = Theme0
        elif type == 1:
            Window.clearcolor = Theme1

        elif type == 2:
            Window.clearcolor = Theme2
        else:
            pass

    def openfile(self, file):
        print("OPENING", file)
        try:
            os.startfile(file, 'open')
        except:
            MAIN.showpop(3, "File not specified/found!")
            print("Error!", file, "not found!")
    def _on_file_drop(self, window, file_path):
        obj = FChoose()
        print(file_path.decode("utf-8"))
        obj.getFile(file_path.decode("utf-8"), 1)

    def returnfilename(self, file):
        base = 0
        for i in range(len(file)):
            if file[i] == "\\" or file[i] == "/":
                base = i + 1

        text_variable_1 = file[base:]
        #print("HEY", file[base:])
        return text_variable_1
    def returnfoldername(self, file):
        base = 0
        for i in range(len(file)):
            if file[i] == "\\" or file[i] == "/":
                base = i - 1

        text_variable_1 = file[:base+1]
        #print("HEY", file[base:])
        return text_variable_1

    def build(self):
        self.current = 'MainScreen'
        self.input_path = os.getcwd()
        self.in_file = " "
        self.output_path = os.getcwd()
        self.out_file = " "
        self.key_file = ""
        self.key = ""
        self.mode = 1
        #Clock.max_iteration = 20
        Window.bind(on_dropfile=self._on_file_drop)
        return buildKV

MAIN = PycryptApp()


########################################################################################################################
# Text Based Interface #
########################

class Text(Screen):

    def __init__(self, **kwargs):
        super(Text, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 2)

    encr = ObjectProperty(None)
    decr = ObjectProperty(None)
    key = ObjectProperty(None)
    key_len = ObjectProperty(None)
    output_name= ObjectProperty(None)
    output_button = ObjectProperty(None)

########################################################################################################################

    class Button_Normal_Vert(Button):
        pass
    class Label_Container(Label):
        pass
    def test(self):
        print(MAIN.input_path)
########################################################################################################################

    def enc(self, mode=1):
        inputs = self.encr.text
        obj = backend.ED()
        obj2 = backend.FileManager()
       
        if len(self.key.text) > 2:
            obj.ed_mastermethod(input=inputs, key=self.key.text, mode="encrypt")
            if mode == 1:
                self.decr.text = obj.encrypt_string
            elif mode == 2:
                if self.output_name.text == "":
                    MAIN.out_file  = "Pycr_N.txt"
                else:
                    if "." in self.output_name.text:
                        MAIN.out_file = self.output_name.text
                    else:
                        MAIN.out_file = self.output_name.text + ".txt"

                obj2.write(obj.encrypt_string, MAIN.output_path + '\\' + MAIN.out_file)
                MAIN.openfile(MAIN.output_path + '\\' + MAIN.out_file)

                print("FILE")
            #self.encr.text = ""
        else:
            MAIN.showpop(1)


    def dec(self, mode=1):
        inputs = self.decr.text
        obj = backend.ED()
        obj2 = backend.FileManager()

        if len(self.key.text) > 2:
            obj.ed_mastermethod(input=inputs, key=self.key.text, mode="decrypt")
            if mode == 1:
                self.encr.text = obj.decrypt_string
            elif mode == 2:
                if self.output_name.text == "":
                    MAIN.out_file  = "Pycr_N.txt"
                else:
                    if "." in self.output_name.text:
                        MAIN.out_file = self.output_name.text
                    else:
                        MAIN.out_file = self.output_name.text + ".txt"

                obj2.write(obj.decrypt_string, MAIN.out_file)
                MAIN.openfile(MAIN.output_path + '\\' + MAIN.out_file)
            #self.decr.text = ""
        else:
            MAIN.showpop(1)

    def copy(self, text):
        pyperclip.copy(text)
    def enc_paste(self):
        self.encr.text = pyperclip.paste()
    def dec_paste(self):
        self.decr.text = pyperclip.paste()

    def key_show(self):
        if len(self.key.text) > 7:
            obj = backend.FileManager()
            file_name = "Pkey["+ str(len(self.key.text)) + "].txt"
            obj.write(self.key.text, file_name)
            MAIN.openfile(file_name)
            time.sleep(2)
            os.remove(file_name)

    def key_generator(self):
        if self.key_len.text != "" and self.key_len.text.isdigit():
            length = int(self.key_len.text)
            self.key.text = utilityfunc.key_gen(length)
        else:
            MAIN.showpop(2)
    def update(self, *args):
            self.output_button.text = MAIN.returnfilename(MAIN.out_file)


########################################################################################################################



class About(Screen):
    pass
class MainScreen(Screen):
    def about(self):
        webbrowser.open("http://github.com/Corruption13")
    pass

class File(Screen):
    #encr = ObjectProperty(None)
    #decr = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(File, self).__init__(**kwargs)
        self.output_file = ""
        self.random_name = ""
        Clock.schedule_interval(self.update, 2)


    button1 = ObjectProperty(None)      # Preview Input
    button2 = ObjectProperty(None)      # Preview Output
    key = ObjectProperty(TextInput)
    key_len = ObjectProperty(TextInput)
    key_name = ObjectProperty
    input_name = ObjectProperty(None)
    out_name = ObjectProperty(TextInput)
    out_text = ObjectProperty(TextInput)
    def test(self):
        print(MAIN.input_path)
    def enc(self, mode=2):
        obj1 = backend.ED()
        obj2 = backend.FileManager()
        f_object = backend.FileManager()
        file_name = self.out_name.text
        if file_name == "":
            file_name = "Pycrypt_" + MAIN.returnfilename(MAIN.in_file)

        try:
            metadata = f_object.read(MAIN.in_file)
        except:
            MAIN.showpop(3, "Error")
        print("Encrypting", MAIN.in_file)
        if len(self.key.text) > 2:
            obj1.ed_mastermethod(input=metadata, key=self.key.text, mode="encrypt")
            if mode == 1:
                print(obj1.encrypt_string)
            elif mode == 2:
                if "." not in file_name:
                    file_name = file_name + ".txt"
                MAIN.out_file = file_name
                self.out_text.text = obj1.encrypt_string
                obj2.write(obj1.encrypt_string, MAIN.output_path + '\\' + file_name)
        else:
            MAIN.showpop(1)



    def dec(self, mode=2):
        obj1 = backend.ED()
        obj2 = backend.FileManager()
        f_object = backend.FileManager()
        file_name = self.out_name.text[:-1]
        if file_name == "":
            file_name = "Pycrypt_" + MAIN.returnfilename(MAIN.in_file)
        metadata = f_object.read(MAIN.in_file)
        if len(self.key.text) > 2:
            obj1.ed_mastermethod(input=metadata, key=self.key.text, mode="decrypt")
            if mode == 1:
                print(obj1.decrypt_string)
            elif mode == 2:
                if "." not in file_name:
                    file_name = self.out_name.text + ".txt"
                MAIN.out_file = file_name
                self.out_text = obj1.decrypt_string
                obj2.write(obj1.decrypt_string, MAIN.output_path + '\\' + file_name)



    def key_show(self):
        if len(self.key.text) > 7:
            obj = backend.FileManager()
            file_name = "Pkey["+ str(len(self.key.text)) + "].txt"
            obj.write(self.key.text, file_name)
            self.openfile(file_name)
            time.sleep(2)
            os.remove(file_name)



    def key_generator(self, mode=1):
        if self.key_len.text.isdigit() and int(self.key_len.text) >= 3:
            length = int(self.key_len.text)
            self.key.text = utilityfunc.key_gen(length)
            if mode!=1:
                try:
                    if os.path.exists(MAIN.output_path + '\\' + self.random_name):
                        os.remove(MAIN.output_path + '\\' + self.random_name)
                    else:
                        print("The file does not exist")
                except:
                    print("!")
                if self.key_name.text == "":
                    self.random_name =  MAIN.in_file +"_" + self.key.text[:3] + ".pkey"
                else:
                    self.random_name = self.key_name.text + ".pkey"
                try:
                    file = codecs.open(MAIN.output_path + '\\' + self.random_name, 'w', "UTF-8")
                    file.write(self.key.text)
                    file.close()
                except:
                    print("Woops!")

        else:
            MAIN.showpop(2)
    pass
    def update(self, *args):
            obj = backend.FileManager()
            self.button1.text = MAIN.returnfilename(MAIN.in_file)
            self.button2.text = MAIN.returnfilename(MAIN.out_file)

            if MAIN.key_file!="":
                self.key.text = obj.read(MAIN.key_file)


class FChoose(Screen):

    def scriptpath(self):
        return os.getcwd()

    def getFile(self, _file, mode=1):
        path = _file
        path = "".join(path)
        print("File:", path)
        if mode == 1:
            MAIN.in_file = path
        elif mode == 2:
            MAIN.output_path = MAIN.returnfoldername(path)
        elif mode ==3:
            MAIN.key_file = path


        #os.startfile(input_path, 'open')


    def getFolder(self, Folder, mode=1):
        path = Folder
        print("Folder:", path)
        if mode == 1:
            MAIN.input_path = path
        elif mode == 2:
            MAIN.output_path = path


        # os.startfile(input_path, 'open')






buildKV = Builder.load_file("pycrypt.kv")


if __name__=='__main__':
    MAIN.run()