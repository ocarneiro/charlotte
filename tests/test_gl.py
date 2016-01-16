from charlotte import Canvas
from unittest import mock


def test_window_created():
    mockwindow = mock.MagicMock()
    dummy = mock.Mock()
    dummy.window.Window = mockwindow
    canvas = Canvas(gl=dummy)
    assert mockwindow.called


def test_draws_object():
    dummy = mock.Mock()
    canvas = Canvas(gl=dummy)
    label = mock.Mock()
    label.draw = mock.MagicMock()
    canvas.objects['label'] = label
    canvas.window.on_draw()
    assert label.draw.called
