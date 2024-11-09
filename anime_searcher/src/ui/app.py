# pylint: disable=no-name-in-module
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QFrame,
    QPushButton,
    QTextEdit,
    QGraphicsDropShadowEffect,
)

from services.jsonLibrary import JsonLibrary
from services.library import Library

from utils.searchFns import (
    search_by_title,
    search_by_titles,
    search_by_criteria,
    get_random_anime,
)

from .widgets.searchByTitle import SearchByTitleWidget, SearchByContainTitleWidget
from .widgets.searchByCriteria import SearchByCriteriaWidget

from .styles import apply_styles


class AnimeApp(QMainWindow):
    """
    Clase principal para la aplicación de la biblioteca de animes utilizando PyQt6.
    """

    def __init__(self):
        """
        Inicializa la interfaz principal de la aplicación.
        """
        super().__init__()

        self.setWindowTitle("Biblioteca de Animes")
        self.setGeometry(100, 100, 600, 600)

        self.anime_loader = JsonLibrary()
        self.anime_loader.load_data("assets/anime-offline-database-minified.json")
        self.anime_library = Library()
        self.anime_library.animes = self.anime_loader.get_anime()

        self.result_area = QTextEdit(self)

        self.init_ui()
        apply_styles(self)

    def init_ui(self):
        """
        Configure el diseño inicial de la interfaz de usuario.
        """
        v_layout = QVBoxLayout()

        self.search_by_title = SearchByTitleWidget(self.search_anime_by_title)
        v_layout.addWidget(self.search_by_title)

        self.search_by_contain = SearchByContainTitleWidget(
            self.search_anime_by_contain_title
        )
        v_layout.addWidget(self.search_by_contain)

        self.search_by_criteria = SearchByCriteriaWidget(
            self.search_anime_by_criteria, self.anime_library
        )
        v_layout.addWidget(self.search_by_criteria)

        self.result_area.setReadOnly(True)
        self.result_area.setFrameShape(QFrame.Shape.Panel)
        self.result_area.setFrameShadow(QFrame.Shadow.Plain)

        result_layout = QVBoxLayout(self.result_area)
        result_layout.setContentsMargins(0, 0, 0, 0)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        self.random_button = QPushButton("Random", self)

        self.random_button.clicked.connect(self.get_random_anime)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(2, 2)
        shadow.setColor(QColor(0, 0, 0, 120))
        self.random_button.setGraphicsEffect(shadow)

        button_layout.addWidget(
            self.random_button,
            alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight,
        )

        result_layout.addLayout(button_layout)

        v_layout.addWidget(self.result_area)

        container = QWidget()
        container.setLayout(v_layout)
        self.setCentralWidget(container)

    def search_anime_by_title(self, title):
        """
        Busca un anime por su título exacto.
        """
        result = search_by_title(self.anime_library, title)
        self.result_area.setText(result)

    def search_anime_by_contain_title(self, contain):
        """
        Busca un anime por una subcadena dentro del título.
        """
        result = search_by_titles(self.anime_library, contain)
        self.result_area.setText(result)

    def search_anime_by_criteria(
        self, type_search, year_search, season_search, status_search, tags_search, limit
    ):
        """
        Busca animes según múltiples criterios: tipo, año, temporada, estado, etiquetas.
        """
        result = search_by_criteria(
            self.anime_library,
            type_search,
            year_search,
            season_search,
            status_search,
            tags_search,
            limit,
        )
        self.result_area.setText(result)

    def get_random_anime(self):
        """
        Obtiene un anime aleatorio de la biblioteca y muestra la imagen y detalles.
        """
        anime = get_random_anime(self.anime_loader)

        self.result_area.clear()

        self.result_area.append(anime)
