import sys
import os
from PyQt6.QtWidgets import QApplication
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time


class ChangeHandler(FileSystemEventHandler):
    def __init__(self, app):
        self.app = app

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print("File changed, reloading...")
            self.app.quit()
            os.execv(sys.executable, ["python"] + sys.argv)


if __name__ == "__main__":
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
