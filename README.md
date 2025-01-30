# Amazon-Product-Scraper
This is a Python-based scraper that extracts detailed information from Amazon product pages. It uses **Selenium** to navigate and interact with Amazon pages, allowing it to scrape dynamically rendered content such as product details, price, ratings, reviews, shipping information, and more.

## Features:
- Extracts product name, price, rating, number of reviews, availability, and ASIN (Amazon Standard Identification Number).
- Extracts dynamic shipping/delivery information (delivery times, shipping costs).
- Retrieves seller information, product features (bullet points), and other relevant data.
- Outputs the collected data in a CSV format for easy analysis.

## Requirements

You need to install the following dependencies for the scraper to work:

- **Selenium**: For controlling the browser and interacting with the page.
- **Chromedriver**: To use the Chrome browser for web scraping.

Setup Instructions:
Install Dependencies: Install the necessary Python libraries by running:
`pip install -r requirements.txt`

Download WebDriver:
1.Download ChromeDriver
2.Place the downloaded driver in a directory and update the path in the script (replace path_to_chromedriver with the actual path).

Run the Scraper: After setting up the environment and downloading the appropriate web driver, you can run the scraper using:


Copy
Edit
python amazon_scraper.py
It will scrape the product details and save them in a CSV file (e.g., amazon_product_data.csv).

Scraping Multiple Products: Modify the amazon_url variable in the script to point to any Amazon product page you want to scrape. You can even extend the scraper to scrape multiple pages by iterating over page links.

Example Output
After running the scraper, the output will be written to a CSV file with the following columns:

Product Name
Price
Rating
Number of Reviews
Availability
Seller Name
ASIN
Features
Delivery Info
Example CSV format:
csv
Copy
Edit
Product Name,Price,Rating,Number of Reviews,Availability,Seller Name,ASIN,Features,Delivery Info
"Product 1","₹999","4.5 stars (200 reviews)","200","In stock","Seller A","B07XY12345","Feature 1, Feature 2","Free delivery in 3-5 days"
"Product 2","₹799","4.2 stars (150 reviews)","150","In stock","Seller B","B07XY67890","Feature 1, Feature 2, Feature 3","Arrives by tomorrow with Prime"
License
This project is licensed under the MIT License - see the LICENSE file for details.

shell
Copy
Edit

### `requirements.txt`:

This file lists the Python libraries needed for the scraper:

selenium==4.4.3

vbnet
Copy
Edit

### Instructions for Using the Files:
1. **`README.md`**: This document explains the setup and usage of the scraper script. You can place it in the root of your GitHub repository.
2. **`requirements.txt`**: This file includes the necessary Python packages and versions for the project. You can install them with `pip install -r requirements.txt`.
   
Once you've set up your repository with these files, users can easily follow the instructions to install dependencies and run the scraper.

