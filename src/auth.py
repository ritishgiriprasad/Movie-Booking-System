from db import get_connection


def login(email, password, role):
    connection = get_connection()
    cursor = connection.cursor()

    if role == "User":
        query = """
        SELECT *
        FROM Users
        WHERE email=%s AND password=%s
        """
    else:
        query = """
        SELECT *
        FROM Admins
        WHERE email=%s AND password=%s
        """

    cursor.execute(query, (email, password))
    user = cursor.fetchone()

    cursor.close()
    connection.close()

    return user