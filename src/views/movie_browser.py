from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QScrollArea,
    QGridLayout,
    QFrame,
    QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from movies import get_all_movies, search_movies


class MovieBrowser(QWidget):

    def __init__(self, user):
        super().__init__()

        self.user = user

        self.setWindowTitle("Movie Booking System - Browse Movies")
        self.resize(1200, 750)

        self.setup_ui()
        self.load_movies()

    def setup_ui(self):

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 25, 30, 25)
        main_layout.setSpacing(20)

        # ---------- HEADER ----------

        header = QHBoxLayout()

        title = QLabel("🎬 Browse Movies")
        title.setFont(QFont("Arial", 26, QFont.Weight.Bold))

        back_button = QPushButton("← Back")
        back_button.clicked.connect(self.close)

        header.addWidget(title)
        header.addStretch()
        header.addWidget(back_button)

        main_layout.addLayout(header)

        # ---------- SEARCH ----------

        search_layout = QHBoxLayout()

        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("🔍 Search by title, genre or language...")
        self.search_box.setFixedHeight(42)

        search_button = QPushButton("Search")
        search_button.setFixedHeight(42)
        search_button.clicked.connect(self.search_movies)

        clear_button = QPushButton("Clear")
        clear_button.setFixedHeight(42)
        clear_button.clicked.connect(self.clear_search)

        search_layout.addWidget(self.search_box)
        search_layout.addWidget(search_button)
        search_layout.addWidget(clear_button)

        main_layout.addLayout(search_layout)

        # ---------- MOVIE GRID ----------

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)

        self.movie_container = QWidget()

        self.movie_grid = QGridLayout()
        self.movie_grid.setSpacing(20)
        self.movie_grid.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.movie_container.setLayout(self.movie_grid)

        self.scroll_area.setWidget(self.movie_container)

        main_layout.addWidget(self.scroll_area)

        self.setLayout(main_layout)

        # ---------- STYLE ----------

        self.setStyleSheet("""
            QWidget {
                background-color: #111827;
                color: white;
            }

            QLineEdit {
                background-color: #1f2937;
                border: 1px solid #374151;
                border-radius: 8px;
                padding: 8px 12px;
                font-size: 14px;
            }

            QLineEdit:focus {
                border: 1px solid #3b82f6;
            }

            QPushButton {
                background-color: #2563eb;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 14px;
            }

            QPushButton:hover {
                background-color: #1d4ed8;
            }
        """)

    def load_movies(self):

        movies = get_all_movies()

        self.display_movies(movies)

    def search_movies(self):

        search_text = self.search_box.text().strip()

        if not search_text:
            self.load_movies()
            return

        movies = search_movies(search_text)

        self.display_movies(movies)

    def clear_search(self):

        self.search_box.clear()

        self.load_movies()

    def display_movies(self, movies):

        # Clear existing cards

        while self.movie_grid.count():

            item = self.movie_grid.takeAt(0)

            widget = item.widget()

            if widget:
                widget.deleteLater()

        if not movies:

            message = QLabel("No movies found.")
            message.setAlignment(Qt.AlignmentFlag.AlignCenter)
            message.setFont(QFont("Arial", 18))

            self.movie_grid.addWidget(message, 0, 0)

            return

        columns = 3

        for index, movie in enumerate(movies):

            row = index // columns
            column = index % columns

            card = self.create_movie_card(movie)

            self.movie_grid.addWidget(card, row, column)

    def create_movie_card(self, movie):

        card = QFrame()

        card.setFixedSize(330, 230)

        card.setStyleSheet("""
            QFrame {
                background-color: #1f2937;
                border: 1px solid #374151;
                border-radius: 12px;
            }
        """)

        layout = QVBoxLayout()

        layout.setContentsMargins(18, 15, 18, 15)
        layout.setSpacing(8)

        title = QLabel(movie["title"])
        title.setFont(QFont("Arial", 17, QFont.Weight.Bold))
        title.setWordWrap(True)

        genre = QLabel(
            f"{movie['genre']} • {movie['language']}"
        )

        duration = QLabel(
            f"⏱ {movie['duration']} minutes"
        )

        rating = QLabel(
            f"⭐ {movie['rating']}"
        )

        details_button = QPushButton("View Details")

        details_button.clicked.connect(
            lambda checked=False, m=movie:
            self.show_movie_details(m)
        )

        layout.addWidget(title)
        layout.addWidget(genre)
        layout.addWidget(duration)
        layout.addWidget(rating)

        layout.addStretch()

        layout.addWidget(details_button)

        card.setLayout(layout)

        return card

    
    def show_movie_details(self, movie):
        from views.showtime_selection import ShowtimeSelection

        self.showtime_window = ShowtimeSelection(
            self.user,
            movie
        )

        self.showtime_window.show()
