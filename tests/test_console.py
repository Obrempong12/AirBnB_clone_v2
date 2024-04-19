import sqlite3
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO

class TestHBNBCommand(unittest.TestCase):
    """Unittests for testing the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        """Set up the test environment."""
        # Create an in-memory SQLite database
        cls.conn = sqlite3.connect(":memory:")
        cls.cursor = cls.conn.cursor()
        # Create tables as necessary
        cls.cursor.execute("CREATE TABLE IF NOT EXISTS states (id INTEGER PRIMARY KEY, name TEXT);")
        # Initialize the console instance
        cls.HBNB = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """Clean up after the tests."""
        cls.conn.close()

    def setUp(self):
        """Set up each test case."""
        # Clear any existing data in the tables
        self.cursor.execute("DELETE FROM states;")
        self.conn.commit()

    def test_create_command(self):
        """Test the create command."""
        # Get the initial count of records in the states table
        initial_count = self.get_record_count()

        # Execute the create command
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create State name='California'")

        # Get the final count of records in the states table
        final_count = self.get_record_count()

        # Assert that the final count is greater than the initial count by one
        self.assertEqual(final_count, initial_count + 1)

    def get_record_count(self):
        """Get the count of records in the states table."""
        self.cursor.execute("SELECT COUNT(*) FROM states;")
        return self.cursor.fetchone()[0]

if __name__ == "__main__":
    unittest.main()
