# pylint: disable=no-name-in-module
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, QRect
from PyQt6.QtWidgets import QGraphicsOpacityEffect


def animate_expansion(widget, duration=500):
    """
    Expande el widget verticalmente (animando su altura) sobre la duración especificada.

     Args:
     - widget: El widget para animar.
     - duration: La duración de la animación en milisegundos (el valor predeterminado es de 500 ms).
    """
    animation = QPropertyAnimation(widget, b"geometry")
    animation.setDuration(duration)
    animation.setStartValue(QRect(widget.x(), widget.y(), widget.width(), 0))
    animation.setEndValue(QRect(widget.x(), widget.y(), widget.width(), 200))
    animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
    animation.start()


def fade_in(widget, duration=500):
    """
    Se desvanece en el widget al aumentar gradualmente su opacidad.

    Args:
    - widget: El widget para desvanecerse.
    - duration: La duración del efecto de desvanecimiento en milisegundos (el valor predeterminado es de 500 ms).
    """
    effect = QGraphicsOpacityEffect(widget)
    widget.setGraphicsEffect(effect)

    animation = QPropertyAnimation(effect, b"opacity")
    animation.setDuration(duration)
    animation.setStartValue(0)
    animation.setEndValue(1)
    animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
    animation.start()
