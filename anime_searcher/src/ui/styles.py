"""
Estilos de la app
"""


def apply_styles(app):
    """
    Estilos generales de la app
    """
    app.setStyleSheet(
        """
        QMainWindow {
            background-color: #2b2b2b;
        }
        QLineEdit {
            border: 1px solid #5a5a5a;
            border-radius: 5px;
            padding: 5px;
            color: #ffffff;
            background-color: #3c3c3c;
            width: 10px
        }
        QLineEdit:focus {
            border: 1px solid #ffaa00;
        }
        QPushButton {
            background-color: #ffaa00;
            color: #2b2b2b;
            font-weight: bold;
            padding: 8px 15px;
            border-radius: 5px;
            border: none;
        }
        QPushButton:disabled {
            background-color: #555555;
            color: #aaaaaa;
        }
        QTextEdit {
            background-color: #3c3c3c;
            color: #ffffff;
            border: 1px solid #5a5a5a;
            border-radius: 5px;
            padding: 5px;
            width: 10px
        }
        QPushButton:hover {
            background-color: #ffbf00;
        }
    """
    )
