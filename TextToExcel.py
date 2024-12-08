import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# File containing comments
input_file = "5th-december.txt"
output_file = "5th-december.csv"

# Read the comments from the text file
with open(input_file, "r", encoding="utf-8") as file:
    content = file.read()

# Split the file into sections by posts
posts = content.split("=" * 50 + "\n\n")

# Initialize lists to store sentiment results
post_sentiments = []
all_comments_sentiment = []

# Process each post
for post in posts:
    if "Post Title:" in post:
        # Extract post title and comments
        title_match = re.search(r"Post Title: (.+)", post)
        url_match = re.search(r"URL: (.+)", post)

        post_title = title_match.group(1) if title_match else "Unknown"
        post_url = url_match.group(1) if url_match else "Unknown"

        # Extract individual comments
        comments = []
        for line in post.split("\n"):
            if line.startswith("First Comment:"):
                comment = line.replace("First Comment:", "").strip()
                comments.append(comment)

        # Skip posts without comments
        if not comments:
            continue

        # Perform sentiment analysis on comments
        lexicon_values = []
        for comment in comments:
            sentiment_score = sia.polarity_scores(comment)
            lexicon_values.append(sentiment_score)
            all_comments_sentiment.append(sentiment_score["compound"])

        # Calculate average sentiment for the post
        avg_sentiment = {
            "Positive": sum(score["pos"] for score in lexicon_values) / len(lexicon_values),
            "Neutral": sum(score["neu"] for score in lexicon_values) / len(lexicon_values),
            "Negative": sum(score["neg"] for score in lexicon_values) / len(lexicon_values),
            "Compound": sum(score["compound"] for score in lexicon_values) / len(lexicon_values)
        }

        # Determine overall sentiment
        compound_avg = avg_sentiment["Compound"]
        if compound_avg >= 0.05:
            overall_sentiment = "Positive"
        elif compound_avg <= -0.05:
            overall_sentiment = "Negative"
        else:
            overall_sentiment = "Neutral"

        # Append results for the post  
        post_sentiments.append({
            "Title": post_title,
            "URL": post_url,
            "Positive Avg": avg_sentiment["Positive"],
            "Neutral Avg": avg_sentiment["Neutral"],
            "Negative Avg": avg_sentiment["Negative"],
            "Compound Avg": avg_sentiment["Compound"],
            "Overall Sentiment": overall_sentiment
        })

# Create a DataFrame for sentiment results
df = pd.DataFrame(post_sentiments)
print(df.head())
# Save results to an Excel file
df.to_csv(output_file, index=False)
print(f"Sentiment analysis completed. Results saved to {output_file}.") 
