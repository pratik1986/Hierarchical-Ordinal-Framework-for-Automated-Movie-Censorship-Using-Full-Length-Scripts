"""
===============================================================================
Script: scriptdotcom.py

Description:
    Searches the scripts.com website for publicly available movie screenplay
    pages and extracts candidate script links.

Purpose:
    During construction of the English movie script dataset used in the paper
    "Hierarchical Ordinal Framework for Automated Movie Censorship Using
    Full-Length Scripts" (IEEE GCAT 2025), screenplay sources were identified
    from publicly accessible websites. This utility automates searching
    scripts.com and extracts candidate screenplay URLs for manual verification.

Functionality:
    • Searches scripts.com using a movie title.
    • Downloads the search results page.
    • Parses HTML using BeautifulSoup.
    • Extracts screenplay links.
    • Saves the retrieved HTML for debugging if the website structure changes.

Input:
    Movie title.

Output:
    Candidate screenplay URLs printed to the console.

Dependencies:
    requests
    beautifulsoup4

Author:
    Pratik N. Kalamkar
===============================================================================
"""


import requests
from bs4 import BeautifulSoup

def search_scripts_com(movie_title):
    url = f"https://www.scripts.com/search.php?searchtype=scripts&search={movie_title.replace(' ', '+')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }
    
    try:
        print(f"Searching for: {movie_title}")
        print(f"Request URL: {url}")
        
        response = requests.get(url, headers=headers)
        print(f"Status Code: {response.status_code}")
        
        # Check if request was successful
        if response.status_code != 200:
            print(f"Request failed with status code {response.status_code}")
            return
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Debug: Save the HTML to inspect
        with open('debug_page.html', 'w', encoding='utf-8') as f:
            f.write(soup.prettify())
        
        # Try different selectors - the site might have changed its structure
        results = soup.find_all('a', href=True)  # First try broad search
        script_links = [a for a in results if '/script/' in a['href']]
        
        if not script_links:
            print("No results found using broad search")
            # Try looking for specific containers
            script_divs = soup.find_all('div', class_='script-result')  # Example class
            if script_divs:
                print(f"Found {len(script_divs)} possible results in divs")
        
        for link in script_links[:5]:  # Limit to first 5 for testing
            print(f"Possible match: {link.text.strip()} | Link: https://www.scripts.com{link['href']}")
            
    except Exception as e:
        print(f"Error searching for {movie_title}: {str(e)}")

# Test with different queries
search_scripts_com("Paddington 2")
search_scripts_com("The Social Network")  # Known to be on the site
search_scripts_com("Pulp Fiction")  # Another likely candidate