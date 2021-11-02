from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label

class menutab(BoxLayout):
    pass

class menubarApp(App):
    def build(self):
        menulayer = menutab()
        # return Button(text='hello',size_hint_y=None,size=(1,50),pos_hint={'top': 1})
        return menulayer
if __name__ == '__main__':
    menubarApp().run()