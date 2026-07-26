"""
===============================================================================
Script: detect_duplicate_scripts.py

Description:
    Detects potential duplicate movie script files across multiple screenplay
    collections using filename normalization and fuzzy string matching.

Purpose:
    During construction of the English movie script dataset used in the paper
    "Hierarchical Ordinal Framework for Automated Movie Censorship Using
    Full-Length Scripts" (IEEE GCAT 2025), screenplay files collected from
    different sources were compared to identify duplicate movies before merging
    them into the final corpus.

Functionality:
    • Normalizes movie filenames by removing rating prefixes, release years,
      common words (e.g., "The"), and formatting differences.
    • Uses fuzzy string matching (difflib) to identify likely duplicate files.
    • Generates a dry-run report without modifying or deleting any files.

Input:
    Two directories containing movie screenplay text files.

Output:
    Console report listing potential duplicate movies.

Dependencies:
    Python Standard Library
        - os
        - re
        - difflib

Author:
    Pratik N. Kalamkar
===============================================================================
"""


import os
import re
import difflib

# Paths
english_folder = r"G:\My Drive\PhDWorks\4_Final_Writing_Papers\05_ConferencePaper_3\dataset\English"
additional_folder = r"G:\My Drive\PhDWorks\4_Final_Writing_Papers\05_ConferencePaper_3\dataset\English_additional"

prefixes = ["G_", "PG_", "PG-13_", "NC-17_", "R_"]

def normalize_filename(filename):
    name, _ = os.path.splitext(filename)
    for prefix in prefixes:
        if name.startswith(prefix):
            name = name[len(prefix):]
            break
    name = re.sub(r"_20\d{2}$", "", name)
    name = name.replace("_", "")
    name = re.sub(r"(?i)the", "", name)
    return name.lower()

# Normalize English files
normalized_english_files = set()
for file in os.listdir(english_folder):
    norm = normalize_filename(file)
    normalized_english_files.add(norm)

# Try fuzzy matching for additional files
matched_files = []

for file in os.listdir(additional_folder):
    norm = normalize_filename(file)
    match = difflib.get_close_matches(norm, normalized_english_files, n=1, cutoff=0.90)
    if match:
        matched_files.append((file, match[0]))

# Report matches
print("\n=== Dry Run: Matched Files (No Files Deleted) ===")
if matched_files:
    for original, matched_with in matched_files:
        print(f"- {original}  <-- matched with -->  {matched_with}")
    print(f"\nTotal matched files: {len(matched_files)}")
else:
    print("No matching files found.")

input("\nPress Enter to exit...")
