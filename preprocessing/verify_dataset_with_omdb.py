"""
===============================================================================
Script: verify_dataset_with_omdb.py

Description:
    Verifies movie screenplay filenames against the Open Movie Database (OMDb)
    and reports metadata inconsistencies.

Purpose:
    As part of the dataset preparation workflow for the paper
    "Hierarchical Ordinal Framework for Automated Movie Censorship Using
    Full-Length Scripts" (IEEE GCAT 2025), this utility validates movie
    titles, MPAA ratings, and release years encoded in screenplay filenames
    against official OMDb metadata.

Functionality:
    • Parses screenplay filenames.
    • Queries OMDb using movie title and release year.
    • Verifies MPAA rating and release year.
    • Suggests corrected filenames for mismatched entries.
    • Handles retries for temporary API failures.
    • Produces a verification summary.

Dependencies:
    requests
    python-dotenv

Author:
    Pratik N. Kalamkar
===============================================================================
"""


import os
import re
import time
import requests
from dotenv import load_dotenv
from urllib.parse import quote

# ===== CONFIGURATION =====
SCRIPT_FOLDER = r"G:\My Drive\PhDWorks\4_Final_Writing_Papers\05_ConferencePaper_3\dataset\English_additional"
ENV_FILE = r"G:\My Drive\PhDWorks\4_Final_Writing_Papers\05_ConferencePaper_3\dataset\key_.env"
MAX_RETRIES = 2
RETRY_DELAY = 2
# =========================

load_dotenv(ENV_FILE)
API_KEY = os.getenv("OMDB_API_KEY")

if not API_KEY:
    raise ValueError("❌ API key not found in key_.env")

def clean_title(title):
    """Convert underscores to spaces while preserving the full title"""
    return title.replace("_", " ").strip()

def verify_movie(filename):
    print(f"\n🔍 Processing: {filename}")
    
    # First check if it's a PG_13 file
    if filename.startswith("PG_13_"):
        # Handle PG_13 case specially
        rating = "PG_13"
        remaining = filename[6:]  # Remove "PG_13_"
        # Split the remaining part into title and year
        parts = remaining.rsplit("_", 1)
        if len(parts) != 2:
            print(f"❌ Invalid filename format for PG_13 movie")
            return None
        title, year_part = parts
        year = year_part.replace(".txt", "")
    else:
        # Handle other ratings normally
        parts = filename.split("_")
        if len(parts) < 3:
            print(f"❌ Invalid filename format")
            return None
        rating = parts[0]
        year = parts[-1].replace(".txt", "")
        title = "_".join(parts[1:-1])
    
    cleaned_title = clean_title(title)
    print(f"Parsed: Rating={rating}, Title='{cleaned_title}', Year={year}")
    
    # API Request
    base_url = f"http://www.omdbapi.com/?t={quote(cleaned_title)}&y={year}"
    print(f"🔎 Querying: {base_url}...")
    
    attempt = 0
    while attempt <= MAX_RETRIES:
        try:
            response = requests.get(f"{base_url}&apikey={API_KEY}", timeout=10).json()
            
            if response.get("Response") == "True":
                imdb_rating = response.get("Rated", "N/A").upper()
                imdb_title = response.get("Title", "N/A")
                imdb_year = response.get("Year", "N/A")
                
                print(f"📊 IMDb Data: {imdb_rating}/{imdb_year} ({imdb_title})")
                
                # Compare ratings (convert PG_13 to PG-13 for comparison)
                our_rating = rating.replace("_", "-")
                if our_rating == imdb_rating and year == imdb_year:
                    print(f"✅ Perfect match!")
                    return None  # No changes needed
                else:
                    # Generate suggested new filename
                    new_rating = imdb_rating.replace("-", "_")
                    new_title = imdb_title.replace(" ", "_")
                    new_filename = f"{new_rating}_{new_title}_{imdb_year}.txt"
                    return (filename, new_filename)
            else:
                error = response.get("Error", "Unknown error")
                print(f"⚠️ API Error (attempt {attempt+1}/{MAX_RETRIES+1}): {error}")
                
        except Exception as e:
            print(f"⚠️ Network error (attempt {attempt+1}/{MAX_RETRIES+1}): {str(e)}")
        
        attempt += 1
        if attempt <= MAX_RETRIES:
            time.sleep(RETRY_DELAY * attempt)
    
    print(f"❌ Failed after {MAX_RETRIES+1} attempts")
    return (filename, None)  # Couldn't verify, no suggestion

def main():
    print(f"🚀 Verifying script files in:\n{SCRIPT_FOLDER}")
    
    try:
        txt_files = [f for f in os.listdir(SCRIPT_FOLDER) if f.endswith('.txt')]
        
        if not txt_files:
            print("❌ No .txt files found")
            return
        
        print(f"Found {len(txt_files)} script files")
        
        verified_files = []
        needs_changes = []
        
        for i, filename in enumerate(txt_files, 1):
            print(f"\n📄 File {i}/{len(txt_files)}: {filename}")
            result = verify_movie(filename)
            if result is None:
                verified_files.append(filename)
            else:
                needs_changes.append(result)
            time.sleep(1)  # Rate limiting
        
        # Print results summary
        print("\n" + "="*50)
        print("🎉 Verification Results:")
        print("="*50)
        
        print("\n✅ VERIFIED FILES:")
        if verified_files:
            for file in verified_files:
                print(f"- {file}")
        else:
            print("No files were verified")
        
        print("\n⚠️ FILES NEEDING CHANGES:")
        if needs_changes:
            print("\nSuggested filename changes:")
            max_len = max(len(old) for old, new in needs_changes if new is not None)
            for old, new in needs_changes:
                if new:
                    print(f"{old.ljust(max_len)} : {new}")
                else:
                    print(f"{old} : [Could not determine correct filename]")
        else:
            print("All files were verified successfully!")
        
        print(f"\nSUMMARY: {len(verified_files)} verified, {len(needs_changes)} need changes")
        
    except Exception as e:
        print(f"❌ Critical error: {str(e)}")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()