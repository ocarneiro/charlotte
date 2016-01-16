from charlotte import Canvas
from unittest import mock

def test_draw_line():
    canvas = mock.Mock(Canvas())
    canvas.draw_line()
