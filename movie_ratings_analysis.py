import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 1. CREATE DATASET
# ============================================================

file_name = "movies.csv"

data = {
    "Movie": [
        "Inception", "The Dark Knight", "Interstellar", "Titanic",
        "Avatar", "Joker", "The Godfather", "Avengers Endgame",
        "Toy Story", "Parasite", "Forrest Gump", "The Matrix",
        "Gladiator", "Coco", "The Shawshank Redemption", "Pulp Fiction",
        "Finding Nemo", "Iron Man", "Up", "The Lion King",
        "Black Panther", "Whiplash", "Frozen", "Spider-Man",
        "Dangal", "3 Idiots", "Bahubali", "Drishyam", "RRR", "KGF"
    ],

    "Genre": [
        "Sci-Fi", "Action", "Sci-Fi", "Romance", "Sci-Fi",
        "Drama", "Crime", "Action", "Animation", "Thriller",
        "Drama", "Sci-Fi", "Action", "Animation", "Drama",
        "Crime", "Animation", "Action", "Animation", "Animation",
        "Action", "Drama", "Animation", "Action", "Drama",
        "Comedy", "Action", "Thriller", "Action", "Action"
    ],

    "Rating": [
        8.8, 9.0, 8.7, 7.9, 7.8,
        8.4, 9.2, 8.4, 8.3, 8.5,
        8.8, 8.7, 8.5, 8.4, 9.3,
        8.9, 8.2, 7.9, 8.3, 8.5,
        7.3, 8.5, 7.4, 7.3, 8.3,
        8.4, 8.0, 8.2, 8.0, 8.2
    ],

    "Popularity": [
        95, 98, 92, 96, 97,
        94, 90, 99, 85, 88,
        91, 89, 87, 86, 93,
        92, 82, 90, 84, 95,
        88, 80, 89, 93, 85,
        87, 86, 84, 96, 91
    ],

    "Year": [
        2010, 2008, 2014, 1997, 2009,
        2019, 1972, 2019, 1995, 2019,
        1994, 1999, 2000, 2017, 1994,
        1994, 2003, 2008, 2009, 1994,
        2018, 2014, 2013, 2002, 2016,
        2009, 2015, 2015, 2022, 2018
    ],

    "Votes": [
        250000, 320000, 280000, 350000, 300000,
        220000, 400000, 350000, 180000, 190000,
        380000, 360000, 300000, 160000, 450000,
        390000, 170000, 270000, 150000, 310000,
        210000, 200000, 190000, 250000, 180000,
        300000, 160000, 140000, 220000, 200000
    ]
}

df = pd.DataFrame(data)

# Save dataset
df.to_csv(file_name, index=False)

print("Movie dataset created successfully!")


# ============================================================
# 2. LOAD DATASET
# ============================================================

df = pd.read_csv(file_name)

print("\n" + "=" * 50)
print("MOVIE RATINGS DATA ANALYSIS")
print("=" * 50)

