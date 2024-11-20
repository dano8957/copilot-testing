import unittest
import sqlite3
import os
from webscraper import WebScraper, init_db, app

class TestWebScraper(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        init_db()

    def setUp(self):
        self.base_url = "https://example.com"
        self.endpoints = ["page1", "page2", "page3"]
        self.scraper = WebScraper(self.base_url, self.endpoints)
        self.db_path = 'scraper.db'

    def tearDown(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_scraper_initialization(self):
        self.assertEqual(self.scraper.base_url, self.base_url)
        self.assertEqual(self.scraper.endpoints, self.endpoints)
        self.assertEqual(self.scraper.results, [])

    def test_scraper_run(self):
        self.scraper.run()
        self.assertGreater(len(self.scraper.results), 0)

    def test_save_to_db(self):
        self.scraper.results = [("Test Title", "https://example.com/page1")]
        self.scraper.save_to_db()
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM data')
        rows = cursor.fetchall()
        conn.close()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][1], "Test Title")
        self.assertEqual(rows[0][2], "https://example.com/page1")

class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        init_db()
        cls.app = app.test_client()
        cls.app.testing = True

    def tearDown(self):
        if os.path.exists('scraper.db'):
            os.remove('scraper.db')

    def test_get_data(self):
        response = self.app.get('/data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_add_data(self):
        response = self.app.post('/data', json={'title': 'Test Title', 'url': 'https://example.com'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['status'], 'success')

        response = self.app.get('/data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)
        self.assertEqual(response.json[0][1], 'Test Title')
        self.assertEqual(response.json[0][2], 'https://example.com')

if __name__ == '__main__':
    unittest.main()