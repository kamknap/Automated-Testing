import unittest
from db_manager import UserDatabase
from psycopg2 import Error

class TestDatabaseManagement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db = UserDatabase(
            db_name="test_db",
            user="postgres",
            password="admin",
            host="localhost",
            port=5432
        )

    @classmethod
    def tearDownClass(cls):
        cls.db.close_connection()

    def setUp(self):
        self.db.cursor.execute("DELETE FROM users")
        self.db.connection.commit()

    def test_add_user(self):
        result = self.db.add_user("TestUser", "Test@example.com")
        self.assertEqual(result, "User added successfully.")

    def test_get_user(self):
        self.db.add_user("TestUser", "Test@example.com")
        result = self.db.get_user("TestUser")
        expected_result = (result[0], "TestUser", "Test@example.com")
        self.assertEqual(result, expected_result)

    def test_delete_user(self):
        self.db.add_user("TestUser", "Test@example.com")
        self.db.delete_user("TestUser")
        result = self.db.get_user("TestUser")
        self.assertIsNone(result)

    def test_add_user_duplicate_email(self):
        self.db.add_user("TestUser", "Test@example.com")
        with self.assertRaises(Error):
            self.db.add_user("AnotherUser", "Test@example.com") 

    def test_add_user_wrong_email(self):
        with self.assertRaises(Error):
            self.db.add_user("TestUser", "Test@examplecom")

    def test_get_not_existing_user(self):
        with self.assertRaises(Error):
            self.db.get_user("NotExistingUser")

            



    