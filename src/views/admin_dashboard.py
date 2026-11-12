
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class AdminDashboard(QWidget):

    def __init__(self, admin):
        super().__init__()

        self.admin = admin

        self.setWindowTitle("Movie Booking System - Admin Dashboard")
        self.resize(1000, 600)

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(20)

        title = QLabel("🎬 Movie Booking System")
        title.setFont(QFont("Arial", 28, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        welcome = QLabel(f"Welcome, {self.admin['name']}!")
        welcome.setFont(QFont("Arial", 18))
        welcome.setAlignment(Qt.AlignmentFlag.AlignCenter)

        movies_btn = QPushButton("🎥 Manage Movies")
        movies_btn.setFixedHeight(50)
        movies_btn.clicked.connect(self.open_movie_manager)

        shows_btn = QPushButton("🎞 Manage Shows")
        shows_btn.setFixedHeight(50)
        shows_btn.clicked.connect(self.open_show_manager)

        bookings_btn = QPushButton("📋 Bookings & Payments")
        bookings_btn.setFixedHeight(50)
        bookings_btn.clicked.connect(self.open_bookings_payments)

        logout_btn = QPushButton("🚪 Logout")
        logout_btn.setFixedHeight(50)
        logout_btn.clicked.connect(self.logout)

        layout.addWidget(title)
        layout.addWidget(welcome)
        layout.addSpacing(25)
        layout.addWidget(movies_btn)
        layout.addWidget(shows_btn)
        layout.addWidget(bookings_btn)
        layout.addWidget(logout_btn)

        self.setLayout(layout)

    def logout(self):

        from views.login import LoginWindow

        self.login = LoginWindow()
        self.login.show()

        self.close()

    def open_movie_manager(self):

        from views.movie_manager import MovieManager

        self.movie_manager = MovieManager(self.admin)
        self.movie_manager.show()

    def open_show_manager(self):

        from views.show_manager import ShowManager

        self.show_manager = ShowManager(self.admin)
        self.show_manager.show()

    def open_bookings_payments(self):

        from views.admin_bookings_payments import AdminBookingsPayments

        self.bookings_payments = AdminBookingsPayments(self.admin)
        self.bookings_payments.show()
