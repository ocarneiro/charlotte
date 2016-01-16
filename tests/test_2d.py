from charlotte import Canvas
from unittest import mock


def test_draw_line():
    mock_gl = mock.Mock()
    canvas = Canvas(gl=mock_gl)
    canvas.draw_line()
    assert len(canvas.objects) > 0


def test_label():
    mock_gl = mock.Mock()
    canvas = Canvas(gl=mock_gl)
    canvas.draw_label('Cool!')
    assert canvas.objects['Cool!']
