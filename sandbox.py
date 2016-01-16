import pyglet

class Canvas(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        super(Canvas, self).__init__(800,600)
        self.app = pyglet.app
        self.label = pyglet.text.Label(text="Awesome!")

    def on_draw(self):
        self.label.draw()

if __name__ == '__main__':
    canvas = Canvas()
    canvas.app.run()
