from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QGraphicsTextItem
from PyQt5.QtGui import QColor, QBrush, QPainter, QFont
from PyQt5.QtCore import Qt
from piezas import Pieces
import sys

SQUARE_SIZE = 80
LIGHT_COLOR = QColor(220, 118, 51)
DARK_COLOR = QColor(110, 44, 0)
LABEL_FONT = QFont("Arial", 20, QFont.Bold)
LETTERS = 'abcdefgh'
NUMBERS = '87654321'


class SecureApplication(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

    def event(self, event):
        if event.type() == 24:
            print("Handling application state change event.")
        return super().event(event)

    def applicationSupportsSecureRestorableState(self):
        return True


class Board(QGraphicsRectItem):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h)
        self.setBrush(QBrush(color))


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        screens = QApplication.screens()
        screen_geometry = screens[0].geometry()
        self.setGeometry(screen_geometry)

        scene = QGraphicsScene(self)
        self.create_board(scene)
        self.add_pieces_to_board(scene)
        self.add_labels_to_board(scene)

        view = QGraphicsView(scene, self)
        view.setRenderHint(QPainter.Antialiasing)
        view.setRenderHint(QPainter.SmoothPixmapTransform)
        self.setCentralWidget(view)
        view.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)  # type: ignore
        view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # type: ignore

    def create_board(self, scene):
        for row in range(8):
            for col in range(8):
                color = LIGHT_COLOR if (row + col) % 2 == 0 else DARK_COLOR
                rect = Board(col * SQUARE_SIZE, row *
                             SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE, color)
                scene.addItem(rect)

    def add_pieces_to_board(self, scene):
        pieces = Pieces()
        pieces.add_pieces(scene)

    def add_labels_to_board(self, scene):
        for col in range(8):
            letter_item = QGraphicsTextItem(LETTERS[col])
            letter_item.setFont(LABEL_FONT)
            letter_item.setDefaultTextColor(Qt.white)  # type: ignore
            letter_item.setPos(col * SQUARE_SIZE +
                               SQUARE_SIZE / 2 - 5, 8.1 * SQUARE_SIZE)
            scene.addItem(letter_item)

        for row in range(8):
            number_item = QGraphicsTextItem(NUMBERS[row])
            number_item.setFont(LABEL_FONT)
            number_item.setDefaultTextColor(Qt.white)  # type: ignore
            number_item.setPos(8.1 * SQUARE_SIZE, row *
                               SQUARE_SIZE + SQUARE_SIZE / 2 - 10)
            scene.addItem(number_item)


if __name__ == '__main__':
    app = SecureApplication(sys.argv)
    window = Window()
    window.setWindowTitle("Ajedrez")
    window.setFixedSize(1040, 780)
    window.show()
    app.exec_()
