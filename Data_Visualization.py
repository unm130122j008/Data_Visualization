import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")  # <-- your CSV file name

required_cols = [
    "title",
    "language",
    "genre",
    "release_year",
    "duration_minutes",
    "rating",
    "views_estimated"
]

for col in required_cols:
    if col not in df.columns:
        raise ValueError(f"Column '{col}' is missing in your CSV! Found: {df.columns.tolist()}")

print("CSV Loaded Successfully!\n")
print(df.head())

# -----------------------------
# 1️⃣ Bar Chart: Number of movies per language
# -----------------------------
plt.figure(figsize=(10,6))
df.language.value_counts().plot(kind="bar", color="skyblue")
plt.title("Number of Movies by Language")
plt.xlabel("Language")
plt.ylabel("Movie Count")
plt.tight_layout()
plt.show()

# -----------------------------
# 2️⃣ Line Chart: Movies released per year
# -----------------------------
plt.figure(figsize=(12,6))
df.release_year.value_counts().sort_index().plot(kind="line", marker='o', color="green")
plt.title("Movies Released Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Movies")
plt.grid(True)
plt.tight_layout()
plt.show()

# -----------------------------
# 3️⃣ Scatter Plot: Rating vs Views
# -----------------------------
plt.figure(figsize=(12,6))
plt.scatter(df.rating, df.views_estimated, s=df.duration_minutes/2, alpha=0.5, color="orange")
plt.title("Movie Rating vs Views (Bubble Size = Duration)")
plt.xlabel("Rating")
plt.ylabel("Views Estimated")
plt.tight_layout()
plt.show()

# -----------------------------
# 4️⃣ Pie Chart: Movie distribution by genre
# -----------------------------
plt.figure(figsize=(8,8))
df.genre.value_counts().plot(kind="pie", autopct='%1.1f%%', startangle=140)
plt.title("Movie Distribution by Genre")
plt.ylabel("")  # remove y-label
plt.tight_layout()
plt.show()

# -----------------------------
# 5️⃣ Box Plot: Rating distribution by language
# -----------------------------
plt.figure(figsize=(12,6))
df.boxplot(column="rating", by="language", grid=True)
plt.title("Rating Distribution by Language")
plt.suptitle("")  # remove default title
plt.xlabel("Language")
plt.ylabel("Rating")
plt.tight_layout()
plt.show()

# 6️⃣ Histogram of movie durations
plt.figure(figsize=(10,6))
plt.hist(df['duration_minutes'], bins=10, color='skyblue', edgecolor='black')
plt.title("Distribution of Movie Durations")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Movies")
plt.show()

print("\nAll 5 visualizations generated successfully!")
