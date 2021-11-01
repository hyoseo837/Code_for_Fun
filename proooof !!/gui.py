from kivy.app import App
from kivy.uix.button import Button

class testapp(App):
    def build(self):
        return Button(text = 'hello world')

testapp().run()