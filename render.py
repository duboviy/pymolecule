#! /usr/bin/python3
from random import random
 
import pyglet
from pyglet.window import key, Window
from pyglet.gl import *
from pyglet.gl.glu import *


window = Window()


class Molecule(object):
    def __init__(self, atoms):
        self.atoms = atoms
 
    @classmethod
    def import_from_file(self, fn):
        """ An alternative constructor to instantiate molecule from text file. """
        atoms = []
        with open(fn) as f:
            for l in f:
                el, x, y, z = l.split()
                self.atoms.append(
                    (el, float(x), float(y), float(z))
                )
         return cls(atoms)
 
    def draw(self):
        for atom in self.atoms:
            glPushMatrix() # save model matrix
            glTranslatef(*atom[1:]) # shift the matrix of the model to the atom coordinates
            # draw the sphere of radius 1 and the color of the corresponding atom type
            draw_sphere(1, palette.get_color(atom[0]))
            glPopMatrix() # load the saved matrix of the model
 
 
molecule = Molecule.import_from_file('glucose.dat')
 
 
def draw_sphere(radius, color):
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
     
    # set matrerial color
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, (GLfloat * 3)(*color))
    glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION,
        (GLfloat * 3)(*map(lambda x: x/2, color))
    )
    # glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (GLfloat * 3)(*color))
 
    sphere = gluNewQuadric()
    gluSphere(sphere, radius, 50, 50) # 50, 50 - amount of meridians and parallels
    # if you need more atoms - reduce their amount to increase performance
    

def update_frame(dt):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity() # load identity matrix
   
    # TODO: implement rotation logic without global vars
    global rotation
    rotation += dt * 10 # more time - bigger rotation
    glRotatef(rotation, 0, 1, 0) # around y axis
    molecule.draw()

    
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
