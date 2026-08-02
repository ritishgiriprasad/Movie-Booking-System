from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QFrame
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMessageBox

from auth import login


class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.selected_role = "User"

        self.setWindowTitle("Movie Booking System")
        self.setFixedSize(1000, 600)

        self.setup_ui()

    def setup_ui(self):

        # ---------- Main Layout ----------

        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        # ---------- Left Panel ----------

        left_panel = QFrame()
        left_panel.setStyleSheet("""
            background-color: #1f2937;
        """)

        left_layout = QVBoxLayout()

        left_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        icon = QLabel("🎬")
        icon.setFont(QFont("Arial", 48))
        icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title = QLabel("Movie Booking System")
        title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        subtitle = QLabel("Book movies in just a few clicks.")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        left_layout.addWidget(icon)
        left_layout.addSpacing(20)
        left_layout.addWidget(title)
        left_layout.addWidget(subtitle)

        left_panel.setLayout(left_layout)

        # ---------- Right Panel ----------

        right_panel = QFrame()

        right_layout = QVBoxLayout()
        right_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        heading = QLabel("Welcome Back")
        heading.setFont(QFont("Arial", 22, QFont.Weight.Bold))

        self.email = QLineEdit()
        self.email.setPlaceholderText("Email")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        role_layout = QHBoxLayout()

        self.user_btn = QPushButton("User")
        self.admin_btn = QPushButton("Admin")

        self.user_btn.clicked.connect(self.select_user)
        self.admin_btn.clicked.connect(self.select_admin)

        self.select_user()


        role_layout.addWidget(self.user_btn)
        role_layout.addWidget(self.admin_btn)

        self.login_btn = QPushButton("Login")
        self.login_btn.clicked.connect(self.login_clicked)

        right_layout.addWidget(heading)
        right_layout.addSpacing(20)
        right_layout.addWidget(self.email)
        right_layout.addWidget(self.password)
        right_layout.addSpacing(10)
        right_layout.addLayout(role_layout)
        right_layout.addSpacing(20)
        right_layout.addWidget(self.login_btn)

        right_panel.setLayout(right_layout)

        # ---------- Add Panels ----------

        main_layout.addWidget(left_panel, 3)
        main_layout.addWidget(right_panel, 2)

        self.setStyleSheet("""
        QWidget{
            background-color:#20232A;
            color:white;
        }

        QLineEdit{
            padding:10px;
            font-size:15px;
            border:2px solid #3b82f6;
            border-radius:8px;
            background:#2b2b2b;
        }

        QPushButton{
            background:#2563eb;
            color:white;
            border:none;
            border-radius:8px;
            padding:10px;
            font-size:15px;
        }

        QPushButton:hover{
            background:#1d4ed8;
        }
        """)

    def select_user(self):
            self.selected_role = "User"

            self.user_btn.setStyleSheet("""
                background-color: #2563eb;
                color: white;
            """)

            self.admin_btn.setStyleSheet("")

    def select_admin(self):
        self.selected_role = "Admin"

        self.admin_btn.setStyleSheet("""
            background-color: #2563eb;
            color: white;
        """)

        self.user_btn.setStyleSheet("")


    def login_clicked(self):

        email = self.email.text().strip()
        password = self.password.text().strip()

        if email == "" or password == "":

            QMessageBox.warning(
                self,
                "Missing Information",
                "Please enter both email and password."
            )

            return

        user = login(email, password, self.selected_role)

        if user:

            QMessageBox.information(
                self,
                "Success",
                f"Welcome {user['name']}!"
            )

            if self.selected_role == "User":
                self.open_user_dashboard(user)

            else:
                self.open_admin_dashboard(user)

        else:

            QMessageBox.critical(
                self,
                "Login Failed",
                "Invalid email or password."
            )
    def open_user_dashboard(self, user):

        from views.user_dashboard import UserDashboard

        self.dashboard = UserDashboard(user)

        self.dashboard.show()

        self.close()


    def open_admin_dashboard(self, user):

        from views.admin_dashboard import AdminDashboard

        self.dashboard = AdminDashboard(user)

        self.dashboard.show()

        self.close()