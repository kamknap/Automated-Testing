import psycopg2

class UserDatabase:
    def __init__(self, db_name, user, password, host, port):
        self.connection = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor = self.connection.cursor()

    def add_user(self, username, email):
        try:
            self.cursor.execute("INSERT INTO users (username, email) VALUES (%s, %s)", (username, email))
            self.connection.commit()
            return "User added successfully."
        except psycopg2.Error as e:
            return f"Error: {e}"

    def get_user(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        result = self.cursor.fetchone()
        return result

    def delete_user(self, username):
        self.cursor.execute("DELETE FROM users WHERE username = %s", (username,))
        self.connection.commit()
        return "User deleted successfully."

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
