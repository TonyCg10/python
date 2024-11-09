# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QComboBox,
    QLineEdit,
    QPushButton,
)

from utils.searchFns import (
    get_type,
    get_status,
    get_season,
    get_tags,
)

from models.animeEnum import Type, Status, Season


class SearchByCriteriaWidget(QWidget):
    """
    Widget para buscar animes basados en múltiples criterios.
    """

    def __init__(self, on_search, anime_library):
        super().__init__()
        self.anime_library = anime_library

        self.type_combo = QComboBox(self)
        self.type_combo.addItems([e.name for e in Type])

        self.year_combo = QComboBox(self)
        self.year_combo.addItems(self.get_all_years())
        self.year_combo.setEditable(False)

        self.status_combo = QComboBox(self)
        self.status_combo.addItems([e.name for e in Status])

        self.season_combo = QComboBox(self)
        self.season_combo.addItems([e.name for e in Season])

        self.tags_combo = QComboBox(self)
        self.tags_combo.addItems(self.get_all_tags())

        self.limit_input = QLineEdit(self)
        self.limit_input.setPlaceholderText("Enter result limit")

        self.search_criteria_button = QPushButton("🔍", self)
        self.search_criteria_button.clicked.connect(self.on_search_clicked)

        fixed_height = 30
        self.tags_combo.setFixedHeight(fixed_height)
        self.limit_input.setFixedHeight(fixed_height)
        self.search_criteria_button.setFixedHeight(fixed_height)

        main_layout = QVBoxLayout()

        top_row_layout = QHBoxLayout()
        top_row_layout.addWidget(self.type_combo)
        top_row_layout.addWidget(self.status_combo)
        top_row_layout.addWidget(self.year_combo)

        bottom_row_layout = QHBoxLayout()
        bottom_row_layout.addWidget(self.tags_combo, stretch=2)
        bottom_row_layout.addWidget(self.limit_input, stretch=1)
        bottom_row_layout.addWidget(self.search_criteria_button, stretch=0)

        main_layout.addLayout(top_row_layout)
        main_layout.addWidget(self.season_combo)
        main_layout.addLayout(bottom_row_layout)

        self.setLayout(main_layout)
        self.on_search = on_search

    def get_all_tags(self):
        """
        Devuelve todas las etiquetas únicas en la biblioteca de anime.
        """

        all_tags = {
            tag
            for anime in self.anime_library.animes
            if anime.tags
            for tag in anime.tags
        }
        return sorted(list(all_tags))

    def get_all_years(self):
        """
        Devuelve todos los años únicos de las temporadas de anime en la biblioteca.
        """

        all_years = {
            anime.anime_season.year
            for anime in self.anime_library.animes
            if anime.anime_season
        }
        return sorted(list(map(str, all_years)))

    def on_search_clicked(self):
        """
        Ejecuta la búsqueda con los criterios seleccionados.
        """

        type_str = self.type_combo.currentText()
        year_str = self.year_combo.currentText()
        season_str = self.season_combo.currentText()
        status_str = self.status_combo.currentText()
        tags_str = self.tags_combo.currentText()
        limit_str = self.limit_input.text()

        type_search = get_type(type_str)
        year_search = int(year_str) if year_str.isdigit() else None
        season_search = get_season(season_str)
        status_search = get_status(status_str)
        tags_search = get_tags(tags_str)
        limit = int(limit_str) if limit_str.isdigit() else 0

        self.on_search(
            type_search, year_search, season_search, status_search, tags_search, limit
        )
