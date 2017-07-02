#! /usr/bin/python3
from random import random
 
import pyglet
from pyglet.window import key, Window
from pyglet.gl import *
from pyglet.gl.glu import *


window = Window()


@window.event
def on_draw():
    pass # TODO: implement!

@window.event
def on_resize(width, height):
    glClearColor(0.0, 0.3, 0.0, 0.0)
    
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightf(GL_LIGHT0, GL_POSITION, 1, 5, 4)
    
    pass # TODO: implement!

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        update_frame(-1)
    elif symbol == key.RIGHT:
        update_frame(1)
 

if __name__=="__main__":
    pyglet.clock.schedule_interval(update_frame, 0.02)
    pyglet.app.run()
