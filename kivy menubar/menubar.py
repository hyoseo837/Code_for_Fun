from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Line, Ellipse

current_color = (1,0,0)

class menubarLayout(BoxLayout):
    def clear_canvas(self):
        self.children[1].canvas.clear()

class menuTab(BoxLayout):
    pass

class function_button(Button):
    pass

class clr_btn(Button):
    def on_release(self):
        self.parent.clear_canvas()

class paper(Widget):
    
    def on_touch_down(self, touch):
        with self.canvas:
            Color(*current_color)
            touch.ud['line'] = Line(points=(touch.x,touch.y),width=2)
    
    def on_touch_move(self, touch):
        if touch.y > 65 and touch.y < self.parent.size[1]-50:
                touch.ud['line'].points += [touch.x,touch.y]
        else:
            touch.ud['line'] = Line(points=(touch.x,touch.y),width=2)



class menubarApp(App):
    def build(self):
        menus = menuTab(orientation='horizontal',size_hint_y=None,size = (50,50))
        menus.add_widget(function_button(text='fnc1'))
        menus.add_widget(function_button(text='fnc2'))
        menus.add_widget(function_button(text='fnc3'))

        menulayer = menubarLayout(orientation='vertical')
        menulayer.add_widget(menus)
        menulayer.add_widget(paper())
        menulayer.add_widget(clr_btn(text='clear',size_hint_y=None,size = (65,65)))
        
        return menulayer

        
if __name__ == '__main__':
    menubarApp().run()