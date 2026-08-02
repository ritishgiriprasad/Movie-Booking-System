from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class UserDashboard(QWidget):

    def __init__(self, user):
        super().__init__()

        self.user = user

        self.setWindowTitle("Movie Booking System - User Dashboard")
        self.resize(1000, 600)

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(20)

        title = QLabel("🎬 Movie Booking System")
        title.setFont(QFont("Arial", 28, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        welcome = QLabel(f"Welcome, {self.user['name']}!")
        welcome.setFont(QFont("Arial", 18))
        welcome.setAlignment(Qt.AlignmentFlag.AlignCenter)

        browse_btn = QPushButton("🎥 Browse Movies")
        browse_btn.setFixedHeight(50)

        bookings_btn = QPushButton("🎟 My Bookings")
        bookings_btn.setFixedHeight(50)

        logout_btn = QPushButton("🚪 Logout")
        logout_btn.setFixedHeight(50)
        logout_btn.clicked.connect(self.logout)

        layout.addWidget(title)
        layout.addWidget(welcome)
        layout.addSpacing(25)
        layout.addWidget(browse_btn)
        layout.addWidget(bookings_btn)
        layout.addWidget(logout_btn)

        self.setLayout(layout)

    def logout(self):

        from views.login import LoginWindow

        self.login = LoginWindow()
        self.login.show()

        self.close()