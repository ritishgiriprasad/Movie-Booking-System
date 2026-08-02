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

        shows_btn = QPushButton("🎞 Manage Shows")
        shows_btn.setFixedHeight(50)

        bookings_btn = QPushButton("📋 View Bookings")
        bookings_btn.setFixedHeight(50)

        payments_btn = QPushButton("💳 Payments")
        payments_btn.setFixedHeight(50)

        logout_btn = QPushButton("🚪 Logout")
        logout_btn.setFixedHeight(50)
        logout_btn.clicked.connect(self.logout)

        layout.addWidget(title)
        layout.addWidget(welcome)
        layout.addSpacing(25)
        layout.addWidget(movies_btn)
        layout.addWidget(shows_btn)
        layout.addWidget(bookings_btn)
        layout.addWidget(payments_btn)
        layout.addWidget(logout_btn)

        self.setLayout(layout)

    def logout(self):

        from views.login import LoginWindow

        self.login = LoginWindow()
        self.login.show()

        self.close()