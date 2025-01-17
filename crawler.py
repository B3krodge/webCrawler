
import requests 
from bs4 import BeautifulSoup
from parser_html import Parser_html
from urllib.parse import urlparse
import Levenshtein
import re

class Crawler():
    def __init__(self):
        self.crawled = 0
        self.find_keywords = Parser_html()
        
        
    def simple_crawler(self, seed_url, visited_set, url_queue, data): 
        #Add url to visited set
        visited_set.add(seed_url)

        # Send HTTP request to the URL 
        try:
            response = requests.get(seed_url)
            # Check if the request was successful (status code 200) 

            if response.status_code == 200: 
            # Parse HTML content with BeautifulSoup
                soup = BeautifulSoup(response.text, 'html.parser') 
                keywords = self.find_keywords.extract_keywords(soup)
                # Extract and print relevant information (modify as needed) 
                title = soup.title.text 
                data.append((seed_url, title, keywords))
                # Find all <a> tags and extract the href attribute
                urls = [a['href'] for a in soup.find_all('a', href=True)]

                # Find unvisited the extracted URLs
                for url in urls:
                    if re.match("https:", url) != None:
                        if url not in visited_set:
                            visited_set.add(url)
                            url_queue.put((self.compare_domains(seed_url, url), url))
                return True
            
        except Exception as e:
            print (e) 

        else: 
            print(f'Error: Failed to fetch {seed_url}') 
        return False

    def compare_domains(self, url1, url2):
    # Extract the netloc (domain) from each URL
        domain1 = urlparse(url1).netloc
        domain2 = urlparse(url2).netloc
        return Levenshtein.distance(domain1, domain2)
