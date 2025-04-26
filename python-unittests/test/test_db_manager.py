import unittest
from db_manager import UserDatabase

class TestDatabaseManagement(unittest.TestCase):

    def test_connection(self):
        try:
            db = UserDatabase(
                db_name="test_db",
                user="postgres",
                password="admin",
                host="localhost",
                port=5432   
            )
            self.assertIsNotNone(db.connection)
            db.close_connection()
        except Exception as e:
            self.fail(f"Connection to db failed: {e}")
    