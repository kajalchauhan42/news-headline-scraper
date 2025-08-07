import requests
from bs4 import BeautifulSoup
import time

def scrape_news_headlines(url, output_file="news_headlines.txt"):
    """
    Scrapes headlines from a news website and saves them to a text file.
    
    Args:
        url (str): The URL of the news website.
        output_file (str): Path to save the headlines (default: 'news_headlines.txt').
    """
    try:
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        

        print(f"Fetching headlines from: {url}")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Check for HTTP errors
        
       
        soup = BeautifulSoup(response.text, 'html.parser')
        
        
        headlines = []
        for tag in ['h1', 'h2', 'h3', 'h4', 'a']:
            elements = soup.find_all(tag)
            for element in elements:
                text = element.get_text(strip=True)
                if text and len(text.split()) > 3:  # Filter out short/non-headline text
                    headlines.append(text)
        
        
        headlines = list(set(headlines))
        
        
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write("=== LATEST NEWS HEADLINES ===\n\n")
            for idx, headline in enumerate(headlines, 1):
                file.write(f"{idx}. {headline}\n")
        
        print(f"✅ Success! Saved {len(headlines)} headlines to '{output_file}'")
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching the page: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
   
    NEWS_URL = "https://www.bbc.com/news"
    OUTPUT_FILE = "news_headlines.txt"
    
    scrape_news_headlines(NEWS_URL, OUTPUT_FILE)