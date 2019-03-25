from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *


def myinit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60,1,1,30)
    gluLookAt(7,10,10,
              2,0,0,
              0,1,0)
    glClearColor(0,1,0,1)
    glClear(GL_COLOR_BUFFER_BIT)
#vertices
def xyz():

    glBegin(GL_LINES)
    glColor(1,0,0)
    glVertex(0,0,0)
    glVertex(10,0,0)
    glColor(0,1,0)
    glVertex(0,0,0)
    glVertex(0, 10, 0)
    glColor(0,0,1)
    glVertex(0,0,0)
    glVertex(0,0,10)
    glEnd()
#variales
angle=0
m=0
d=True

def draw():
    global m
    global angle
    global d
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
   # xyz()

#main blackroad
    glColor(0, 0, 0)
    glLoadIdentity()
    glRotate(90,1,0,0)
    glBegin(GL_POLYGON)
    glVertex(100, 5)
    glVertex(100, -8)
    glVertex(-100, -8)
    glVertex(-100, 5)
    glEnd()

#additions on road
    glColor(1, 1, 1)
    glLoadIdentity()
    glRotate(90, 1, 0, 0)
    glTranslate(0,3,0)
    glBegin(GL_POLYGON)
    glVertex(2, 0.5)
    glVertex(2, -0.5)
    glVertex(-2, -0.5)
    glVertex(-2, 0.5)
    glEnd()

    glColor(1, 1, 1)
    glLoadIdentity()
    glRotate(90, 1, 0, 0)
    glTranslate(-10, 3, 0)
    glBegin(GL_POLYGON)
    glVertex(3, 0.5)
    glVertex(3, -0.5)
    glVertex(-3, -0.5)
    glVertex(-3, 0.5)
    glEnd()

    glLoadIdentity()
    glRotate(90, 1, 0, 0)
    glTranslate(8, 3, 0)
    glBegin(GL_POLYGON)
    glVertex(2, 0.5)
    glVertex(2, -0.5)
    glVertex(-2, -0.5)
    glVertex(-2, 0.5)
    glEnd()

    glColor(1, 1, 1)
    glLoadIdentity()
    glRotate(90, 1, 0, 0)
    glTranslate(0, -3, 0)
    glBegin(GL_POLYGON)
    glVertex(2, 0.5)
    glVertex(2, -0.5)
    glVertex(-2, -0.5)
    glVertex(-2, 0.5)
    glEnd()

    glColor(1, 1, 1)
    glLoadIdentity()
    glRotate(90, 1, 0, 0)
    glTranslate(-10, -3, 0)
    glBegin(GL_POLYGON)
    glVertex(3, 0.5)
    glVertex(3, -0.5)
    glVertex(-3, -0.5)
    glVertex(-3, 0.5)
    glEnd()

    glLoadIdentity()
    glRotate(90, 1, 0, 0)
    glTranslate(8, -3, 0)
    glBegin(GL_POLYGON)
    glVertex(2, 0.5)
    glVertex(2, -0.5)
    glVertex(-2, -0.5)
    glVertex(-2, 0.5)
    glEnd()
#end of addtions


#the road spliter
    glLoadIdentity()
    glRotate(90,0,0,1)
    glColor(0.4, 0.4, 0.3)
    glTranslate(0, 0, 0)
    glScale(0.1, 10, 0.1)
    glutSolidCube(10)



#the wheels
    glColor(0.3,0.1,0.1)
    glLoadIdentity()
    glTranslate(m, 0, 2)
    glTranslate(5*0.5, -5*0.25*0.5, 5*0.5*0.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125,0.5,12,10)

    glColor(0.3,0.1,0.1)
    glLoadIdentity()
    glTranslate(m, 0, 2)
    glTranslate(5*0.5, -5*0.25*0.5, -5*0.5*0.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 12, 10)

    glColor(0.3,0.1,0.1)
    glLoadIdentity()
    glTranslate(m, 0, 2)
    glTranslate(-5*0.5, -5*0.25*0.5, -5*0.5*0.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 12, 10)

    glColor(0.3,0.1,0.1)
    glLoadIdentity()
    glTranslate(m, 0, 2)
    glTranslate(-5*0.5,-5*0.25*0.5, 5*0.5*0.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 12, 10)

    # the car
    glLoadIdentity()
    glColor(0, 0.2, 0.5)
    glTranslate(m, 0, 2)
    glScale(1, 0.25, 0.5)
    glutSolidCube(5)

    glLoadIdentity()
    glColor(0, 0.7, 0.7)
    glTranslate(m, 0, 2)
    # glRotate(45, 0, 1, 0)
    glTranslate(0, 5 * 0.25, 0)
    glScale(0.2, 0.09, 0.2)
    glutSolidSphere(7, 100, 100)

    glutSwapBuffers()

    if d:
        angle += 2
        m += 0.002
        if m >5:
            d=False
    else:
        angle -=2
        m -=0.002
        if m<-5:
            d=True





glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Moving Car ")
myinit()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()