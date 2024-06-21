# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Start coding!
netflix_df = pd.read_csv("netflix_data.csv", index_col = 0)
netflix_df.iloc[:5,]

netflix_subset = netflix_df[netflix_df["type"] == "Movie"]
netflix_subset.iloc[:5]
netflix_movies = netflix_subset[['title', 'country', 'genre', 'release_year', 'duration']]

fig, ax = plt.subplots(figsize=(12, 8))

colors = []

for col, row in netflix_movies.iterrows():
    if row['genre'] == "International TV":
        colors.append("green")
    elif row['genre'] == "Crime TV":
        colors.append("red")
    elif row['genre'] == "Horror Movies":
        colors.append("orange")
    elif row['genre'] == "Action":
        colors.append("yellow")
    elif row['genre'] == "Dramas":
        colors.append("purple")
    elif row['genre'] == "Anime Series":
        colors.append("blue")
    elif row['genre'] == "TV Comedies":
        colors.append("pink")
    elif row['genre'] == "British TV":
        colors.append("teal")
    elif row['genre'] == "Docuseries":
        colors.append("gray")
    elif row['genre'] == "Comedies":
        colors.append("indigo")
    elif row['genre'] == "Independent Movies":
        colors.append("olive")
    elif row['genre'] == "Sports Movies":
        colors.append("cyan")
    else:
        colors.append("black")

ax.scatter(x=netflix_movies['release_year'], y=netflix_movies['duration'], c=colors)

plt.xlabel("Release year")
plt.ylabel("Duration (min)")

plt.title("Movie Duration by Year of Release")

plt.show()

answer = "maybe"