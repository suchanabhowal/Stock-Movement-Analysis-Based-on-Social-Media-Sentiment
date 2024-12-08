import pandas as pd

# File paths
TestToExcel = "5th-december.csv"  # File from CODEB.py
DateWisePost = "2024_12_05_posts.csv"   # File from reddit-date.py
title_sentiment_file = "SentimentOfPost-5th-december.csv"  # File from title-sentiment.py
output_file = "WeightedSentimentAnalysis-5th-december.csv"  # Output Excel file

# Read the files
codeb_df = pd.read_csv(TestToExcel, usecols=["Title", "Compound Avg"])
reddit_df = pd.read_csv(DateWisePost, usecols=["Title", "Upvote Ratio"])
title_sentiment_df = pd.read_csv(title_sentiment_file, usecols=["Title", "Compound"])


print(codeb_df)
print(reddit_df)
print(title_sentiment_df)
# Merge the DataFrames on the 'Title' column
merged_df = codeb_df.merge(reddit_df, on="Title").merge(title_sentiment_df, on="Title")

# Remove duplicates (keep the first occurrence)
merged_df = merged_df.drop_duplicates(subset=["Title"], keep="first")

#print(merged_df)
print(merged_df.columns)
merged_df = merged_df.rename(columns={
    "Compound Avg": "Compound Avg of Comments",
    "Compound": "Compound of Posts"
})

# Verify the changes
print(merged_df.columns)
# Define weights for the weighted average calculation
weights = {
    "compound avg": 0.5,  # Weight for compound avg (sentiment of comments)
    "Upvote Ratio": 0.2,         # Weight for Score (post score)
    "compound": 0.3      # Weight for compound (sentiment of title)
}

# Calculate the final weighted value
merged_df["Final Value"] = (
    merged_df["Compound Avg of Comments"] * weights["compound avg"] +
    merged_df["Upvote Ratio"] * weights["Upvote Ratio"] +
    merged_df["Compound of Posts"] * weights["compound"]
)
def categorize_sentiment(value):
    if value > 0.25:
        return "High chance of price increase"
    elif 0.25 < value <= 0.05:
        return "Moderate chance of price increase"
    elif -0.05 <= value <= 0.05:
        return "Price will remain the same"
    elif -0.25 <= value < -0.05:
        return "Moderate chance of price decrease"
    else:
        return "High chance of price decrease"

# Apply the function to create the 'Final Sentiment' column
merged_df["Final Sentiment"] = merged_df["Final Value"].apply(categorize_sentiment)

# Save the final DataFrame to an Excel file
merged_df.to_csv(output_file, index=False)

print(f"Merged analysis saved to {output_file}.")  

