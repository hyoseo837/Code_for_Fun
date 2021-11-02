from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Color,Ellipse,Line


class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            Color(1,0,0)
            d = 40.
            Ellipse(pos=(touch.x-d/2,touch.y-d/2),size=(d,d))
            Color(1,1,0)
            touch.ud['line'] = Line(points=(touch.x,touch.y),width=2)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x,touch.y]

class MyPaintApp(App):
    def build(self):
        parent = Widget()
        self.painter = MyPaintWidget()
        clearbtn = Label(text='clear',pos=(100,100))
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)

        return parent
    
    def clear_canvas(self,obj):
        self.painter.canvas.clear()


if __name__ == '__main__':
    MyPaintApp().run()
