
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QHeaderView,
    QDialog,
    QFormLayout,
    QComboBox,
    QDateEdit,
    QTimeEdit,
    QDoubleSpinBox,
    QSpinBox,
)
from PyQt6.QtCore import Qt, QDate, QTime
from PyQt6.QtGui import QFont

from shows import (
    get_all_shows,
    get_all_movies_for_shows,
    get_all_halls,
    add_show,
    update_show,
    delete_show,
)


class ShowManager(QWidget):
    def __init__(self, admin):
        super().__init__()

        self.admin = admin
        self.setWindowTitle("Movie Booking System - Manage Shows")
        self.resize(1100, 650)

        self.setup_ui()
        self.load_shows()

    def setup_ui(self):
        layout = QVBoxLayout()

        title = QLabel("🎞 Manage Shows")
        title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(title)

        # Search bar
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText(
            "Search by movie, hall, date, or show ID..."
        )
        self.search_input.textChanged.connect(self.search_shows)

        layout.addWidget(self.search_input)

        # Show table
        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels([
            "Show ID",
            "Movie",
            "Hall",
            "Date",
            "Time",
            "Price",
            "Available Seats",
        ])

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        layout.addWidget(self.table)

        # Buttons
        button_layout = QHBoxLayout()

        add_btn = QPushButton("➕ Add Show")
        edit_btn = QPushButton("✏️ Edit Show")
        delete_btn = QPushButton("🗑 Delete Show")
        refresh_btn = QPushButton("🔄 Refresh")
        back_btn = QPushButton("⬅ Back")

        for button in (
            add_btn,
            edit_btn,
            delete_btn,
            refresh_btn,
            back_btn,
        ):
            button.setFixedHeight(45)

        add_btn.clicked.connect(self.add_show_dialog)
        edit_btn.clicked.connect(self.edit_show_dialog)
        delete_btn.clicked.connect(self.delete_selected_show)
        refresh_btn.clicked.connect(self.load_shows)
        back_btn.clicked.connect(self.close)

        button_layout.addWidget(add_btn)
        button_layout.addWidget(edit_btn)
        button_layout.addWidget(delete_btn)
        button_layout.addWidget(refresh_btn)
        button_layout.addWidget(back_btn)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def load_shows(self):
        try:
            shows = get_all_shows()

            self.table.setRowCount(len(shows))

            for row, show in enumerate(shows):
                show_time = show["show_time"]

                # MySQL TIME values may be returned as timedelta objects.
                total_seconds = int(show_time.total_seconds())
                hours = total_seconds // 3600
                minutes = (total_seconds % 3600) // 60
                formatted_time = f"{hours:02}:{minutes:02}"

                values = [
                    show["show_id"],
                    show["movie_title"],
                    show["hall_name"],
                    show["show_date"].strftime("%Y-%m-%d"),
                    formatted_time,
                    str(show["price"]),
                    show["available_seats"],
                ]

                for column, value in enumerate(values):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(
                        Qt.AlignmentFlag.AlignCenter
                    )
                    self.table.setItem(row, column, item)

        except Exception as error:
            QMessageBox.critical(
                self,
                "Error",
                f"Could not load shows:\n{error}",
            )
    def search_shows(self, text):
        search_text = text.strip().lower()

        for row in range(self.table.rowCount()):
            match_found = False

            for column in range(self.table.columnCount()):
                item = self.table.item(row, column)

                if item and search_text in item.text().lower():
                    match_found = True
                    break

            self.table.setRowHidden(row, not match_found)

    def get_selected_show(self):
        selected_rows = self.table.selectionModel().selectedRows()

        if not selected_rows:
            QMessageBox.warning(
                self,
                "No Selection",
                "Please select a show first.",
            )
            return None

        row = selected_rows[0].row()

        show_id = int(
            self.table.item(row, 0).text()
        )

        shows = get_all_shows()

        for show in shows:
            if show["show_id"] == show_id:
                return show

        return None

    def add_show_dialog(self):
        dialog = ShowDialog(self)

        if dialog.exec():
            data = dialog.get_data()

            try:
                add_show(
                    data["movie_id"],
                    data["hall_id"],
                    data["show_date"],
                    data["show_time"],
                    data["price"],
                    data["available_seats"],
                )

                QMessageBox.information(
                    self,
                    "Success",
                    "Show added successfully!",
                )

                self.load_shows()

            except Exception as error:
                QMessageBox.critical(
                    self,
                    "Error",
                    f"Could not add show:\n{error}",
                )

    def edit_show_dialog(self):
        show = self.get_selected_show()

        if show is None:
            return

        dialog = ShowDialog(self, show)

        if dialog.exec():
            data = dialog.get_data()

            try:
                update_show(
                    show["show_id"],
                    data["movie_id"],
                    data["hall_id"],
                    data["show_date"],
                    data["show_time"],
                    data["price"],
                    data["available_seats"],
                )

                QMessageBox.information(
                    self,
                    "Success",
                    "Show updated successfully!",
                )

                self.load_shows()

            except Exception as error:
                QMessageBox.critical(
                    self,
                    "Error",
                    f"Could not update show:\n{error}",
                )

    def delete_selected_show(self):
        show = self.get_selected_show()

        if show is None:
            return

        confirmation = QMessageBox.question(
            self,
            "Confirm Delete",
            f"Delete the show for {show['movie_title']}?",
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No,
        )

        if confirmation == QMessageBox.StandardButton.Yes:
            try:
                delete_show(show["show_id"])

                QMessageBox.information(
                    self,
                    "Success",
                    "Show deleted successfully!",
                )

                self.load_shows()

            except Exception as error:
                QMessageBox.critical(
                    self,
                    "Error",
                    "Could not delete show.\n"
                    "It may have existing bookings.\n\n"
                    f"{error}",
                )


