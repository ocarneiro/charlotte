import pyglet

class Canvas(object):

    def __init__(self, gl=None):
        if not gl:
            self.gl = pyglet
        else:
            self.gl = gl
        self.gl.window.Window()


    def draw_line(self):
        pass
