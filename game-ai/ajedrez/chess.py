import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QSize, Qt


class ChessApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ajedrez con PyQt5")
        self.setFixedSize(QSize(480, 480))

        self.board = ChessBoard(self)
        self.setCentralWidget(self.board)


class ChessBoard(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.turn = 'white'
        self.init_ui()

    def init_ui(self):
        grid_layout = QGridLayout()
        self.setLayout(grid_layout)
        self.buttons = [[QPushButton(self) for _ in range(8)]
                        for _ in range(8)]

        for row in range(8):
            for col in range(8):
                button = self.buttons[row][col]
                button.setFixedSize(60, 60)
                button.clicked.connect(
                    lambda _, r=row, c=col: self.on_button_click(r, c))
                grid_layout.addWidget(button, row, col)

    def on_button_click(self, row, col):
        button = self.buttons[row][col]
        piece = button.text()

        if piece:
            if (self.turn == 'white' and piece.islower()) or (self.turn == 'black' and piece.isupper()):
                QMessageBox.warning(self, "Turno Incorrecto",
                                    f"Es el turno de {self.turn}")
                return
            # Aquí puedes añadir la lógica para mover piezas
        else:
            button.setText('P' if self.turn == 'white' else 'p')
            self.turn = 'black' if self.turn == 'white' else 'white'
            QMessageBox.information(
                self, "Cambio de Turno", f"Es el turno de {self.turn}")


def main():
    app = QApplication(sys.argv)
    main_window = ChessApp()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
