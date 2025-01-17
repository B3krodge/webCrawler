from crawler import Crawler
from queue import PriorityQueue
import csv
import matplotlib.pyplot as plt
from datetime import datetime


class Main():

    def __init__(self) -> None:
        self.crawler_queue = PriorityQueue()
        self.visited_set = set()
        self.seed_url = 'https://www.gatech.edu' 
        self.crawler = Crawler()
        self.data = []
        self.num_crawled = []
        self.queue_size= []
        self.time_y = []

    def search(self):
        #Placing starting url in queue
        self.crawler_queue.put((1, self.seed_url))
        #Creating csv file to save subjects of websites
        with open("titles.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["URL", "Title", "Keywords"])  # Write the header

            num_visited_urls = 0
            while (num_visited_urls < 1000 and self.crawler_queue.empty() == False):
                successful_url = self.crawler.simple_crawler(
                    self.crawler_queue.get()[1],
                    self.visited_set, 
                    self.crawler_queue,
                    self.data
                )
                if (successful_url == True):
                    url, title, keywords = self.data.pop()
                    writer.writerow([str(url), str(title), str(keywords)])
                    num_visited_urls+=1
                    self.num_crawled.append(num_visited_urls)
                    self.queue_size.append(self.crawler_queue.qsize())
                    current_time = datetime.now().strftime("%H:%M")  # Format as "HH:MM"
                    self.time_y.append(current_time)

                    print ("WE ARE AT " + str(num_visited_urls))
            # Plot the first line
            plt.plot(self.time_y, self.queue_size, label="Queue Size", linestyle="-", marker="o")

            # Plot the second line
            plt.plot(self.time_y, self.num_crawled, label="Crawled", linestyle="--", marker="s")
            # Add labels, title, and legend
            plt.xlabel("Time")
            plt.ylabel("Number of URLs")
            plt.title("Crawled vs. Queued URLs")
            plt.legend()
            # Save the plot to a file (e.g., PNG format)
            plt.savefig("crawling_stats.png", format="png")
            # Show the plot (optional)
            plt.show()

if __name__ == "__main__":
    main = Main()
    main.search()