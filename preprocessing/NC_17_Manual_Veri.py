# List of known NC-17 films (manually verified)
nc17_movies_alltime = [
    {"title": "Showgirls", "year": 1995},  # Most famous example
    {"title": "Blue Is the Warmest Color", "year": 2013},
    {"title": "Antichrist", "year": 2009},
    {"title": "The Brown Bunny", "year": 2003},
    {"title": "Crash", "year": 1996},  # Cronenberg's film
    {"title": "A Serbian Film", "year": 2010},
    {"title": "Caligula", "year": 1979},
    {"title": "Baise-moi", "year": 2000},
    {"title": "The Dreamers", "year": 2003},  # Originally NC-17
    {"title": "Henry & June", "year": 1990},  # First NC-17 film
    {"title": "Love", "year": 2015},  # Gaspar Noé's film
    {"title": "Nymphomaniac Vol. I", "year": 2013},
    {"title": "Nymphomaniac Vol. II", "year": 2013},
    {"title": "The Evil Dead", "year": 1981},  # Originally NC-17 (later recut)
    {"title": "The Cook, the Thief, His Wife & Her Lover", "year": 1989}
]

# Filter for post-2010 films
nc17_post_2010 = [movie for movie in nc17_movies_alltime if movie["year"] >= 2010]

# Print results
print("=== NC-17 Movies Released After 2010 ===")
for i, movie in enumerate(nc17_post_2010, 1):
    print(f"{i}. {movie['title']} ({movie['year']})")

print(f"\nTotal found: {len(nc17_post_2010)}")

# Pause before exiting
input("\nPress Enter to exit...")