# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton


class SearchByTitleWidget(QWidget):
    """
    Busca un anime por su título exacto.
    """

    def __init__(self, on_search):
        super().__init__()

        layout = QVBoxLayout()
        title_layout = QHBoxLayout()

        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Ingresa el título exacto del anime")

        self.search_button = QPushButton("🔍")
        self.search_button.setEnabled(False)

        self.search_button.clicked.connect(lambda: on_search(self.title_input.text()))
        self.title_input.textChanged.connect(self.toggle_search_button)

        title_layout.addWidget(self.title_input)
        title_layout.addWidget(self.search_button)

        layout.addLayout(title_layout)
        self.setLayout(layout)

    def toggle_search_button(self):
        """
        Botón de búsqueda.
        """
        self.search_button.setEnabled(bool(self.title_input.text().strip()))


class SearchByContainTitleWidget(QWidget):
    """
    Busca un anime por una subcadena dentro del título.
    """

    def __init__(self, on_search):
        super().__init__()

        layout = QVBoxLayout()
        contains_layout = QHBoxLayout()

        self.contains_input = QLineEdit(self)
        self.contains_input.setPlaceholderText(
            "Ingresa texto que contenga el título del anime"
        )

        self.search_contains_button = QPushButton("🔍")
        self.search_contains_button.setEnabled(False)

        self.search_contains_button.clicked.connect(
            lambda: on_search(self.contains_input.text())
        )
        self.contains_input.textChanged.connect(self.toggle_search_button)

        contains_layout.addWidget(self.contains_input)
        contains_layout.addWidget(self.search_contains_button)

        layout.addLayout(contains_layout)
        self.setLayout(layout)

    def toggle_search_button(self):
        """
        Botón de búsqueda.
        """
        self.search_contains_button.setEnabled(bool(self.contains_input.text().strip()))
