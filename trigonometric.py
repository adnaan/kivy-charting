from random import random, randrange
from kivy.app import App
from kivy.graphics import Color, Ellipse, Line, Rectangle, Color, Translate
from kivy.uix.scatter import Scatter
from kivy.clock import Clock
from kivy.graphics.transformation import Matrix
from functools import partial
import math




def sinx(x):
    return 2*math.sin(2*3.14*(x-1/4))
    
def update_chart(ctx, *largs):
    
    #update instruction set by index
    #to-do, update by instruction name.
    ctx.x+=0.01
    #sine curve
    ctx.y =  sinx(ctx.x)
    ctx.statsr[0].r = randrange(0, 254, 1)
    ctx.statsr[0].g = random()
    ctx.statsr[0].b = random()
    ctx.statsr[1].points += (300* ctx.x-10, 100 * ctx.y+200)
    #ctx.statsr[1].points +=(10,0)
    ctx.statsr[2].pos = (300* ctx.x-10, 100 * ctx.y+200)
       
    




class VisualContext:
    
    def __init__(self):
        self.config = {}

class VisualizationWidget(Scatter):
    def __init__(self, **kwargs):
        super(VisualizationWidget, self).__init__(**kwargs) 
        Clock.schedule_once(self.create_chart)
        self.ctx = VisualContext()
        

    def translate(self, instance):
       
        self.apply_transform(Matrix().translate(-1, 0, 0))
 
    def create_chart(self, *largs):
    	    
        #chart properties
        self.ctx.inputstats = 0
        self.ctx.stats = []
        self.ctx.statsr = []
        self.ctx.x = 0.0
        self.ctx.y = 0.0
         
        with self.canvas:
            
            c = (random(), random(), random())
            self.ctx.color = Color(*c)
            d =15
            m = 64
            for x in xrange(64):
                #instruction set for chart
                self.ctx.stats.append(0)
                self.ctx.statsr.append(Color(*c))                
                self.ctx.statsr.append(Line(points=(0,0),dash_length=0.1,pointsize=100))
                self.ctx.statsr.append(Ellipse(pos=(-100, -100 ), size=(d, d)))
                
        Clock.schedule_interval(self.translate, 1 / 60.)
        Clock.schedule_interval(partial(update_chart, self.ctx), 1 / 60.)


class VisualizationApp(App):
    def build(self):
        graph = VisualizationWidget()
        
        return graph


if __name__ == '__main__':
    VisualizationApp().run()
