from db import get_connection


def main():
    try:
        connection = get_connection()
        print("Database Connected Successfully!")
        connection.close()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()