import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Target URL (practice website)
BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

all_books = []

# Loop through first 3 pages (you can extend)
for page in range(1, 4):
    url = BASE_URL.format(page)
    print(f"Scraping page {page} → {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all book containers
    books = soup.find_all("article", class_="product_pod")
    
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.strip()
        availability = book.find("p", class_="instock availability").text.strip()
        
        all_books.append({
            "Title": title,
            "Price": price,
            "Availability": availability
        })
    
    time.sleep(1)  # polite delay to avoid hitting server too fast

# Convert to DataFrame
df = pd.DataFrame(all_books)
print(df.head())

# Save dataset
df.to_csv("books_dataset.csv", index=False)
print("Data saved to books_dataset.csv")