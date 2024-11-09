from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QFrame,
)
from PyQt6.QtCore import Qt, QPropertyAnimation, QRect
import sys
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class SimpleUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Simple UI")
        self.setGeometry(100, 100, 600, 400)
        self.resize(1280, 720)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Barra de búsqueda
        search_bar_layout = QVBoxLayout()
        main_layout.addLayout(search_bar_layout)

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search...")
        self.search_bar.setFixedHeight(40)
        self.search_bar.setStyleSheet(
            """
            QLineEdit {
                border-radius: 5px;
                padding: 5px;
                border: 1px solid gray;
            }
        """
        )
        search_bar_layout.addWidget(
            self.search_bar, alignment=Qt.AlignmentFlag.AlignCenter
        )

        self.search_options = QFrame()
        self.search_options.setStyleSheet(
            "background-color: white; border: 1px solid gray;"
        )
        self.search_options.setFixedHeight(0)
        search_bar_layout.addWidget(self.search_options)

        self.search_bar.mousePressEvent = self.expand_search

    def expand_search(self, event):
        self.animation = QPropertyAnimation(self.search_options, b"geometry")
        self.animation.setDuration(300)
        self.animation.setStartValue(
            QRect(
                self.search_options.x(),
                self.search_options.y(),
                self.search_options.width(),
                0,
            )
        )
        self.animation.setEndValue(
            QRect(
                self.search_options.x(),
                self.search_options.y(),
                self.search_options.width(),
                100,
            )
        )
        self.animation.start()


class ChangeHandler(FileSystemEventHandler):
    def __init__(self, app):
        self.app = app

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print("File changed, reloading...")
            self.app.quit()
            os.execv(sys.executable, ["python"] + sys.argv)


if __name__ == "__main__":
    print("Starting application...")
    app = QApplication(sys.argv)
    window = SimpleUI()
    window.show()

    event_handler = ChangeHandler(app)
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=True)
    observer.start()

    try:
        sys.exit(app.exec())
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

    print("Application reloaded successfully!")
