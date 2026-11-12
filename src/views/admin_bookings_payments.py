
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QMessageBox,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from booking import get_all_bookings_and_payments


class AdminBookingsPayments(QWidget):

    def __init__(self, admin):
        super().__init__()

        self.admin = admin

        self.setWindowTitle("Admin - Bookings & Payments")
        self.resize(1400, 750)

        self.setup_ui()
        self.load_bookings()

    def setup_ui(self):

        layout = QVBoxLayout()
        layout.setSpacing(15)

        title = QLabel("📋 Bookings & Payments")
        title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        subtitle = QLabel(
            "View all customer bookings and their payment details"
        )
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.summary_label = QLabel("Loading bookings...")
        self.summary_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.summary_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.booking_table = QTableWidget()
        self.booking_table.setColumnCount(13)

        self.booking_table.setHorizontalHeaderLabels([
            "Booking ID",
            "Customer",
            "Email",
            "Movie",
            "Hall",
            "Show Date",
            "Show Time",
            "Seats",
            "Total Amount",
            "Payment Status",
            "Payment Mode",
            "Transaction ID",
            "Payment Date",
        ])

        self.booking_table.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )

        self.booking_table.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )

        self.booking_table.setSelectionMode(
            QTableWidget.SelectionMode.SingleSelection
        )

        self.booking_table.setAlternatingRowColors(True)

        self.booking_table.setWordWrap(False)

        header = self.booking_table.horizontalHeader()
        header.setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents
        )

        self.booking_table.verticalHeader().setVisible(False)

        refresh_button = QPushButton("🔄 Refresh")
        refresh_button.setFixedHeight(40)
        refresh_button.clicked.connect(self.load_bookings)

        close_button = QPushButton("← Back")
        close_button.setFixedHeight(40)
        close_button.clicked.connect(self.close)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(close_button)
        buttons_layout.addWidget(refresh_button)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(self.summary_label)
        layout.addWidget(self.booking_table)
        layout.addLayout(buttons_layout)

        self.setLayout(layout)

    def load_bookings(self):

        try:
            bookings = get_all_bookings_and_payments()

            self.booking_table.setRowCount(0)

            self.summary_label.setText(
                f"Total Bookings: {len(bookings)}"
            )

            for row, booking in enumerate(bookings):

                self.booking_table.insertRow(row)

                values = [
                    booking["booking_id"],
                    booking["customer_name"],
                    booking["customer_email"],
                    booking["movie_title"],
                    booking["hall_name"],
                    booking["show_date"],
                    booking["show_time"],
                    booking["seat_numbers"],
                    f"₹{float(booking['total_amount']):.2f}",
                    booking["payment_status"],
                    booking["payment_mode"] or "Not Available",
                    booking["transaction_id"] or "Not Available",
                    booking["payment_date"] or "Not Available",
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

            if not bookings:
                self.summary_label.setText(
                    "No bookings have been made yet."
                )

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                f"Could not load bookings and payments:\n\n{str(e)}"
            )
