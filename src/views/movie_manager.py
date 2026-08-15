from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QHeaderView
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from movies import delete_movie, get_movie_by_id
from movies import get_all_movies, search_movies


class MovieManager(QWidget):

    def __init__(self, admin):
        super().__init__()

        self.admin = admin

        self.setWindowTitle("Movie Booking System - Manage Movies")
        self.resize(1200, 700)

        self.setup_ui()
        self.load_movies()

    def setup_ui(self):

        main_layout = QVBoxLayout()

        # ---------- HEADER ----------

        header_layout = QHBoxLayout()

        title = QLabel("🎥 Manage Movies")
        title.setFont(QFont("Arial", 26, QFont.Weight.Bold))

        back_button = QPushButton("← Back")
        back_button.clicked.connect(self.close)

        header_layout.addWidget(title)
        header_layout.addStretch()
        header_layout.addWidget(back_button)

        main_layout.addLayout(header_layout)

        # ---------- SEARCH ----------

        search_layout = QHBoxLayout()

        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText(
            "🔍 Search by title, genre or language..."
        )

        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search_movies)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear_search)

        add_button = QPushButton("+ Add Movie")
        add_button.clicked.connect(self.add_movie)

        search_layout.addWidget(self.search_box)
        search_layout.addWidget(search_button)
        search_layout.addWidget(clear_button)
        search_layout.addWidget(add_button)

        main_layout.addLayout(search_layout)

        # ---------- MOVIE TABLE ----------

        self.movie_table = QTableWidget()

        self.movie_table.setColumnCount(6)

        self.movie_table.setHorizontalHeaderLabels([
            "ID",
            "Title",
            "Genre",
            "Language",
            "Duration",
            "Rating"
        ])

        self.movie_table.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )

        self.movie_table.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )

        self.movie_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        main_layout.addWidget(self.movie_table)

        # ---------- ACTION BUTTONS ----------

        action_layout = QHBoxLayout()

        edit_button = QPushButton("✏ Edit Selected")
        edit_button.clicked.connect(self.edit_movie)

        delete_button = QPushButton("🗑 Delete Selected")
        delete_button.clicked.connect(self.delete_selected_movie)

        action_layout.addWidget(edit_button)
        action_layout.addWidget(delete_button)

        main_layout.addLayout(action_layout)

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

            QTableWidget {
                background-color: #1f2937;
                border: 1px solid #374151;
                gridline-color: #374151;
                border-radius: 8px;
            }

            QHeaderView::section {
                background-color: #374151;
                color: white;
                padding: 8px;
                font-weight: bold;
            }

            QPushButton {
                background-color: #2563eb;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 9px 16px;
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

        self.movie_table.setRowCount(0)

        for movie in movies:

            row = self.movie_table.rowCount()

            self.movie_table.insertRow(row)

            self.movie_table.setItem(
                row,
                0,
                QTableWidgetItem(str(movie["movie_id"]))
            )

            self.movie_table.setItem(
                row,
                1,
                QTableWidgetItem(movie["title"])
            )

            self.movie_table.setItem(
                row,
                2,
                QTableWidgetItem(movie["genre"])
            )

            self.movie_table.setItem(
                row,
                3,
                QTableWidgetItem(movie["language"])
            )

            self.movie_table.setItem(
                row,
                4,
                QTableWidgetItem(
                    f"{movie['duration']} min"
                )
            )

            self.movie_table.setItem(
                row,
                5,
                QTableWidgetItem(
                    str(movie["rating"])
                )
            )

    def get_selected_movie_id(self):

        selected_rows = self.movie_table.selectionModel().selectedRows()

        if not selected_rows:

            QMessageBox.warning(
                self,
                "No Movie Selected",
                "Please select a movie first."
            )

            return None

        row = selected_rows[0].row()

        movie_id = self.movie_table.item(row, 0).text()

        return int(movie_id)

    def add_movie(self):

        from views.add_movie import AddMovieWindow

        self.add_movie_window = AddMovieWindow(self)

        self.add_movie_window.show()

    def edit_movie(self):

        movie_id = self.get_selected_movie_id()

        if movie_id is None:
            return

        from movies import get_movie_by_id

        movie = get_movie_by_id(movie_id)

        if not movie:

            QMessageBox.warning(
                self,
                "Movie Not Found",
                "The selected movie could not be found."
            )

            return

        from views.add_movie import AddMovieWindow

        self.edit_movie_window = AddMovieWindow(
            self,
            movie
        )

        self.edit_movie_window.show()

    def delete_selected_movie(self):

        movie_id = self.get_selected_movie_id()

        if movie_id is None:
            QMessageBox.warning(
                self,
                "No Movie Selected",
                "Please select a movie to delete."
            )
            return

        movie = get_movie_by_id(movie_id)

        if not movie:
            QMessageBox.warning(
                self,
                "Movie Not Found",
                "The selected movie could not be found."
            )
            return

        # Confirmation dialog
        reply = QMessageBox.question(
            self,
            "Confirm Delete",
            f"Are you sure you want to delete\n\n"
            f"'{movie['title']}'?",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply != QMessageBox.StandardButton.Yes:
            return

        try:

            deleted = delete_movie(movie_id)

            if deleted:

                QMessageBox.information(
                    self,
                    "Movie Deleted",
                    f"'{movie['title']}' was deleted successfully."
                )

                self.load_movies()

            else:

                QMessageBox.warning(
                    self,
                    "Delete Failed",
                    "The movie could not be deleted."
                )

        except Exception as e:

            QMessageBox.critical(
                self,
                "Database Error",
                f"Could not delete the movie.\n\n{str(e)}"
            )