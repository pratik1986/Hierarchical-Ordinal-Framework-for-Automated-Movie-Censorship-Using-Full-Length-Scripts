import requests
import os
from dotenv import load_dotenv
import time

load_dotenv(r"G:\My Drive\PhDWorks\4_Final_Writing_Papers\05_ConferencePaper_3\dataset\key_.env")
API_KEY = os.getenv("OMDB_API_KEY")

G_TARGET, NC17_TARGET = 20, 40
START_YEAR = 1990  # Expanded year range
g_movies, nc17_movies = [], []

def fetch_movies():
    for year in range(START_YEAR, 2025):
        print(f"Checking year: {year}...")
        page = 1
        while True:
            url = f"http://www.omdbapi.com/?s=movie&y={year}&page={page}&apikey={API_KEY}"
            response = requests.get(url).json()
            
            if "Search" not in response:
                break
            
            for movie in response["Search"]:
                details_url = f"http://www.omdbapi.com/?i={movie['imdbID']}&apikey={API_KEY}"
                details = requests.get(details_url).json()
                
                rated = details.get("Rated", "")
                if rated == "G" and len(g_movies) < G_TARGET:
                    g_movies.append(details["Title"])
                    print(f"Found G: {details['Title']} ({year})")
                elif rated == "NC-17" and len(nc17_movies) < NC17_TARGET:
                    nc17_movies.append(details["Title"])
                    print(f"Found NC-17: {details['Title']} ({year})")
                
                if len(g_movies) == G_TARGET and len(nc17_movies) == NC17_TARGET:
                    return
            
            page += 1
            time.sleep(1)  # Avoid rate limits

fetch_movies()

print("\n=== Results ===")
print(f"\nG-rated Movies (Total: {len(g_movies)}):")
for i, title in enumerate(g_movies, 1):
    print(f"{i}. {title}")

print(f"\nNC-17-rated Movies (Total: {len(nc17_movies)}):")
for i, title in enumerate(nc17_movies, 1):
    print(f"{i}. {title}")

input("\nPress Enter to exit...")