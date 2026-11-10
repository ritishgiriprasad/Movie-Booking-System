from PyQt6.QtWidgets import (
    QDialog,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QTextEdit,
    QMessageBox,
    QDateEdit
)
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QDate, Qt

from movies import add_movie


class AddMovieWindow(QDialog):

    def __init__(self, parent=None, movie=None):
        super().__init__(parent)

        self.parent_window = parent
        self.movie = movie

        self.setWindowTitle("Edit Movie" if movie else "Add Movie")
        self.setFixedSize(500, 650)

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, False)
        self.setAutoFillBackground(True)

        self.setup_ui()

        if self.movie:
            self.load_movie_data()

    def setup_ui(self):

        layout = QVBoxLayout()
        layout.setSpacing(12)
        layout.setContentsMargins(30, 25, 30, 25)

        title = QLabel("🎬 Add New Movie")
        title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(title)
        layout.addSpacing(15)

        # Title

        layout.addWidget(QLabel("Movie Title"))

        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Enter movie title")
        layout.addWidget(self.title_input)

        # Genre

        layout.addWidget(QLabel("Genre"))

        self.genre_input = QLineEdit()
        self.genre_input.setPlaceholderText("e.g. Action, Comedy")
        layout.addWidget(self.genre_input)

        # Language

        layout.addWidget(QLabel("Language"))

        self.language_input = QLineEdit()
        self.language_input.setPlaceholderText("e.g. Hindi, English")
        layout.addWidget(self.language_input)

        # Duration

        layout.addWidget(QLabel("Duration (minutes)"))

        self.duration_input = QLineEdit()
        self.duration_input.setPlaceholderText("e.g. 150")
        layout.addWidget(self.duration_input)

        # Rating

        layout.addWidget(QLabel("Rating"))

        self.rating_input = QLineEdit()
        self.rating_input.setPlaceholderText("e.g. 8.5")
        layout.addWidget(self.rating_input)

        # Release date

        layout.addWidget(QLabel("Release Date"))

        self.release_date_input = QDateEdit()
        self.release_date_input.setCalendarPopup(True)
        self.release_date_input.setDate(QDate.currentDate())
        layout.addWidget(self.release_date_input)

        # Description

        layout.addWidget(QLabel("Description"))

        self.description_input = QTextEdit()
        self.description_input.setPlaceholderText(
            "Enter movie description"
        )
        self.description_input.setFixedHeight(100)
        layout.addWidget(self.description_input)

        # Buttons

        button_layout = QHBoxLayout()

        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.close)

        add_button = QPushButton(
            "Save Changes" if self.movie else "Add Movie"
        )
        add_button.clicked.connect(self.save_movie)

        button_layout.addWidget(cancel_button)
        button_layout.addWidget(add_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

        self.setStyleSheet("""
            QDialog {
                background-color: #111827;
                color: white;
            }

            QLabel {
                background-color: transparent;
                color: white;
            }

            QLineEdit,
            QTextEdit,
            QDateEdit {
                background-color: #1f2937;
                color: white;
                border: 1px solid #374151;
                border-radius: 8px;
                padding: 8px;
            }

            QPushButton {
                background-color: #2563eb;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px;
            }

            QPushButton:hover {
                background-color: #1d4ed8;
            }
        """)

    def save_movie(self):

        title = self.title_input.text().strip()
        genre = self.genre_input.text().strip()
        language = self.language_input.text().strip()
        duration = self.duration_input.text().strip()
        rating = self.rating_input.text().strip()

        release_date = self.release_date_input.date().toString(
            "yyyy-MM-dd"
        )

        description = self.description_input.toPlainText().strip()

        # ---------- VALIDATION ----------

        if not title or not genre or not language:

            QMessageBox.warning(
                self,
                "Missing Information",
                "Please fill in the title, genre and language."
            )

            return

        try:
            duration = int(duration)

        except ValueError:

            QMessageBox.warning(
                self,
                "Invalid Duration",
                "Duration must be a whole number."
            )

            return

        try:
            rating = float(rating)

        except ValueError:

            QMessageBox.warning(
                self,
                "Invalid Rating",
                "Rating must be a number such as 8.5."
            )

            return

        if duration <= 0:

            QMessageBox.warning(
                self,
                "Invalid Duration",
                "Duration must be greater than zero."
            )

            return

        if rating < 0 or rating > 10:

            QMessageBox.warning(
                self,
                "Invalid Rating",
                "Rating must be between 0 and 10."
            )

            return

                # ---------- DATABASE ----------
        try:
            if self.movie:
                from movies import update_movie

                success = update_movie(
                    self.movie["movie_id"],
                    title,
                    genre,
                    language,
                    duration,
                    rating,
                    release_date,
                    description,
                )

                if success:
                    QMessageBox.information(
                        self, "Movie Updated", "Movie updated successfully!"
                    )
                else:
                    QMessageBox.warning(
                        self, "Update Failed", "The movie could not be updated."
                    )
                    return

            else:
                movie_id = add_movie(
                    title,
                    genre,
                    language,
                    duration,
                    rating,
                    release_date,
                    description,
                )

                QMessageBox.information(
                    self,
                    "Movie Added",
                    f"Movie added successfully!\n\nMovie ID: {movie_id}",
                )

            if self.parent_window:
                self.parent_window.load_movies()

            self.close()

        except Exception as e:
            QMessageBox.critical(
                self, "Database Error", f"Could not save movie.\n\n{str(e)}"
            )
    def load_movie_data(self):

        self.title_input.setText(
            self.movie["title"]
        )

        self.genre_input.setText(
            self.movie["genre"]
        )

        self.language_input.setText(
            self.movie["language"]
        )

        self.duration_input.setText(
            str(self.movie["duration"])
        )

        self.rating_input.setText(
            str(self.movie["rating"])
        )

        release_date = self.movie["release_date"]

        self.release_date_input.setDate(
            QDate(
                release_date.year,
                release_date.month,
                release_date.day
            )
        )

        self.description_input.setPlainText(
            self.movie["description"]
        )