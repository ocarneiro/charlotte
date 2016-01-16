from charlotte import Canvas
from unittest import mock


def test_window_created():
    mockwindow = mock.MagicMock()
    dummy = mock.Mock()
    dummy.window = mock.Mock()
    dummy.window.Window = mockwindow
    canvas = Canvas(gl=dummy)
    assert mockwindow.called
