"""
===============================================================================
Script: rename_files_OMDB.py

Description:
    Automatically renames movie script files using verified metadata retrieved
    from the Open Movie Database (OMDb) API.

Purpose:
    During construction of the English movie script dataset used in the paper
    "Hierarchical Ordinal Framework for Automated Movie Censorship Using
    Full-Length Scripts" (IEEE GCAT 2025), downloaded screenplay files often
    lacked standardized filenames. This utility retrieves the official release
    year and MPAA rating from OMDb and renames files accordingly, ensuring
    consistent dataset organization.

Functionality:
    • Loads the OMDb API key from an environment file.
    • Queries OMDb for each movie title.
    • Retrieves official release year and MPAA rating.
    • Filters movies by selected rating categories.
    • Renames files using verified metadata.
    • Generates a processing summary.

Input:
    Directory containing movie script text files.

Output:
    Renamed movie script files with standardized metadata in the filename.

Dependencies:
    requests
    python-dotenv

Author:
    Pratik N. Kalamkar
===============================================================================
"""

import os
import requests
import json
from urllib.parse import quote
from dotenv import load_dotenv
import sys
import time

# Configuration
folder_path = r"G:\My Drive\PhDWorks\4_Final_Writing_Papers\05_ConferencePaper_3\dataset\Movie Scripts Corpus kaggle\screenplay_data\data\raw_texts\2008"
env_file = r"G:\My Drive\PhDWorks\4_Final_Writing_Papers\05_ConferencePaper_3\dataset\key_.env"
target_ratings = ["G", "PG", "NC-17"]  # Only process these ratings

def load_api_key(env_path):
    """Load API key from .env file"""
    try:
        load_dotenv(env_path)
        return os.getenv("OMDB_API_KEY")
    except Exception as e:
        print(f"Error loading .env file: {str(e)}")
        return None

def get_movie_info(title, api_key):
    """Query OMDB API for movie information"""
    base_url = "http://www.omdbapi.com/"
    encoded_title = quote(title)
    url = f"{base_url}?t={encoded_title}&apikey={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data.get("Response") == "True":
            year = data.get("Year", "").split("–")[0]  # Take first year if range
            rating = data.get("Rated", "")
            return year, rating
        else:
            print(f"Error for '{title}': {data.get('Error', 'Unknown error')}")
            return None, None
    except Exception as e:
        print(f"API request failed for '{title}': {str(e)}")
        return None, None

def rename_files_with_ratings():
    """Main function to process and rename files"""
    # Load API key from .env file
    api_key = load_api_key(env_file)
    if not api_key:
        print("Failed to load API key. Exiting.")
        return
    
    processed_count = 0
    skipped_count = 0
    error_count = 0
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".txt"):
            # Extract movie title by removing extension
            movie_title = os.path.splitext(filename)[0]
            
            # Get movie info from OMDB
            year, rating = get_movie_info(movie_title, api_key)
            
            if year and rating and rating in target_ratings:
                # Clean up year and rating
                year = year.strip()
                rating = rating.strip().replace("-", "")
                
                # Create new filename
                new_filename = f"{year}_{movie_title}_{rating}.txt"
                new_path = os.path.join(folder_path, new_filename)
                old_path = os.path.join(folder_path, filename)
                
                # Rename the file
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed: {filename} -> {new_filename}")
                    processed_count += 1
                except Exception as e:
                    print(f"Failed to rename {filename}: {str(e)}")
                    error_count += 1
            else:
                if rating:
                    print(f"Skipping {filename} (Rating: {rating})")
                else:
                    print(f"Skipping {filename} (No rating info found)")
                skipped_count += 1
    
    # Print summary
    print("\n" + "="*50)
    print(f"Processing complete!")
    print(f"Files renamed: {processed_count}")
    print(f"Files skipped: {skipped_count}")
    print(f"Errors encountered: {error_count}")
    print("="*50 + "\n")
    
    # Pause before exiting
    if sys.platform == "win32":
        os.system("pause")
    else:
        input("Press Enter to exit...")

if __name__ == "__main__":
    rename_files_with_ratings()