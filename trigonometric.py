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
    ctx.x+=ctx.step
    #sine curve
    ctx.y =  sinx(ctx.x)
    #color
    ctx.instr[0].r = randrange(0, 254, 1)
    ctx.instr[0].g = random()
    ctx.instr[0].b = random()
    #line
    ctx.instr[1].points += (ctx.scaleX* ctx.x+ctx.offsetX, ctx.scaleY * ctx.y+ctx.offsetY)
    #ctx.instr[1].points +=(10,0)
    #ellipse
    ctx.instr[2].pos = (ctx.scaleX* ctx.x+ctx.offsetX, ctx.scaleY * ctx.y+ctx.offsetY)
    
       
    




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
       
        self.ctx.instr = []
        self.ctx.x = 0.0
        self.ctx.y = 0.0
        self.ctx.step = 0.01
        self.ctx.scaleX = 300
        self.ctx.scaleY = 100
        self.ctx.offsetX = -10
        self.ctx.offsetY = 200
         #instructions
        with self.canvas:
            
            c = (random(), random(), random())
            self.ctx.color = Color(*c)
            d =15
            m = 64
            for x in xrange(64):
                #instruction set for chart
                
                self.ctx.instr.append(Color(*c))                
                self.ctx.instr.append(Line(points=(0,0),dash_length=0.1,pointsize=100))
                self.ctx.instr.append(Ellipse(pos=(-100, -100 ), size=(d, d)))
                
        Clock.schedule_interval(self.translate, 1 / 60.)
        Clock.schedule_interval(partial(update_chart, self.ctx), 1 / 60.)


class VisualizationApp(App):
    def build(self):
        graph = VisualizationWidget()
        
        return graph


if __name__ == '__main__':
    VisualizationApp().run()