class ShowDialog(QDialog):
    def __init__(self, parent=None, show=None):
        super().__init__(parent)

        self.show_data = show

        self.setWindowTitle(
            "Edit Show" if show else "Add Show"
        )
        self.setMinimumWidth(400)

        self.setup_ui()

        if show:
            self.populate_fields()

    def setup_ui(self):
        layout = QVBoxLayout()
        form = QFormLayout()

        # Movie dropdown
        self.movie_combo = QComboBox()

        self.movies = get_all_movies_for_shows()

        for movie in self.movies:
            self.movie_combo.addItem(
                movie["title"],
                movie["movie_id"],
            )

        # Hall dropdown
        self.hall_combo = QComboBox()

        self.halls = get_all_halls()

        for hall in self.halls:
            self.hall_combo.addItem(
                hall["hall_name"],
                hall["hall_id"],
            )

        # Date
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDisplayFormat("yyyy-MM-dd")
        self.date_edit.setDate(QDate.currentDate())

        # Time
        self.time_edit = QTimeEdit()
        self.time_edit.setDisplayFormat("HH:mm")
        self.time_edit.setTime(QTime(10, 0))

        # Ticket price
        self.price_spin = QDoubleSpinBox()
        self.price_spin.setRange(0, 10000)
        self.price_spin.setDecimals(2)
        self.price_spin.setPrefix("₹ ")

        # Available seats
        self.seats_spin = QSpinBox()
        self.seats_spin.setRange(0, 1000)

        form.addRow("Movie:", self.movie_combo)
        form.addRow("Hall:", self.hall_combo)
        form.addRow("Date:", self.date_edit)
        form.addRow("Time:", self.time_edit)
        form.addRow("Ticket Price:", self.price_spin)
        form.addRow("Available Seats:", self.seats_spin)

        layout.addLayout(form)

        # Buttons
        button_layout = QHBoxLayout()

        save_btn = QPushButton("Save")
        cancel_btn = QPushButton("Cancel")

        save_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)

        button_layout.addWidget(save_btn)
        button_layout.addWidget(cancel_btn)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def populate_fields(self):
        show = self.show_data

        movie_index = self.movie_combo.findData(
            show["movie_id"]
        )
        hall_index = self.hall_combo.findData(
            show["hall_id"]
        )

        if movie_index >= 0:
            self.movie_combo.setCurrentIndex(movie_index)

        if hall_index >= 0:
            self.hall_combo.setCurrentIndex(hall_index)

        show_date = show["show_date"]

        self.date_edit.setDate(
            QDate(
                show_date.year,
                show_date.month,
                show_date.day,
            )
        )

        total_seconds = int(
            show["show_time"].total_seconds()
        )

        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60

        self.time_edit.setTime(
            QTime(hours, minutes)
        )

        self.price_spin.setValue(
            float(show["price"])
        )

        self.seats_spin.setValue(
            int(show["available_seats"])
        )

    def get_data(self):
        return {
            "movie_id": self.movie_combo.currentData(),
            "hall_id": self.hall_combo.currentData(),
            "show_date": self.date_edit.date().toString(
                "yyyy-MM-dd"
            ),
            "show_time": self.time_edit.time().toString(
                "HH:mm:ss"
            ),
            "price": self.price_spin.value(),
            "available_seats": self.seats_spin.value(),
        }
