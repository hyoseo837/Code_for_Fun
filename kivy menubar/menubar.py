from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Line, Ellipse


class menubarLayout(BoxLayout):
    color = (0,0,0)
    def clear_canvas(self):
        self.children[1].canvas.clear()

class menuTab(BoxLayout):
    def clear_brush (self):
        for i in self.children:
            i.background_color = 'grey'

class function_button(Button):
    def __init__(self,**kwargs):
        if 'brush_color' in kwargs:
            self.background_color = kwargs['brush_color']
            self.brush_color = kwargs['brush_color']
            kwargs.pop('brush_color')
        super().__init__(**kwargs)

    def on_release(self):
        self.parent.parent.color = self.brush_color
        self.parent.clear_brush()

class clr_btn(Button):
    def on_release(self):
        self.parent.clear_canvas()

class paper(Widget):
    
    def on_touch_down(self, touch):
        with self.canvas:
            Color(*self.parent.color)
            touch.ud['line'] = Line(points=(touch.x,touch.y),width=2)
    
    def on_touch_move(self, touch):
        if touch.y > 65 and touch.y < self.parent.size[1]-50:
                touch.ud['line'].points += [touch.x,touch.y]



class menubarApp(App):
    def build(self):
        menus = menuTab(orientation='horizontal',size_hint_y=None,size = (50,50))
        menus.add_widget(function_button(text='Black',brush_color=(0,0,0)))
        menus.add_widget(function_button(text='Red',brush_color=(1,0,0)))
        menus.add_widget(function_button(text='Green',brush_color=(0,1,0)))
        menus.add_widget(function_button(text='Blue',brush_color=(0,0,1)))
        menus.add_widget(function_button(text='Cyan',brush_color=(0,1,1)))
        menus.add_widget(function_button(text='Yellow',brush_color=(1,1,0)))
        menus.add_widget(function_button(text='Magenta',brush_color=(1,0,1)))
        menus.add_widget(function_button(text='Eraser',brush_color=(1,1,1)))

        menulayer = menubarLayout(orientation='vertical')
        menulayer.add_widget(menus)
        menulayer.add_widget(paper())
        menulayer.add_widget(clr_btn(text='clear',size_hint_y=None,size = (65,65)))
        
        return menulayer

        
if __name__ == '__main__':
    menubarApp().run()