import pyglet
import time

class Canvas(object):

    def __init__(self, gl=None):
        if not gl:
            self.gl = pyglet
        else:
            self.gl = gl
        self.window = self.gl.window.Window()
        self.app = self.gl.app
        """ objects = everything that needs to be drawn """
        self.objects = {}
        self.setup_window()


    def draw_line(self, name='Line'):
        line = 1  # TODO replace with actual line
        self.objects[name] = line


    def draw_label(self, text):
        label = self.gl.text.Label(text)
        self.objects[text] = label


    def on_draw(self):
        for o in self.objects.values():
            o.draw()


    def setup_window(self):
        self.window.on_draw = self.on_draw
        # TODO run self.app.run() in a thread to allow interactivity


if __name__ == '__main__':
    canvas = Canvas()
    canvas.draw_label('opa')
    #time.sleep(5)
    canvas.app.run()
