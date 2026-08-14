from db import get_connection


def login(email, password, role):

    connection = get_connection()
    cursor = connection.cursor()

    if role == "User":

        query = """
        SELECT
            user_id AS id,
            name,
            email,
            phone,
            password,
            join_date
        FROM `user`
        WHERE email = %s AND password = %s
        """

    else:

        query = """
        SELECT
            admin_id AS id,
            username AS name,
            email,
            password
        FROM Admins
        WHERE email = %s AND password = %s
        """

    cursor.execute(query, (email, password))

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    return user