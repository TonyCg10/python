import requests
from io import BytesIO
import os

# pylint: disable=no-name-in-module
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPixmap, QGuiApplication
from PyQt6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QFrame,
    QPushButton,
    QGraphicsDropShadowEffect,
    QLabel,
    QScrollArea,
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
        self.setGeometry(0, 0, 800, 800)

        self.anime_loader = JsonLibrary()
        self.anime_loader.load_data("assets/anime-offline-database-minified.json")
        self.anime_library = Library()
        self.anime_library.animes = self.anime_loader.get_anime()

        self.init_ui()
        apply_styles(self)

        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()
        center_point = screen_geometry.center()
        window_geometry.moveCenter(center_point)
        self.move(window_geometry.topLeft())

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

        v_layout.addLayout(button_layout)

        self.result_area = QScrollArea()
        self.result_area.setFrameShape(QFrame.Shape.Panel)
        self.result_area.setFrameShadow(QFrame.Shadow.Plain)
        self.result_area.setWidgetResizable(True)

        self.result_content = QWidget()
        self.result_layout = QVBoxLayout(self.result_content)
        self.result_area.setWidget(self.result_content)

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

    def load_image(self, anime):
        """
        Intenta cargar una imagen desde una URL o una ruta de archivo local.
        """
        pixmap = QPixmap()

        if anime.picture:
            if anime.picture.startswith("http"):
                try:
                    response = requests.get(anime.picture, timeout=5)
                    response.raise_for_status()
                    image_data = BytesIO(response.content)
                    pixmap.loadFromData(image_data.read())
                except requests.exceptions.Timeout:
                    print("Request timed out while trying to load the image.")
                except requests.exceptions.RequestException as e:
                    print(f"Error loading image from URL: {e}")
            elif os.path.isfile(anime.picture):
                if not pixmap.load(anime.picture):
                    print(f"Failed to load image from local file: {anime.picture}")
            else:
                print(f"Image path does not exist: {anime.picture}")
        return pixmap

    def get_random_anime(self):
        """
        Obtiene un anime aleatorio de la biblioteca y muestra su imagen y detalles.
        """
        anime = get_random_anime(self.anime_loader)
        self.clear_result_area()

        if not anime:
            self.result_layout.addWidget(QLabel("<b>No anime available.</b>"))
            return

        anime_details = (
            f"<b>Título:</b> {anime.title}<br>"
            f"<b>Tipo:</b> {anime.anime_type.name}<br>"
            f"<b>Estado:</b> {anime.status.name}<br>"
            f"<b>Etiquetas:</b> {', '.join(anime.tags)}<br>"
            f"<b>Episodios:</b> {anime.episodes}<br>"
            f"<b>Temporada:</b> {anime.anime_season.season.name if anime.anime_season else 'N/A'}, "
            f"{anime.anime_season.year if anime.anime_season else 'N/A'}<br><br>"
        )
        anime_details_label = QLabel()
        anime_details_label.setTextFormat(Qt.TextFormat.RichText)
        anime_details_label.setText(anime_details)
        anime_details_label.setWordWrap(True)

        self.result_layout.addWidget(anime_details_label)

        pixmap = self.load_image(anime)

        if not pixmap.isNull():
            image_label = QLabel()
            image_label.setPixmap(
                pixmap.scaledToWidth(200, Qt.TransformationMode.SmoothTransformation)
            )
            self.result_layout.addWidget(image_label)
        else:
            print("Failed to load image; Pixmap is null.")

    def clear_result_area(self):
        """
        Borra todos los widgets en el diseño del área de resultados.
        """
        for i in reversed(range(self.result_layout.count())):
            widget = self.result_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)