print("\nFirst 5 Movies:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())


# ============================================================
# 3. DATA CLEANING
# ============================================================

print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

print("\nTotal Movies:", len(df))


# ============================================================
# 4. BASIC STATISTICS
# ============================================================

rating = df["Rating"].to_numpy()

print("\n" + "=" * 50)
print("STATISTICAL ANALYSIS")
print("=" * 50)

print("Average Rating:", round(np.mean(rating), 2))
print("Highest Rating:", np.max(rating))
print("Lowest Rating:", np.min(rating))
print("Standard Deviation:", round(np.std(rating), 2))


# ============================================================
# 5. TOP 10 HIGHEST-RATED MOVIES
# ============================================================

top_rated = df.sort_values(
    "Rating",
    ascending=False
).head(10)

print("\n" + "=" * 50)
print("TOP 10 HIGHEST-RATED MOVIES")
print("=" * 50)

print(
    top_rated[
        ["Movie", "Genre", "Rating"]
    ].to_string(index=False)
)


# ============================================================
# 6. TOP 10 MOST POPULAR MOVIES
# ============================================================

popular = df.sort_values(
    "Popularity",
    ascending=False
).head(10)

print("\n" + "=" * 50)
print("TOP 10 MOST POPULAR MOVIES")
print("=" * 50)

print(
    popular[
        ["Movie", "Popularity", "Rating"]
    ].to_string(index=False)
)


# ============================================================
# 7. GENRE ANALYSIS
# ============================================================

genre = df.groupby("Genre").agg(
    Average_Rating=("Rating", "mean"),
    Average_Popularity=("Popularity", "mean"),
    Movie_Count=("Movie", "count")
)

genre = genre.sort_values(
    "Average_Rating",
    ascending=False
)

print("\n" + "=" * 50)
print("GENRE ANALYSIS")
print("=" * 50)

print(genre.round(2))


# ============================================================
# 8. BEST GENRE
# ============================================================

best_genre = genre["Average_Rating"].idxmax()

print("\nBest Rated Genre:", best_genre)
print(
    "Average Rating:",
    round(genre["Average_Rating"].max(), 2)
)


# ============================================================
# 9. MOVIE SCORE
# ============================================================
# Rating = 70%
# Popularity = 30%

df["Movie_Score"] = (
    df["Rating"] / 10 * 70
    +
    df["Popularity"] / 100 * 30
)

best_movies = df.sort_values(
    "Movie_Score",
    ascending=False
).head(10)

print("\n" + "=" * 50)
print("TOP 10 MOVIES BY COMBINED SCORE")
print("=" * 50)

print(
    best_movies[
        ["Movie", "Rating", "Popularity", "Movie_Score"]
    ].round(2).to_string(index=False)
)


# ============================================================
# 10. CORRELATION
# ============================================================

correlation = np.corrcoef(
    df["Rating"],
    df["Popularity"]
)[0, 1]

print("\n" + "=" * 50)
print("CORRELATION ANALYSIS")
print("=" * 50)

print(
    "Rating vs Popularity:",
    round(correlation, 2)
)

if correlation > 0.7:
    print("Strong positive relationship")

elif correlation > 0.3:
    print("Moderate positive relationship")

elif correlation > -0.3:
    print("Weak relationship")

else:
    print("Negative relationship")


# ============================================================
# 11. BAR CHART - AVERAGE RATING BY GENRE
# ============================================================

plt.figure(figsize=(8, 5))

plt.bar(
    genre.index,
    genre["Average_Rating"],
    color="skyblue",
    edgecolor="black"
)

plt.title("Average Rating by Genre")
plt.xlabel("Genre")
plt.ylabel("Average Rating")
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig("average_rating_by_genre.png")
plt.show()


# ============================================================
# 12. PIE CHART - MOVIES BY GENRE
# ============================================================

genre_count = df["Genre"].value_counts()

plt.figure(figsize=(7, 7))

plt.pie(
    genre_count,
    labels=genre_count.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Movie Distribution by Genre")

plt.tight_layout()
plt.savefig("movie_distribution_by_genre.png")
plt.show()


# ============================================================
# 13. HISTOGRAM - RATING DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 5))

plt.hist(
    df["Rating"],
    bins=8,
    color="orange",
    edgecolor="black"
)

plt.title("Distribution of Movie Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Movies")

plt.tight_layout()
plt.savefig("rating_distribution.png")
plt.show()


# ============================================================
# 14. SCATTER PLOT - RATING VS POPULARITY
# ============================================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Rating"],
    df["Popularity"],
    color="green",
    s=70
)

plt.title("Rating vs Popularity")
plt.xlabel("Rating")
plt.ylabel("Popularity")
plt.grid(True)

plt.tight_layout()
plt.savefig("rating_vs_popularity.png")
plt.show()


# ============================================================
# 15. TOP 10 POPULAR MOVIES
# ============================================================

top_10 = df.sort_values(
    "Popularity",
    ascending=False
).head(10)

plt.figure(figsize=(10, 6))

plt.barh(
    top_10["Movie"],
    top_10["Popularity"],
    color="purple",
    edgecolor="black"
)

plt.title("Top 10 Most Popular Movies")
plt.xlabel("Popularity")
plt.ylabel("Movie")

plt.gca().invert_yaxis()

plt.tight_layout()
plt.savefig("top_10_popular_movies.png")
plt.show()


# ============================================================
# 16. MOVIES BY YEAR
# ============================================================

year_count = df.groupby("Year")["Movie"].count()

plt.figure(figsize=(10, 5))

plt.plot(
    year_count.index,
    year_count.values,
    marker="o",
    color="red"
)

plt.title("Number of Movies by Year")
plt.xlabel("Year")
plt.ylabel("Number of Movies")
plt.grid(True)

plt.tight_layout()
plt.savefig("movies_by_year.png")
plt.show()


# ============================================================
# 17. MOVIE COUNT BY GENRE
# ============================================================

plt.figure(figsize=(8, 5))

plt.bar(
    genre_count.index,
    genre_count.values,
    color="teal",
    edgecolor="black"
)

plt.title("Number of Movies by Genre")
plt.xlabel("Genre")
plt.ylabel("Number of Movies")
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig("movie_count_by_genre.png")
plt.show()


# ============================================================
# 18. CORRELATION HEATMAP
# ============================================================

columns = [
    "Rating",
    "Popularity",
    "Year",
    "Votes",
    "Movie_Score"
]

correlation_matrix = df[columns].corr()

plt.figure(figsize=(8, 6))

plt.imshow(
    correlation_matrix,
    cmap="coolwarm"
)

plt.colorbar()

plt.xticks(
    range(len(columns)),
    columns,
    rotation=30
)

plt.yticks(
    range(len(columns)),
    columns
)

# Add numbers to heatmap
for i in range(len(columns)):
    for j in range(len(columns)):
        plt.text(
            j,
            i,
            round(correlation_matrix.iloc[i, j], 2),
            ha="center",
            va="center"
        )

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()


# ============================================================
# 19. FINAL RESULTS
# ============================================================

print("\n" + "=" * 50)
print("FINAL PROJECT FINDINGS")
print("=" * 50)

print(
    "Average Rating:",
    round(df["Rating"].mean(), 2)
)

print(
    "Highest Rated Movie:",
    df.loc[df["Rating"].idxmax(), "Movie"]
)

print(
    "Most Popular Movie:",
    df.loc[df["Popularity"].idxmax(), "Movie"]
)

print(
    "Best Genre:",
    best_genre
)

print(
    "Rating-Popularity Correlation:",
    round(correlation, 2)
)

print(
    "Total Movies:",
    len(df)
)

print("\nAnalysis completed successfully!")