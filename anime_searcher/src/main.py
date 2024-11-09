import sys

# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QApplication

from ui.app import AnimeApp


def main():
    """
    Función principal para ejecutar la aplicación PyQt6.
    Crea una instancia de la aplicación y muestra la ventana principal.
    """
    app = QApplication(sys.argv)
    window = AnimeApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
