Simple Recommendation System
A movie recommendation system that matches user-entered interests against a small dataset using similarity scoring, then displays the best matches.
Requirements
Python 3.8+ (no external libraries needed)
Concepts Demonstrated
Logic building, pattern matching, recommendation concepts
What It Does
1.	Takes user input — you enter your interests as comma-separated tags (e.g. action, sci-fi)
2.	Matches using similarity — each movie in the dataset is scored using Jaccard similarity (shared tags ÷ total unique tags between your interests and the movie’s tags)
3.	Displays recommendations — the top 3 highest-scoring movies are shown, ranked with their match scores
How to Run
python recommendation_system.py
Example Interaction
🎬 Welcome to the Movie Recommender!
Available tags: sci-fi, action, thriller, romance, drama, comedy,
                horror, mystery, superhero, musical, crime, teen, space

Enter your interests (comma-separated, e.g. action, sci-fi): action, sci-fi

Based on your interests (action, sci-fi), we recommend:

1. Avengers: Endgame  (match score: 0.67)
2. Inception  (match score: 0.50)
3. John Wick  (match score: 0.25)
How It Works
Each movie is stored with a list of descriptive tags (genres/themes). When you enter your interests, the system compares your tag set against each movie’s tag set and calculates:
similarity = (shared tags) / (total unique tags combined)
Movies are then ranked from highest to lowest score, and the top 3 are displayed. This is a basic form of content-based filtering the same underlying idea used in real recommendation engines like Netflix or Spotify, just on a much smaller scale.
Customizing
To use a different dataset (books, music, products), just replace the movies list with your own items and tags the matching logic stays the same.
