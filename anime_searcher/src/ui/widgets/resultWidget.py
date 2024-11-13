# pylint: disable=no-name-in-module
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QVBoxLayout, QLabel, QScrollArea, QFrame, QWidget


class ResultsWidget(QScrollArea):
    """
    Widget para mostrar los resultados de búsqueda de anime.
    """

    def __init__(self):
        super().__init__()

        self.setFrameShape(QFrame.Shape.Panel)
        self.setFrameShadow(QFrame.Shadow.Plain)
        self.setWidgetResizable(True)

        self.result_content = QWidget()
        self.result_layout = QVBoxLayout(self.result_content)
        self.setWidget(self.result_content)

    def clear_results(self):
        """
        Borra todos los widgets en el área de resultados.
        """
        for i in reversed(range(self.result_layout.count())):
            widget = self.result_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

    def display_text_result(self, text):
        """
        Muestra un resultado de texto.
        """
        label = QLabel(text)
        label.setTextFormat(Qt.TextFormat.RichText)
        label.setWordWrap(True)
        self.result_layout.addWidget(label)

    def display_image_result(self, pixmap: QPixmap):
        """
        Muestra una imagen en los resultados.
        """
        if not pixmap.isNull():
            image_label = QLabel()
            image_label.setPixmap(
                pixmap.scaledToWidth(200, Qt.TransformationMode.SmoothTransformation)
            )
            self.result_layout.addWidget(image_label)
