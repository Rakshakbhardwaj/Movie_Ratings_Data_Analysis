🎬 Movie Ratings Data Analysis

A Python-based Movie Ratings Data Analysis project that explores movie ratings, popularity, genres, release years, and votes using Pandas, NumPy, and Matplotlib.

The project creates a movie dataset, performs data cleaning and statistical analysis, identifies top-rated and most-popular movies, analyzes genres, calculates a combined movie score, measures correlations, and generates several visualizations.

📌 Project Overview

This project analyzes a dataset containing 30 movies with information such as:

Movie name
Genre
Rating
Popularity
Release year
Number of votes

The analysis helps identify patterns in movie ratings and popularity and provides visual insights through different charts and graphs.

🛠️ Technologies Used
Python
Pandas – Data manipulation and analysis
NumPy – Numerical and statistical calculations
Matplotlib – Data visualization
CSV – Dataset storage
📂 Dataset Features
Column	Description
Movie	Name of the movie
Genre	Movie genre
Rating	Movie rating out of 10
Popularity	Popularity score
Year	Movie release year
Votes	Number of votes received
🔍 Analysis Performed
1. Dataset Creation

The project creates a custom movie dataset and saves it as:

movies.csv

2. Data Loading & Cleaning
Loads the CSV dataset using Pandas
Checks for missing values
Removes duplicate records
Displays dataset shape and columns
3. Statistical Analysis

Calculates:

Average movie rating
Highest rating
Lowest rating
Standard deviation
4. Top-Rated Movies

Identifies the Top 10 highest-rated movies based on their ratings.

5. Most Popular Movies

Finds the Top 10 most popular movies using the popularity score.

6. Genre Analysis

Calculates for each genre:

Average rating
Average popularity
Number of movies

It also identifies the best-rated genre.

7. Combined Movie Score

A custom score is calculated using:

Movie Score = Rating × 70% + Popularity × 30%

This combines movie quality and popularity to rank movies.

8. Correlation Analysis

The project calculates the correlation between:

Rating
Popularity

It also creates a correlation matrix involving:

Rating
Popularity
Year
Votes
Movie Score
📊 Visualizations

The project generates the following charts:

Average Rating by Genre
Movie Distribution by Genre
Rating Distribution Histogram
Rating vs Popularity Scatter Plot
Top 10 Most Popular Movies
Number of Movies by Year
Movie Count by Genre
Correlation Heatmap

All visualizations are automatically saved as PNG files.

📁 Project Structure
Movie-Ratings-Data-Analysis/
│
├── movie_analysis.py
├── movies.csv
│
├── average_rating_by_genre.png
├── movie_distribution_by_genre.png
├── rating_distribution.png
├── rating_vs_popularity.png
├── top_10_popular_movies.png
├── movies_by_year.png
├── movie_count_by_genre.png
├── correlation_heatmap.png
│
└── README.md

▶️ How to Run the Project
1. Clone the repository
git clone https://github.com/your-username/Movie-Ratings-Data-Analysis.git

2. Navigate to the project directory
cd Movie-Ratings-Data-Analysis

3. Install required libraries
pip install numpy pandas matplotlib

4. Run the Python program
python movie_analysis.py


The program will create the dataset, perform the analysis, display the results, and generate the visualization files.

📈 Key Findings

The project provides insights into:

Overall movie rating performance
Highest-rated movie
Most popular movie
Best-performing genre
Relationship between ratings and popularity
Movie distribution across genres
Relationship between movie year, votes, ratings, and popularity
Top movies based on the combined scoring system
🎯 Learning Objectives

This project is useful for practicing:

Python programming
Pandas DataFrame operations
NumPy statistical functions
Data cleaning
GroupBy and aggregation
Sorting and filtering
Correlation analysis
Data visualization
Exploratory Data Analysis (EDA)
Working with CSV datasets
🚀 Future Improvements

Possible improvements include:

Add more movies to the dataset
Use a real-world movie dataset
Add Seaborn visualizations
Build an interactive dashboard
Add machine learning for rating prediction
Create a movie recommendation system
Analyze directors, actors, budgets, and revenue
Add interactive filters by genre and year
👨‍💻 Project Purpose

This project was created as a practical Data Analysis / Exploratory Data Analysis (EDA) project to demonstrate the use of Python libraries for analyzing and visualizing structured movie data.

⭐ If you find this project useful, consider giving the repository a star!
