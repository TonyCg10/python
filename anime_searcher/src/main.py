import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QMessageBox,
)
from PyQt5.QtCore import Qt
from main_code import (
    loader,
    library,
    search_by_title,
    search_by_criteria,
    get_random_anime,
    get_status,
    get_season,
    get_type,
    get_year,
    get_tags,
)


class AnimeApp(QMainWindow):
    def __init__(self):
        super().__init__()

        try:
            self.loader = loader
            self.library = library
        except Exception as e:
            self.show_error_message(f"Error loading library or loader: {e}")
            return

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Anime Library")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        # Labels
        self.command_label = QLabel(
            "Use the fields below to search for anime:")
        layout.addWidget(self.command_label)

        # Input Fields
        self.add_input_fields(layout)

        # Result Area
        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)
        layout.addWidget(self.result_area)

        # Buttons
        self.add_buttons(layout)

        self.central_widget.setLayout(layout)

    def add_input_fields(self, layout):
        # Title Search
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Title")
        layout.addWidget(self.title_input)

        # Criteria Search
        self.type_input = QLineEdit()
        self.type_input.setPlaceholderText("Type (e.g., TV, Movie)")
        layout.addWidget(self.type_input)

        self.year_input = QLineEdit()
        self.year_input.setPlaceholderText("Year (e.g., 2021)")
        layout.addWidget(self.year_input)

        self.season_input = QLineEdit()
        self.season_input.setPlaceholderText("Season (e.g., Spring, Summer)")
        layout.addWidget(self.season_input)

        self.status_input = QLineEdit()
        self.status_input.setPlaceholderText(
            "Status (e.g., Ongoing, Finished)")
        layout.addWidget(self.status_input)

        self.tags_input = QLineEdit()
        self.tags_input.setPlaceholderText("Tags (comma separated)")
        layout.addWidget(self.tags_input)

        self.limit_input = QLineEdit()
        self.limit_input.setPlaceholderText("Limit")
        layout.addWidget(self.limit_input)

    def add_buttons(self, layout):
        # Search Button
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.process_search)
        layout.addWidget(self.search_button)

        # Random Button
        self.random_button = QPushButton("Random Anime")
        self.random_button.clicked.connect(self.show_random_anime)
        layout.addWidget(self.random_button)

    def process_search(self):
        try:
            title = self.title_input.text().strip()
            type_ = self.type_input.text().strip()
            year = self.year_input.text().strip()
            season = self.season_input.text().strip()
            status = self.status_input.text().strip()
            tags = self.tags_input.text().strip()
            limit = self.limit_input.text().strip()

            # Validate year and limit inputs
            if year and not year.isdigit():
                self.show_error_message("Year must be a valid number.")
                return

            if limit and not limit.isdigit():
                self.show_error_message("Limit must be a valid number.")
                return

            # If title is provided, prioritize title search
            if title:
                result = search_by_title(self.library, title)
            else:
                # Otherwise, search by criteria
                type_search = get_type(type_) if type_ else None
                year_search = get_year(year) if year else 0
                season_search = get_season(season) if season else None
                status_search = get_status(status) if status else None
                tags_search = get_tags(tags) if tags else []
                limit_search = int(limit) if limit else 0

                result = search_by_criteria(
                    self.library,
                    type_search,
                    year_search,
                    season_search,
                    status_search,
                    tags_search,
                    limit_search,
                )

            if not result:
                self.result_area.setText("No results found.")
            else:
                self.result_area.setText(result)

        except Exception as e:
            self.show_error_message(f"An error occurred during search: {e}")

    def show_random_anime(self):
        try:
            result = get_random_anime(self.loader)
            self.result_area.setText(result)
        except Exception as e:
            self.show_error_message(f"An error occurred: {e}")

    def show_error_message(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setText(message)
        msg_box.setWindowTitle("Error")
        msg_box.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = AnimeApp()
    ex.show()
    sys.exit(app.exec())
