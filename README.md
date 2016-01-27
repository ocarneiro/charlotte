# charlotte
##That little (rather buggy) thing that tells pyglet around

[Pyglet](http://www.pyglet.org) is an awesome library for working with OpenGL in Python. It's extremely powerful, but not easy to learn.

Like in Charlotte's Web (the movie), I thought this little piggy needed something to tell it what to do. Hence, [charlotte](https://github.com/ocarneiro/charlotte). 

Hopefully, charlotte will make it possible to draw 2D or 3D stuff with simple commands such as:

```python
import charlotte
canvas = charlotte.Canvas(800,600)
canvas.draw_cube()
canvas.draw_line(orientation='horizontal')
```

My challenge now is to make it run interactively. Maybe I should run pyglet.app.run() in a thread.
