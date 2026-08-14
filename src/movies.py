from db import get_connection


def get_all_movies():
    """
    Returns all movies from the database.
    """

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            query = """
                SELECT
                    movie_id,
                    title,
                    genre,
                    language,
                    duration,
                    rating,
                    release_date,
                    description
                FROM movies
                ORDER BY title
            """

            cursor.execute(query)

            return cursor.fetchall()

    finally:
        connection.close()


def get_movie_by_id(movie_id):
    """
    Returns a single movie using its movie_id.
    """

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            query = """
                SELECT
                    movie_id,
                    title,
                    genre,
                    language,
                    duration,
                    rating,
                    release_date,
                    description
                FROM movies
                WHERE movie_id = %s
            """

            cursor.execute(query, (movie_id,))

            return cursor.fetchone()

    finally:
        connection.close()


def search_movies(search_term):
    """
    Searches movies by title, genre, or language.
    """

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            search_pattern = f"%{search_term}%"

            query = """
                SELECT
                    movie_id,
                    title,
                    genre,
                    language,
                    duration,
                    rating,
                    release_date,
                    description
                FROM movies
                WHERE title LIKE %s
                   OR genre LIKE %s
                   OR language LIKE %s
                ORDER BY title
            """

            cursor.execute(
                query,
                (
                    search_pattern,
                    search_pattern,
                    search_pattern
                )
            )

            return cursor.fetchall()

    finally:
        connection.close()


def add_movie(
    title,
    genre,
    language,
    duration,
    rating,
    release_date,
    description
):
    """
    Adds a new movie to the database.
    """

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            query = """
                INSERT INTO movies
                (
                    title,
                    genre,
                    language,
                    duration,
                    rating,
                    release_date,
                    description
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            cursor.execute(
                query,
                (
                    title,
                    genre,
                    language,
                    duration,
                    rating,
                    release_date,
                    description
                )
            )

            connection.commit()

            return cursor.lastrowid

    finally:
        connection.close()


def update_movie(
    movie_id,
    title,
    genre,
    language,
    duration,
    rating,
    release_date,
    description
):
    """
    Updates an existing movie.
    """

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            query = """
                UPDATE movies
                SET
                    title = %s,
                    genre = %s,
                    language = %s,
                    duration = %s,
                    rating = %s,
                    release_date = %s,
                    description = %s
                WHERE movie_id = %s
            """

            cursor.execute(
                query,
                (
                    title,
                    genre,
                    language,
                    duration,
                    rating,
                    release_date,
                    description,
                    movie_id
                )
            )

            connection.commit()

            return cursor.rowcount > 0

    finally:
        connection.close()


def delete_movie(movie_id):
    """
    Deletes a movie using its movie_id.
    """

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            query = """
                DELETE FROM movies
                WHERE movie_id = %s
            """

            cursor.execute(query, (movie_id,))

            connection.commit()

            return cursor.rowcount > 0

    finally:
        connection.close()