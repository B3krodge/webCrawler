# Web Crawler Project

## Overview

This is a simple **web crawler** that fetches up to 1,000 websites and extracts relevant data, including the title, keywords, and URLs. The crawler starts with a seed URL and traverses other pages, extracting and storing keywords and titles. It utilizes libraries like `BeautifulSoup` for HTML parsing, `nltk` for natural language processing, and `Levenshtein` for domain similarity calculations.

## Features

- **Crawl websites**: Starting from a given seed URL, the crawler visits up to 1,000 URLs.
- **Extract key data**: The crawler collects the **title**, **keywords**, and **URL** of each webpage.
- **Domain similarity**: It calculates the **Levenshtein distance** between domains to prioritize crawling.
- **Visualization**: The crawler plots the number of crawled URLs and the size of the URL queue over time using `matplotlib`.
- **CSV Export**: The crawler exports the results (URLs, titles, and keywords) to a CSV file for later analysis.

## Project Structure

webCrawler/ │ ├── main.py # Main program to run the crawler ├── crawler.py # Crawler logic for fetching URLs and extracting data ├── parser_html.py # Handles extraction of keywords from HTML content ├── requirements.txt # List of dependencies for the project ├── titles.csv # CSV file containing crawled data (URL, Title, Keywords)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/webCrawler.git
   cd webCrawler
   ```
2. **Create and activate a virtual environment**:
   ````python3 -m venv venv
   source venv/bin/activate # For macOS/Linux
   .\venv\Scripts\activate # For Windows```
   ````
3. **Install the dependencies**:
   `pip install -r requirements.txt`

## Usage

1. **Configure the seed URL**:
   In main.py, the seed URL is defined in the Main class. You can modify the self.seed_url variable to start the crawl from a different URL. By default, it is set to 'https://youtube.com'.

2. **Run the crawler**:
   `python main.py`
3. **Results**:
   The crawler will output the following:
   - titles.csv: A CSV file containing the URL, title, and keywords of the crawled websites.
   - Matplotlib Plot: A graph showing the crawling progress with the number of crawled URLs and the current queue size over time.

## Code Explanation

1. **crawler.py**
   The Crawler class handles the crawling process. It:

- Sends HTTP requests to URLs.
- Extracts HTML content and parses it using BeautifulSoup.
- Extracts the title and keywords from the HTML content using Parser_html.
- Finds and processes additional URLs to crawl, comparing the domains with Levenshtein distance for prioritization.

2.  **main.py**
    The Main class manages the overall crawling operation, including:

- Initializing the seed URL and the priority queue.
- Writing the crawled data to a CSV file.
- Plotting the crawling statistics using Matplotlib.

3. **parser_html.py**
   The Parser_html class extracts keywords from HTML content using nltk stopwords and Counter to calculate word frequencies.

## Requirements

The following Python packages are required to run the project:

- beautifulsoup4: For parsing HTML content.
- nltk: For processing text and removing stopwords.
- requests: For sending HTTP requests.
- matplotlib: For plotting crawling statistics.
- python-Levenshtein: For calculating the Levenshtein distance between domains.
- You can install them via the requirements.txt file:
  `pip install -r requirements.txt`

## Dependencies

Here is a list of the required packages:

- beautifulsoup4==4.12.2
- nltk==3.9.1
- requests==2.31.0
- matplotlib==3.7.4
- python-Levenshtein==0.26.1
