
from db import get_connection


def get_all_shows():
    """Return all shows with their movie and hall names."""

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    s.show_id,
                    s.movie_id,
                    s.hall_id,
                    m.title AS movie_title,
                    h.hall_name,
                    s.show_date,
                    s.show_time,
                    s.price,
                    s.available_seats
                FROM Shows s
                LEFT JOIN Movies m ON s.movie_id = m.movie_id
                LEFT JOIN Halls h ON s.hall_id = h.hall_id
                ORDER BY s.show_date, s.show_time
            """

            cursor.execute(query)
            return cursor.fetchall()

    finally:
        connection.close()


def get_all_movies_for_shows():
    """Return movie IDs and titles for the movie dropdown."""

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT movie_id, title
                FROM Movies
                ORDER BY title
            """)

            return cursor.fetchall()

    finally:
        connection.close()


def get_all_halls():
    """Return hall IDs, names, and seat counts."""

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT hall_id, hall_name, total_seats
                FROM Halls
                ORDER BY hall_name
            """)

            return cursor.fetchall()

    finally:
        connection.close()


def add_show(
    movie_id,
    hall_id,
    show_date,
    show_time,
    price,
    available_seats
):
    """Add a new show."""

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            query = """
                INSERT INTO Shows (
                    movie_id,
                    hall_id,
                    show_date,
                    show_time,
                    price,
                    available_seats
                )
                VALUES (%s, %s, %s, %s, %s, %s)
            """

            cursor.execute(
                query,
                (
                    movie_id,
                    hall_id,
                    show_date,
                    show_time,
                    price,
                    available_seats
                )
            )

            connection.commit()
            return cursor.lastrowid

    finally:
        connection.close()


def update_show(
    show_id,
    movie_id,
    hall_id,
    show_date,
    show_time,
    price,
    available_seats
):
    """Update an existing show."""

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            query = """
                UPDATE Shows
                SET
                    movie_id = %s,
                    hall_id = %s,
                    show_date = %s,
                    show_time = %s,
                    price = %s,
                    available_seats = %s
                WHERE show_id = %s
            """

            cursor.execute(
                query,
                (
                    movie_id,
                    hall_id,
                    show_date,
                    show_time,
                    price,
                    available_seats,
                    show_id
                )
            )

            connection.commit()
            return cursor.rowcount > 0

    finally:
        connection.close()


def delete_show(show_id):
    """Delete a show."""

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM Shows WHERE show_id = %s",
                (show_id,)
            )

            connection.commit()
            return cursor.rowcount > 0

    finally:
        connection.close()
