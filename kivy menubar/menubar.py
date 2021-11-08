from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Line, Ellipse


class menubarLayout(BoxLayout):
    def clear_canvas(self):
        self.children[1].canvas.clear()

class menuTab(BoxLayout):
    current_color = [0,0,0]
    current_brush_size = 2 

######################################################################################
class brush_size_menu(BoxLayout):
    pass

class brush_size_button(Button):
    def on_release(self):
        if self.text == '+':
            self.parent.parent.current_brush_size += 1
        elif self.text == '-' and self.parent.parent.current_brush_size >= 1.5:
            self.parent.parent.current_brush_size -= 1

######################################################################################
class color_menu(GridLayout):
    def clear_brush (self):
        for i in self.children:
            i.background_color = i.brush_color

class color_button(Button):
    def __init__(self,**kwargs):
        if 'brush_color' in kwargs:
            self.background_color = kwargs['brush_color']
            self.brush_color = kwargs['brush_color']
            kwargs.pop('brush_color')
            self.background_normal = ''
            self.background_color = self.brush_color
        super().__init__(**kwargs)

    def on_release(self):
        self.parent.parent.current_color = self.brush_color
        self.parent.clear_brush()
        self.background_color = ((self.brush_color[0]-0.2, self.brush_color[1]-0.2, self.brush_color[2]-0.2))

class clr_btn(Button):
    def on_release(self):
        self.parent.clear_canvas()

######################################################################################
class color_rgb_menu(BoxLayout):
    pass

class color_rgb_part(BoxLayout):
    def __init__(self,**kwargs):
        if 'color_id' in kwargs:
            self.color_id = kwargs['color_id']
            kwargs.pop('color_id')
        super().__init__(**kwargs)

class color_rgb_button(Button):

    def on_press(self):
        mother = self.parent.parent.parent.current_color
        if self.parent.color_id == (1,0,0):
            if self.text == '+':
                mother[0] += 0.05
            elif self.text == '-':
                mother[0] -= 0.05
            if mother[0] > 1:
                mother[0] = 1
            if mother[0] < 0:
                mother[0] = 0

        if self.parent.color_id == (0,1,0):
            if self.text == '+':
                mother[1] += 0.05
            elif self.text == '-':
                mother[1] -= 0.05
            if mother[1] > 1:
                mother[1] = 1
            if mother[1] < 0:
                mother[1] = 0

        if self.parent.color_id == (0,0,1):
            if self.text == '+':
                mother[2] += 0.05
            elif self.text == '-':
                mother[2] -= 0.05
            if mother[2] > 1:
                mother[2] = 1
            if mother[2] < 0:
                mother[2] = 0

######################################################################################
class paper(Widget):
    def on_touch_down(self, touch):
        color_function = self.parent.children[-1]
        size_function = self.parent.children[-1]
        with self.canvas:
            Color(*color_function.current_color)
            touch.ud['line'] = Line(points=(touch.x,touch.y),width=size_function.current_brush_size)
    
    def on_touch_move(self, touch):
        if touch.y > 65 and touch.y < self.parent.size[1]-60:
                touch.ud['line'].points += [touch.x,touch.y]

######################################################################################
class menubarApp(App):
    def build(self):
        # color_section = color_menu(rows=3, size_hint_x=None, size=(100,60))
        # color_section.add_widget(color_button(text='',brush_color=(0,0,0)))
        # color_section.add_widget(color_button(text='',brush_color=(1,0,0)))
        # color_section.add_widget(color_button(text='',brush_color=(0,1,0)))
        # color_section.add_widget(color_button(text='',brush_color=(0,0,1)))
        # color_section.add_widget(color_button(text='',brush_color=(0,1,1)))
        # color_section.add_widget(color_button(text='',brush_color=(1,1,0)))
        # color_section.add_widget(color_button(text='',brush_color=(1,0,1)))
        # color_section.add_widget(color_button(text='',brush_color=(1,1,1)))
        
        color_rgb_red = color_rgb_part(orientation = 'vertical',size_hint_x = None, size=(40,60),color_id=(1,0,0))
        color_rgb_red.add_widget(color_rgb_button(text='+'))
        color_rgb_red.add_widget(color_rgb_button(text='-'))
        color_rgb_green = color_rgb_part(orientation = 'vertical',size_hint_x = None, size=(40,60),color_id=(0,1,0))
        color_rgb_green.add_widget(color_rgb_button(text='+'))
        color_rgb_green.add_widget(color_rgb_button(text='-'))
        color_rgb_blue = color_rgb_part(orientation = 'vertical',size_hint_x = None, size=(40,60),color_id=(0,0,1))
        color_rgb_blue.add_widget(color_rgb_button(text='+'))
        color_rgb_blue.add_widget(color_rgb_button(text='-'))

        color_rgb_section = color_rgb_menu(orientation = 'horizontal', size_hint_x=None, size=(120,60))
        color_rgb_section.add_widget(color_rgb_red)
        color_rgb_section.add_widget(color_rgb_green)
        color_rgb_section.add_widget(color_rgb_blue)

        brush_size_section = brush_size_menu(orientation = 'vertical',size_hint_x=None,size=(30,60))
        brush_size_section.add_widget(brush_size_button(text='+',pos_hint={'top':1}))
        brush_size_section.add_widget(brush_size_button(text='-',pos_hint={'top':0}))

        menus = menuTab(orientation='horizontal',size_hint_y=None,size = (40,60))
        # menus.add_widget(color_section)
        menus.add_widget(color_rgb_section)
        menus.add_widget(brush_size_section)

        menulayer = menubarLayout(orientation='vertical',spacing=(30,10))
        menulayer.add_widget(menus)
        menulayer.add_widget(paper())
        menulayer.add_widget(clr_btn(text='clear',size_hint_y=None,size = (65,65)))
        
        return menulayer

        
if __name__ == '__main__':
    menubarApp().run()