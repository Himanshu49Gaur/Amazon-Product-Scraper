import requests
from bs4 import BeautifulSoup
import csv
import time
import random
import logging
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to extract data from a single product listing
def extract_product_data(product):
    try:
        # Extract product name
        product_name = product.h2.text.strip() if product.h2 else None
    except AttributeError:
        product_name = None

    try:
        # Extract price
        price = product.find("span", {"class": "a-price-whole"}).text.strip() if product.find("span", {"class": "a-price-whole"}) else None
    except AttributeError:
        price = None

    try:
        # Extract rating
        rating = product.find("span", {"class": "a-icon-alt"}).text.strip() if product.find("span", {"class": "a-icon-alt"}) else None
    except AttributeError:
        rating = None

    try:
        # Extract seller name (if available)
        seller_name = product.find("span", {"class": "a-size-small a-color-base"})
        if seller_name:
            seller_name = seller_name.text.strip()
        else:
            seller_name = None
    except AttributeError:
        seller_name = None

    # Log if the seller name is missing (optional for debugging)
    if not seller_name:
        logging.debug("Seller name not found for product: " + (product_name or "Unknown product"))

    return {
        "Product Name": product_name,
        "Price": price,
        "Rating": rating,
        "Seller Name": seller_name
    }


# Function to handle retries and set up a session with retry mechanism
def create_session():
    session = requests.Session()
    retries = Retry(total=3, backoff_factor=0.5, status_forcelist=[500, 502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))
    return session

# Function to scrape product details from a given Amazon URL
def scrape_amazon_products(url, output_csv):
    headers = {
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/92.0 Safari/537.36"
        ])
    }

    session = create_session()
    
    # Send GET request to the URL
    try:
        response = session.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"Failed to retrieve the webpage. Error: {e}")
        return

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all product listings on the page
    products = soup.find_all("div", {"data-component-type": "s-search-result"})

    if not products:
        logging.warning("No products found on the page.")
        return

    # List to store extracted data
    product_list = []

    for product in products:
        product_data = extract_product_data(product)
        if product_data["Product Name"]:  # Only include products with a valid name
            product_list.append(product_data)

    # Write the data to a CSV file
    try:
        file_exists = False
        try:
            with open(output_csv, mode='r', encoding="utf-8") as f:
                file_exists = True
        except FileNotFoundError:
            pass
        
        with open(output_csv, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["Product Name", "Price", "Rating", "Seller Name"])

            # Write header if file does not exist
            if not file_exists:
                writer.writeheader()
            
            writer.writerows(product_list)
        logging.info(f"Data successfully written to {output_csv}")

    except Exception as e:
        logging.error(f"Error writing to CSV: {e}")

# URL of the Amazon page to scrape
amazon_url = "https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar"

# Output CSV file name
output_file = "amazon_products.csv"

# Scrape the products and save to CSV
scrape_amazon_products(amazon_url, output_file)
