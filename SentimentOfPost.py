import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Input and output file names
input_file ="2024_12_05_posts.csv"
output_file ="SentimentOfPost.csv"


# Read the input CSV file
try:
    df = pd.read_csv(input_file)
except FileNotFoundError:
    print(f"Error: File {input_file} not found.")
    exit()

# Check if the "Title" column exists
if "Title" not in df.columns:
    print("Error: The CSV file does not contain a 'Title' column.")
    exit()

# Perform sentiment analysis on the "Title" column
sentiment_results = []
for title in df["Title"]:
    sentiment_score = sia.polarity_scores(title)
    sentiment_results.append(sentiment_score)

# Add sentiment values to the DataFrame
df["Positive"] = [score["pos"] for score in sentiment_results]
df["Neutral"] = [score["neu"] for score in sentiment_results]
df["Negative"] = [score["neg"] for score in sentiment_results]
df["Compound"] = [score["compound"] for score in sentiment_results]

# Save the results to an Excel file
df.to_csv(output_file, index=False)

print(f"Sentiment analysis completed. Results saved to {output_file}.")
