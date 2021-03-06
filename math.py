from random import random, randrange
from kivy.app import App
from kivy.graphics import Color, Ellipse, Line, Rectangle, Color, Translate

from kivy.uix.scatter import Scatter
from kivy.clock import Clock
from kivy.graphics.transformation import Matrix
from functools import partial
from math import*
from kivy.uix.stencilview import StencilView
'''
This script is intended to be standalone. To change curve, in update_chart()
change, e.g:
ctx.y = sinx(x)
To set scale and offset for fitting the wave to the screen, look into create_chart()

'''


def sinx(x):
    return 2*sin(2*3.142*(x-1.0/4))
def cosx(x):
    return 2*sin(3.142*(2-x))
def tanx(x):
    return (sinx(x)/cosx(x))
def cotx(x):
    return (1.0/tanx(x))
def secx(x):
    return (1.0/cosx(x))
def cosecx(x):
    return (1.0/sinx(x))
def logx(x):
    return log10(x)
    
def update_chart(ctx, *largs):
    
    #update instruction set by index
    #to-do, update by instruction name.
    #step x value
    #if ctx.x < 2:
    	#ctx.x+=ctx.step
    #else:
    	#ctx.x = 0.0
    #change the curve function
    ctx.x+=ctx.step
    ctx.y = cotx(ctx.x)

    #color
    ctx.instr[0].rgb = (randrange(0, 254, 1),0, 0)
    
    #line
    pointX = ctx.scaleX * ctx.x + ctx.offsetX
    pointY = ctx.scaleY * ctx.y + ctx.offsetY
    
    ctx.instr[1].points += (pointX, pointY )
    #ctx.instr[1].points +=(10,0)
    
    #ellipse
    ctx.instr[2].pos = (ctx.scaleX* ctx.x+ctx.offsetX, ctx.scaleY * ctx.y+ctx.offsetY)
    
       
    




class VisualContext:
    
    def __init__(self):
        self.config = {}

class VisualizationWidget(StencilView,Scatter):
    def __init__(self, **kwargs):
       
        super(VisualizationWidget, self).__init__(**kwargs)
        
         
        Clock.schedule_once(self.create_chart)
        self.ctx = VisualContext()
        

    def translate(self, instance):
       
        self.apply_transform(Matrix().translate(1, 0, 0))
 
    def create_chart(self, *largs):
    	    
        #chart properties
       
        self.ctx.instr = []
        self.ctx.x = 0.0
        self.ctx.y = 0.0
        self.ctx.step = 0.01
        print self.width
        self.ctx.width = self.width
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
        
        #to use translation remove StencilView, better way to do this.        
        #Clock.schedule_interval(self.translate, 1 / 60.)
        Clock.schedule_interval(partial(update_chart, self.ctx), 1 / 60.)


class VisualizationApp(App):
    def build(self):
        graph = VisualizationWidget(pos=(100,0),size_hint=(None,None),size=(800,600))
        
        return graph


if __name__ == '__main__':
    VisualizationApp().run()
