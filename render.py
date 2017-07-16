#! /usr/bin/python3
from random import random
 
import pyglet
from pyglet.window import key, Window
from pyglet.gl import *
from pyglet.gl.glu import *


window = Window()


def update_frame(dt):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    pass # TODO: implement!

@window.event
def on_draw():
    update_frame(0)

@window.event
def on_resize(width, height):
    glClearColor(0.0, 0.3, 0.0, 0.0) # set the background color
    
    glEnable(GL_DEPTH_TEST) # enable depth buffer
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightf(GL_LIGHT0, GL_POSITION, 1, 5, 4) # put one light
    
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, width / height, .1, 1000) # perspective projection angle 45 degrees
    gluLookAt( # set the camera and aim it at the center of the scene
     1, 4, 15, # eye
     0, 0, 0, # target
     0, 1, 0  # up
    )
    glMatrixMode(GL_MODELVIEW) 
    return pyglet.event.EVENT_HANDLED

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        update_frame(-1)
    elif symbol == key.RIGHT:
        update_frame(1)


if __name__=="__main__":
    pyglet.clock.schedule_interval(update_frame, 0.02)
    pyglet.app.run()
