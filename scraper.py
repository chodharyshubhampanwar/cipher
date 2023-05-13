import requests
from bs4 import BeautifulSoup
import json

# URL of the page to scrape
url = "https://www.imdb.com/chart/top/"

# Send a GET request to the URL and get the response
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the table rows in the page's main table
rows = soup.select("table.chart > tbody > tr")

# Initialize an empty list to store the scraped data
movies = []

# Loop through each table row and extract the movie data
for row in rows:
    cells = row.find_all("td")
    rank = cells[0].text.strip()
    title = cells[1].a.text.strip()
    year = cells[1].span.text.strip("()")
    rating = cells[2].text.strip()
    movie = {"rank": rank, "title": title, "year": year, "rating": rating}
    movies.append(movie)

# Save the data to a JSON file
with open("imdb_top_movies.json", "w") as f:
    json.dump(movies, f, indent=4)
