import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def run_scraper():
    url = "https://news.ycombinator.com/"
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Scraping {url}...")
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('span', class_='titleline')

        # Saving to CSV (Excel compatible)
        with open('headlines.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Index", "Headline", "Timestamp"]) # Header row
            
            for i, title in enumerate(titles[:15], 1):
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
                writer.writerow([i, title.text, timestamp])
        
        print("✅ Success! Check 'headlines.csv' in your folder.")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    run_scraper()
