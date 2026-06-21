"""
Simple Recommendation System
------------------------------
Takes user interests as input, matches them against a small dataset of items
using similarity scoring (overlap between tags), and displays the best matches.

How to run:
    python recommendation_system.py
"""

# Small dataset: each item has a name and a list of tags/genres describing it.
movies = [
    {"title": "Inception",        "tags": ["sci-fi", "thriller", "action", "mind-bending"]},
    {"title": "The Notebook",     "tags": ["romance", "drama"]},
    {"title": "John Wick",        "tags": ["action", "thriller", "crime"]},
    {"title": "Interstellar",     "tags": ["sci-fi", "drama", "space"]},
    {"title": "The Hangover",     "tags": ["comedy"]},
    {"title": "La La Land",       "tags": ["romance", "musical", "drama"]},
    {"title": "Avengers: Endgame","tags": ["action", "sci-fi", "superhero"]},
    {"title": "Get Out",          "tags": ["horror", "thriller", "mystery"]},
    {"title": "The Conjuring",    "tags": ["horror", "thriller"]},
    {"title": "Superbad",         "tags": ["comedy", "teen"]},
]


def similarity_score(user_interests, item_tags):
    """
    Calculates how well an item matches user interests.
    Uses simple overlap (Jaccard-style): shared tags / total unique tags.
    """
    user_set = set(user_interests)
    item_set = set(item_tags)

    if not user_set or not item_set:
        return 0

    intersection = user_set & item_set
    union = user_set | item_set

    return len(intersection) / len(union)


def get_recommendations(user_interests, dataset, top_n=3):
    scored_items = []

    for item in dataset:
        score = similarity_score(user_interests, item["tags"])
        if score > 0:
            scored_items.append((item["title"], score))

    # Sort by highest similarity score first
    scored_items.sort(key=lambda x: x[1], reverse=True)

    return scored_items[:top_n]


def main():
    print("🎬 Welcome to the Movie Recommender!")
    print("Available tags: sci-fi, action, thriller, romance, drama, comedy,")
    print("                horror, mystery, superhero, musical, crime, teen, space\n")

    raw_input_str = input("Enter your interests (comma-separated, e.g. action, sci-fi): ")
    user_interests = [tag.strip().lower() for tag in raw_input_str.split(",") if tag.strip()]

    if not user_interests:
        print("No interests entered. Exiting.")
        return

    recommendations = get_recommendations(user_interests, movies, top_n=3)

    print(f"\nBased on your interests ({', '.join(user_interests)}), we recommend:\n")

    if recommendations:
        for rank, (title, score) in enumerate(recommendations, start=1):
            print(f"{rank}. {title}  (match score: {score:.2f})")
    else:
        print("No matches found. Try different interests!")


if __name__ == "__main__":
    main()
