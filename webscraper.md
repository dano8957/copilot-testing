

Workspace: Here is the functional documentation for the file 

webscraper.py

:

### 

webscraper.py



This module implements a web scraper that fetches data from specified endpoints, saves the data to a SQLite database, and provides a REST API to interact with the data.

#### Imports
- 

threading

: Provides support for threading.
- 

requests

: Allows sending HTTP requests.
- 

bs4 (BeautifulSoup)

: Parses HTML and XML documents.
- 

sqlite3

: Provides a SQL interface for SQLite databases.
- 

flask (Flask, jsonify, request)

: Implements a micro web framework.
- 

logging

: Provides a flexible framework for emitting log messages.
- 

asyncio

: Supports asynchronous I/O.
- 

aiohttp

: Provides asynchronous HTTP client/server framework.

#### Constants
- 

DATABASE

: The name of the SQLite database file (`'scraper.db'`).

#### Functions

##### 

init_db()


Initializes the SQLite database by creating the `data` table if it does not exist.

```python
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            url TEXT
        )
    ''')
    conn.commit()
    conn.close()
```

#### Classes

##### 

WebScraper


A class that handles web scraping and saving data to the database.

###### 

__init__(self, base_url, endpoints)


Initializes the 

WebScraper

 instance with a base URL and a list of endpoints.

###### 

async fetch_page(self, session, url)


Fetches the content of a web page asynchronously.

###### 

async scrape(self, endpoint)


Scrapes data from a specific endpoint and stores the results.

###### 

run(self)


Runs the scraper to fetch data from all endpoints.

###### 

save_to_db(self)


Saves the scraped data to the SQLite database.

```python
class WebScraper:
    def __init__(self, base_url, endpoints):
        self.base_url = base_url
        self.endpoints = endpoints
        self.lock = threading.Lock()
        self.results = []

    async def fetch_page(self, session, url):
        async with session.get(url) as response:
            return await response.text()

    async def scrape(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        async with aiohttp.ClientSession() as session:
            content = await self.fetch_page(session, url)
            soup = BeautifulSoup(content, 'html.parser')
            titles = [tag.get_text() for tag in soup.find_all('h1')]
            with self.lock:
                for title in titles:
                    self.results.append((title, url))

    def run(self):
        loop = asyncio.get_event_loop()
        tasks = [self.scrape(endpoint) for endpoint in self.endpoints]
        loop.run_until_complete(asyncio.gather(*tasks))

    def save_to_db(self):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        with self.lock:
            cursor.executemany('INSERT INTO data (title, url) VALUES (?, ?)', self.results)
        conn.commit()
        conn.close()
```

#### REST API

##### 

app


A Flask application that provides REST API endpoints to interact with the data.

###### `@app.route('/data', methods=['GET'])`
Returns all data from the database as JSON.

###### `@app.route('/data', methods=['POST'])`
Adds new data to the database from a JSON request.

```python
app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM data')
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

@app.route('/data', methods=['POST'])
def add_data():
    title = request.json['title']
    url = request.json['url']
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO data (title, url) VALUES (?, ?)', (title, url))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'}), 201
```

#### Main Execution
Initializes the database, runs the web scraper, saves the data, and starts the Flask application.

```python
if __name__ == "__main__":
    init_db()
    
    # Example usage of the scraper
    base_url = "https://example.com"
    endpoints = ["page1", "page2", "page3"]
    scraper = WebScraper(base_url, endpoints)
    
    logging.info("Starting web scraping...")
    scraper.run()
    logging.info("Saving data to database...")
    scraper.save_to_db()
    logging.info("Data saved successfully.")
    
    # Start the REST API
    app.run(debug=True)
```