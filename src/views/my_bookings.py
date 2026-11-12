
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QHeaderView,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from booking import get_user_bookings


class MyBookings(QWidget):

    def __init__(self, user):
        super().__init__()

        self.user = user

        self.setWindowTitle("My Bookings")
        self.resize(1100, 650)

        self.setup_ui()
        self.load_bookings()

    def setup_ui(self):

        layout = QVBoxLayout()
        layout.setSpacing(15)

        title = QLabel("🎟 My Bookings")
        title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        subtitle = QLabel(
            f"Booking history for {self.user['name']}"
        )
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.booking_table = QTableWidget()
        self.booking_table.setColumnCount(8)

        self.booking_table.setHorizontalHeaderLabels([
            "Booking ID",
            "Movie",
            "Hall",
            "Show Date",
            "Show Time",
            "Seats",
            "Total Amount",
            "Payment Status",
        ])

        self.booking_table.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )

        self.booking_table.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )

        self.booking_table.setAlternatingRowColors(True)

        header = self.booking_table.horizontalHeader()
        header.setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents
        )

        header.setStretchLastSection(True)

        refresh_button = QPushButton("🔄 Refresh")
        refresh_button.clicked.connect(self.load_bookings)

        back_button = QPushButton("← Back to Dashboard")
        back_button.clicked.connect(self.close)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(back_button)
        buttons_layout.addWidget(refresh_button)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(self.booking_table)
        layout.addLayout(buttons_layout)

        self.setLayout(layout)

    def load_bookings(self):

        try:
            bookings = get_user_bookings(self.user["id"])

            self.booking_table.setRowCount(len(bookings))

            if not bookings:
                QMessageBox.information(
                    self,
                    "No Bookings",
                    "You haven't made any bookings yet."
                )
                return

            for row, booking in enumerate(bookings):

                values = [
                    booking["booking_id"],
                    booking["movie_title"],
                    booking["hall_name"],
                    booking["show_date"],
                    booking["show_time"],
                    booking["seat_numbers"],
                    f"₹{float(booking['total_amount']):.2f}",
                    booking["payment_status"],
                ]

                for column, value in enumerate(values):

                    item = QTableWidgetItem(str(value))

                    item.setTextAlignment(
                        Qt.AlignmentFlag.AlignCenter
                    )

                    self.booking_table.setItem(
                        row,
                        column,
                        item
                    )

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                f"Could not load your bookings:\n\n{str(e)}"
            )
