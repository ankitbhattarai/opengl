from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.raw.GLU import gluOrtho2D

def draw_line(x1, y1, x2, y2):
  glBegin(GL_LINES)
  glVertex2f(x1, y1)
  glVertex2f(x2, y2)
  glEnd()

def display():
  glClear(GL_COLOR_BUFFER_BIT)
  glColor3f(1.0, 1.0, 1.0) # Set color to white
  draw_line(100, 100, 300, 300)
  glFlush()

def main():
  glutInit()
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutInitWindowSize(400, 400)
  glutCreateWindow(b"Drawing Lines")
  glClearColor(0.0, 0.0, 0.0, 1.0)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluOrtho2D(0, 400, 0, 400)
  glutDisplayFunc(display)
  glutMainLoop()

if __name__ == "__main__":
  main()