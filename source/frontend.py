# Front end of Pycrypt
import backend
from functools import partial

'''
python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
python -m pip install kivy.deps.gstreamer
'''
from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Welcome to Pycrypt Beta: "Enigma"')

TestApp().run()