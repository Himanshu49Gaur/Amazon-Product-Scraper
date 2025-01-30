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
