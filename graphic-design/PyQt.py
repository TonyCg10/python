from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QListWidget,
    QListWidgetItem,
    QPushButton,
)
import sys


class SimpleUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Simple UI")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Barra superior
        top_bar_layout = QHBoxLayout()
        main_layout.addLayout(top_bar_layout)

        home_button = QPushButton("Home")
        top_bar_layout.addWidget(home_button)

        settings_button = QPushButton("Settings")
        top_bar_layout.addWidget(settings_button)

        # Contenido principal
        content_layout = QHBoxLayout()
        main_layout.addLayout(content_layout)

        # Barra lateral
        side_bar = QListWidget()
        side_bar.addItem(QListWidgetItem("Item 1"))
        side_bar.addItem(QListWidgetItem("Item 2"))
        side_bar.addItem(QListWidgetItem("Item 3"))
        side_bar.addItem(QListWidgetItem("Item 4"))
        content_layout.addWidget(side_bar)

        # Lista principal
        main_list = QListWidget()
        main_list.addItem(QListWidgetItem("Element 1"))
        main_list.addItem(QListWidgetItem("Element 2"))
        main_list.addItem(QListWidgetItem("Element 3"))
        main_list.addItem(QListWidgetItem("Element 4"))
        content_layout.addWidget(main_list)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleUI()
    window.show()
    sys.exit(app.exec())
