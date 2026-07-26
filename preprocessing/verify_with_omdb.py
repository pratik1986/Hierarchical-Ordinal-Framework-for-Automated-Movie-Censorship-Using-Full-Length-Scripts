"""
===============================================================================
Script: verify_with_omdb.py

Description:
    Prototype implementation for validating movie script dataset metadata using
    the Open Movie Database (OMDb) API.

Purpose:
    During construction of the English movie script dataset used in the paper
    "Hierarchical Ordinal Framework for Automated Movie Censorship Using
    Full-Length Scripts" (IEEE GCAT 2025), movie titles, MPAA ratings, and
    release years encoded in dataset filenames were automatically verified
    against OMDb records.

Functionality:
    • Loads the OMDb API key from an environment file.
    • Parses filenames following:
          Rating_Title_Year
    • Extracts the expected MPAA rating, title, and release year.
    • Queries the OMDb API.
    • Compares dataset metadata with official movie metadata.
    • Reports successful matches and metadata mismatches.

Input:
    Movie filenames.

Output:
    Console report indicating:
        - Verified movies
        - Metadata mismatches
        - Movies not found

Dependencies:
    requests
    python-dotenv

Author:
    Pratik N. Kalamkar
===============================================================================
"""

import os
import re
import requests
from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv(r"G:\My Drive\PhDWorks\4_Final_Writing_Papers\05_ConferencePaper_3\dataset\key_.env")
print("Current directory:", os.getcwd())
print("Files in directory:", os.listdir())
print("Is .env present?", '.env' in os.listdir())
api_key = os.getenv("OMDB_API_KEY")

# Verify key loaded
if not api_key:
    print("❌ ERROR: API key not loaded!")
    exit()

print(f"✅ API Key loaded: {api_key[:4]}...{api_key[-4:]}")

filename_pattern = re.compile(r"^(G|PG|PG_13|R|NC_17|NR)_(.+?)_(\d{4})$")

def verify_movie(filename):
    print(f"\nProcessing: {filename}")
    
    match = filename_pattern.match(filename)
    if not match:
        print(f"❌ Invalid filename format: {filename}")
        return
    
    rating, title, year = match.groups()
    title = title.replace("_", " ")
    title = re.sub(r"^(PG13|R|PG|NC17)\s+", "", title)  # Remove rating prefixes
    
    encoded_title = quote(title)
    omdb_url = f"http://www.omdbapi.com/?t={encoded_title}&y={year}&apikey={api_key}"
    print(f"API Query: {omdb_url.split('&apikey')[0]}")
    
    response = requests.get(omdb_url).json()
    print("API Response:", response)
    
    if response.get("Response") == "False":
        print(f"❌ Movie not found: '{title}' ({year}) | Error: {response.get('Error')}")
        return
    
    imdb_rating = response.get("Rated", "N/A")
    imdb_year = response.get("Year", "N/A")
    
    print(f"IMDb Data: Rating={imdb_rating}, Year={imdb_year}")
    
    if rating.replace("_", "-") == imdb_rating and year == imdb_year:
        print(f"✅ Verified: {title} ({year})")
    else:
        print(f"⚠️ Mismatch: Expected {rating}/{year}, Got {imdb_rating}/{imdb_year}")

test_files = [
    "PG_13_Inception_2010",
    "R_The_Shawshank_Redemption_1994",
    "PG_13_Avengers_Endgame_2019"
]

for filename in test_files:
    verify_movie(filename)

input("\nPress Enter to exit...")