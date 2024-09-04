from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsItem, QGraphicsDropShadowEffect, QMessageBox
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

LETTERS = 'abcdefgh'
NUMBERS = '87654321'


class Move(QGraphicsPixmapItem):
    saves = []
    eats = []
    turn = 'white'

    def __init__(self, pixmap, x, y, color, piece_logic=None):
        super().__init__(pixmap)
        self.setPos(x, y)
        self.piece_logic = piece_logic
        self.start_x = x
        self.start_y = y
        self.piece_color = color
        self.setAcceptHoverEvents(True)
        self.setAcceptTouchEvents(True)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)  # type: ignore

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:  # type: ignore
            if Move.saves and Move.saves[-1]['color'][-1] == self.data(0)["chess_piece"][-1]:
                QMessageBox.warning(
                    None, "Error", "Es el turno del otro jugador.")
                return

            self.setShadowEffect(True)
            super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:  # type: ignore
            self.setShadowEffect(False)
            if not self.snap_to_grid():
                return
            super().mouseReleaseEvent(event)

    def snap_to_grid(self):
        square_size = 80
        x = self.x()
        y = self.y()

        nearest_col = max(0, min(7, round(x / square_size)))
        nearest_row = max(0, min(7, round(y / square_size)))

        start_row = round(self.start_y / square_size)
        start_col = round(self.start_x / square_size)

        if self.piece_logic:
            if not self.piece_logic.validate_move(start_row, start_col, nearest_row, nearest_col, self.check_collisions()):
                self.setPos(self.start_x, self.start_y)
                return False

        new_x = nearest_col * square_size
        new_y = nearest_row * square_size

        if new_x == self.start_x and new_y == self.start_y:
            self.setPos(self.start_x, self.start_y)
            return False

        self.setPos(new_x, new_y)

        end_row = nearest_row
        end_col = nearest_col

        captured_piece = self.check_collisions()

        Move.saves.append({
            'color': self.piece_color,
            'start': (f"{LETTERS[start_col].capitalize()}{NUMBERS[start_row]}"),
            'end': (f"{LETTERS[end_col].capitalize()}{NUMBERS[end_row]}"),
            'eats': (captured_piece.data(0)["chess_piece"] if captured_piece else None),
        })

        if captured_piece:
            captured_piece.setVisible(False)

        self.start_x = new_x
        self.start_y = new_y

        print(Move.saves)
        return True

    def check_collisions(self):
        for item in self.scene().items():  # type: ignore
            data = item.data(0)
            if item is not self and data and "chess_piece" in data and self.collidesWithItem(item):
                return item
        return None

    def setShadowEffect(self, enabled):
        if enabled:
            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(30)
            shadow.setColor(QColor(0, 0, 0, 150))
            self.setGraphicsEffect(shadow)
            self.setZValue(1)
        else:
            self.setGraphicsEffect(None)
            self.setZValue(0)
