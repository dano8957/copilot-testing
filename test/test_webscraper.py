import unittest  # Importing the unittest module for creating and running tests
import sqlite3  # Importing the sqlite3 module for interacting with SQLite databases
import os  # Importing the os module for interacting with the operating system
from webscraper import WebScraper, init_db, app  # Importing necessary components from the webscraper module

# Define a test case for the WebScraper class
class TestWebScraper(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize the database before any tests are run
        init_db()

    def setUp(self):
        # Set up the base URL and endpoints for the scraper
        self.base_url = "https://example.com"
        self.endpoints = ["page1", "page2", "page3"]
        # Create an instance of the WebScraper class
        self.scraper = WebScraper(self.base_url, self.endpoints)
        # Define the path to the database file
        self.db_path = 'scraper.db'

    def tearDown(self):
        # Remove the database file after each test if it exists
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_scraper_initialization(self):
        # Test that the scraper is initialized with the correct base URL, endpoints, and empty results list
        self.assertEqual(self.scraper.base_url, self.base_url)
        self.assertEqual(self.scraper.endpoints, self.endpoints)
        self.assertEqual(self.scraper.results, [])

    def test_scraper_run(self):
        # Test that the scraper's run method populates the results list
        self.scraper.run()
        self.assertGreater(len(self.scraper.results), 0)

    def test_save_to_db(self):
        # Test that the scraper can save results to the database
        self.scraper.results = [("Test Title", "https://example.com/page1")]
        self.scraper.save_to_db()
        # Connect to the database and fetch the data
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM data')
        rows = cursor.fetchall()
        conn.close()
        # Check that the data was saved correctly
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][1], "Test Title")
        self.assertEqual(rows[0][2], "https://example.com/page1")

# Define a test case for the API
class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize the database and set up the test client for the API
        init_db()
        cls.app = app.test_client()
        cls.app.testing = True

    def tearDown(self):
        # Remove the database file after each test if it exists
        if os.path.exists('scraper.db'):
            os.remove('scraper.db')

    def test_get_data(self):
        # Test that the GET /data endpoint returns an empty list initially
        response = self.app.get('/data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_add_data(self):
        # Test that the POST /data endpoint adds data correctly
        response = self.app.post('/data', json={'title': 'Test Title', 'url': 'https://example.com'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['status'], 'success')

        # Test that the GET /data endpoint returns the added data
        response = self.app.get('/data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)
        self.assertEqual(response.json[0][1], 'Test Title')
        self.assertEqual(response.json[0][2], 'https://example.com')

# Run the tests if the script is executed directly
if __name__ == '__main__':
    unittest.main()