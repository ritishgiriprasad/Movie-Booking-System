
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from shows import get_shows_for_movie


class ShowtimeSelection(QWidget):

    def __init__(self, user, movie):
        super().__init__()

        self.movie = movie
        self.parent_user = user
        self.setWindowTitle(f"Showtimes - {movie['title']}")
        self.resize(700, 500)

        self.setup_ui()
        self.load_showtimes()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)

        title = QLabel(f"🎬 {self.movie['title']}")
        title.setFont(QFont("Arial", 22, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        subtitle = QLabel("Select a showtime to continue")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.showtimes_layout = QVBoxLayout()
        self.showtimes_layout.setSpacing(10)

        back_button = QPushButton("← Back")
        back_button.clicked.connect(self.close)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addLayout(self.showtimes_layout)
        layout.addStretch()
        layout.addWidget(back_button)

        self.setLayout(layout)

    def load_showtimes(self):
        shows = get_shows_for_movie(self.movie["movie_id"])

        # Only display shows that have not already passed.
        from datetime import datetime, date, time, timedelta

        now = datetime.now()
        upcoming_shows = []

        for show in shows:
            show_date = show["show_date"]
            show_time = show["show_time"]

            # PyMySQL may return TIME values as timedelta.
            if isinstance(show_time, timedelta):
                show_time = (datetime.min + show_time).time()

            show_datetime = datetime.combine(show_date, show_time)

            if show_datetime > now and show["available_seats"] > 0:
                upcoming_shows.append(show)

        if not upcoming_shows:
            message = QLabel(
                "No upcoming shows are currently available for this movie."
            )
            message.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.showtimes_layout.addWidget(message)
            return

        for show in upcoming_shows:
            show_button = QPushButton(
                f"{show['show_date'].strftime('%d %b %Y')}  |  "
                f"{show_time.strftime('%I:%M %p')}  |  "
                f"{show['hall_name']}  |  "
                f"₹{show['price']}"
            )

            show_button.setMinimumHeight(45)
            show_button.clicked.connect(
                lambda checked=False, selected_show=show:
                    self.select_show(selected_show)
            )

            self.showtimes_layout.addWidget(show_button)

    
    def select_show(self, show):
        from views.seat_selection import SeatSelection

        self.seat_selection_window = SeatSelection(
            self.parent_user,
            show
        )

        self.seat_selection_window.show()

