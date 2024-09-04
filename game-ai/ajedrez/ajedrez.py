import sys
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ReloadHandler(FileSystemEventHandler):
    def __init__(self, process, script):
        super().__init__()
        self.process = process
        self.script = script

    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            print(f'\n{time.strftime("%Y-%m-%d %H:%M:%S")
                       } - {event.src_path} has been modified, restarting application...')
            self.process.terminate()
            self.process.wait()
            self.process = subprocess.Popen([sys.executable, self.script])
            print(f'{time.strftime("%Y-%m-%d %H:%M:%S")
                     } - Application restarted.')


def start_application(script):
    return subprocess.Popen([sys.executable, script])


if __name__ == "__main__":
    script = 'ajedrez/ajedrezui/ajedrez_ui.py'
    process = start_application(script)

    event_handler = ReloadHandler(process, script)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()

    print('Starting application with hot reloading...')
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('KeyboardInterrupt caught, stopping observer...')
        observer.stop()
        process.terminate()

    observer.join()
    process.wait()
    print('Observer has been stopped.')
