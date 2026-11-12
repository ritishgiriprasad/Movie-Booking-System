
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QMessageBox,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from booking import get_booked_seats, create_booking


class SeatSelection(QWidget):

    def __init__(self, user, show):
        super().__init__()

        self.user = user
        self.selected_show = show

        self.selected_seats = set()
        self.booked_seats = get_booked_seats(show["show_id"])

        self.seat_price = float(show["price"])

        self.setWindowTitle("Select Seats")
        self.resize(850, 650)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)

        title = QLabel(f"🎬 {self.selected_show['movie_title']}")
        title.setFont(QFont("Arial", 22, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        hall_label = QLabel(
            f"{self.selected_show['hall_name']}  |  "
            f"₹{self.seat_price:.2f} per ticket"
        )
        hall_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        screen_label = QLabel("──────────── SCREEN ────────────")
        screen_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        screen_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))

        layout.addWidget(title)
        layout.addWidget(hall_label)
        layout.addWidget(screen_label)

        self.seat_grid = QGridLayout()
        self.seat_grid.setSpacing(8)

        total_seats = self.selected_show.get("total_seats", 120)

        # Generate rows of 10 seats.
        rows = (total_seats + 9) // 10

        for row_index in range(rows):
            row_letter = chr(ord("A") + row_index)

            for seat_number in range(1, 11):
                seat_index = row_index * 10 + seat_number

                if seat_index > total_seats:
                    break

                seat_id = f"{row_letter}{seat_number}"

                seat_button = QPushButton(seat_id)
                seat_button.setFixedSize(55, 35)

                if seat_id in self.booked_seats:
                    seat_button.setEnabled(False)
                    seat_button.setStyleSheet(
                        "background-color: #777777; color: white;"
                    )
                else:
                    seat_button.setCheckable(True)
                    seat_button.setStyleSheet(
                        "background-color: #2E8B57; color: white;"
                    )

                    seat_button.clicked.connect(
                        lambda checked, seat=seat_id:
                            self.toggle_seat(seat)
                    )

                self.seat_grid.addWidget(
                    seat_button,
                    row_index,
                    seat_number - 1
                )

        layout.addLayout(self.seat_grid)

        legend = QLabel(
            "🟩 Available     ⬜ Selected     ⬛ Booked"
        )
        legend.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.total_label = QLabel("Selected: None | Total: ₹0.00")
        self.total_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.total_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))

        continue_button = QPushButton("Continue")
        continue_button.clicked.connect(self.continue_booking)

        back_button = QPushButton("← Back")
        back_button.clicked.connect(self.close)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(back_button)
        buttons_layout.addWidget(continue_button)

        layout.addWidget(legend)
        layout.addWidget(self.total_label)
        layout.addLayout(buttons_layout)

        self.setLayout(layout)

    def toggle_seat(self, seat_id):
        if seat_id in self.selected_seats:
            self.selected_seats.remove(seat_id)
        else:
            self.selected_seats.add(seat_id)

        self.update_total()

    def update_total(self):
        total = len(self.selected_seats) * self.seat_price

        selected_text = (
            ", ".join(sorted(self.selected_seats))
            if self.selected_seats
            else "None"
        )

        self.total_label.setText(
            f"Selected: {selected_text} | Total: ₹{total:.2f}"
        )

    def continue_booking(self):
        if not self.selected_seats:
            QMessageBox.warning(
                self,
                "No Seats Selected",
                "Please select at least one seat."
            )
            return

        total_amount = len(self.selected_seats) * self.seat_price
        seats_text = ", ".join(sorted(self.selected_seats))

        confirmation = QMessageBox.question(
            self,
            "Confirm Booking",
            f"Movie: {self.selected_show['movie_title']}\n"
            f"Hall: {self.selected_show['hall_name']}\n"
            f"Seats: {seats_text}\n"
            f"Total Amount: ₹{total_amount:.2f}\n\n"
            f"Confirm your booking?",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if confirmation != QMessageBox.StandardButton.Yes:
            return

        try:
            booking_id = create_booking(
            self.user["id"],
            self.selected_show["show_id"],
            self.selected_seats,
            total_amount
        )

            QMessageBox.information(
                self,
                "Booking Successful",
                f"Your booking has been confirmed!\n\n"
                f"Booking ID: {booking_id}\n"
                f"Seats: {seats_text}\n"
                f"Total Paid: ₹{total_amount:.2f}\n\n"
                f"Payment: Demo Payment"
            )

            self.close()

        except Exception as e:
            QMessageBox.critical(
                self,
                "Booking Failed",
                f"Something went wrong while booking your seats:\n\n{str(e)}"
            )
