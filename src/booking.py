
from datetime import datetime

from db import get_connection


def get_booked_seats(show_id):
    """Return seat numbers already booked for a show."""

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            query = """
                SELECT seat_numbers
                FROM Booking
                WHERE show_id = %s
                  AND payment_status = 'COMPLETED'
            """

            cursor.execute(query, (show_id,))
            bookings = cursor.fetchall()

            booked_seats = set()

            for booking in bookings:
                seat_numbers = booking["seat_numbers"]

                if seat_numbers:
                    seats = seat_numbers.split(",")

                    for seat in seats:
                        booked_seats.add(seat.strip())

            return booked_seats

    finally:
        connection.close()


def create_booking(user_id, show_id, seat_numbers, total_amount):
    """Save a completed booking and its simulated payment."""

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            # Create the booking.
            cursor.execute(
                """
                INSERT INTO Booking (
                    user_id,
                    show_id,
                    seat_numbers,
                    booking_date,
                    payment_status,
                    total_amount
                )
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    user_id,
                    show_id,
                    ", ".join(sorted(seat_numbers)),
                    datetime.now(),
                    "COMPLETED",
                    total_amount,
                ),
            )

            booking_id = cursor.lastrowid

            # Create the corresponding payment record.
            cursor.execute(
                """
                INSERT INTO Payments (
                    booking_id,
                    payment_mode,
                    transaction_id,
                    payment_date
                )
                VALUES (%s, %s, %s, %s)
                """,
                (
                    booking_id,
                    "Demo Payment",
                    f"DEMO-{booking_id}",
                    datetime.now(),
                ),
            )

            connection.commit()

            return booking_id

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()

def get_user_bookings(user_id):
    """Return all bookings belonging to a specific user."""

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    b.booking_id,
                    m.title AS movie_title,
                    h.hall_name,
                    s.show_date,
                    s.show_time,
                    b.seat_numbers,
                    b.total_amount,
                    b.payment_status,
                    b.booking_date
                FROM Booking b
                JOIN Shows s ON b.show_id = s.show_id
                LEFT JOIN Movies m ON s.movie_id = m.movie_id
                LEFT JOIN Halls h ON s.hall_id = h.hall_id
                WHERE b.user_id = %s
                ORDER BY b.booking_date DESC
            """

            cursor.execute(query, (user_id,))
            return cursor.fetchall()

    finally:
        connection.close()

def get_all_bookings_and_payments():
    """Return all bookings with customer, show and payment details."""

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    b.booking_id,
                    u.name AS customer_name,
                    u.email AS customer_email,
                    m.title AS movie_title,
                    h.hall_name,
                    s.show_date,
                    s.show_time,
                    b.seat_numbers,
                    b.total_amount,
                    b.payment_status,
                    p.payment_mode,
                    p.transaction_id,
                    p.payment_date
                FROM Booking b
                JOIN `user` u ON b.user_id = u.user_id
                JOIN Shows s ON b.show_id = s.show_id
                LEFT JOIN Movies m ON s.movie_id = m.movie_id
                LEFT JOIN Halls h ON s.hall_id = h.hall_id
                LEFT JOIN Payments p ON b.booking_id = p.booking_id
                ORDER BY b.booking_date DESC
            """

            cursor.execute(query)
            return cursor.fetchall()

    finally:
        connection.close()
