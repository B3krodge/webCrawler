from collections import Counter
import re
from nltk.corpus import stopwords


class Parser_html():
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
    
    def extract_keywords(self, soup, num_keywords=10):

        # Extract relevant content: headings and paragraphs
        headings = ' '.join([tag.get_text() for tag in soup.find_all(['h1', 'h2', 'h3'])])
        paragraphs = ' '.join([tag.get_text() for tag in soup.find_all('p')])
        content = headings + ' ' + paragraphs

        # Clean the text
        content = re.sub(r'\s+', ' ', content)  # Remove extra whitespace
        content = re.sub(r'[^A-Za-z\s]', '', content)  # Remove non-alphabetic characters

        # Tokenize words and remove common stopwords
        words = content.lower().split()
        filtered_words = [word for word in words if word not in self.stop_words]

        # Count word frequencies
        word_counts = Counter(filtered_words)

        # Extract the top keywords
        keywords = word_counts.most_common(num_keywords)
        return keywords