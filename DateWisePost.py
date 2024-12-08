import praw
import pandas as pd
from datetime import datetime

# Initialize PRAW
UG = " "
reddit = praw.Reddit(
        client_id='',
        client_secret='',
        user_agent=UG,
    )

# Initialize lists to store data
titles = []
submission_ids = []
authors = []
scores = []
upvote_ratios = []
created_dates = []
urls = []  # List to store correct post URLs

# Specify the target date
target_date = input("Enter the target date in YYYY-MM-DD format: ")

# Fetch data from the subreddit
for submission in reddit.subreddit('teslamotors').hot(limit=100):
    # Convert the Unix timestamp to a readable date
    post_date = datetime.utcfromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S')
    post_date_only = post_date.split(" ")[0]  # Extract just the date in 'YYYY-MM-DD' format
    
    # Check if the post matches the target date
    if post_date_only == target_date:
        titles.append(submission.title)
        submission_ids.append(submission.id)
        authors.append(submission.author)
        scores.append(submission.score)
        upvote_ratios.append(submission.upvote_ratio)
        created_dates.append(post_date)
        # Construct the full URL of the post
        urls.append(f"https://www.reddit.com{submission.permalink}")

# Check if any posts were found
if titles:
    # Create a DataFrame
    data = {
        "Title": titles,
        "Submission ID": submission_ids,
        "Author": authors,
        "Score": scores,
        "Upvote Ratio": upvote_ratios,
        "Posted Date": created_dates,
        "URL": urls  # Include the correct URL column
    }
    df = pd.DataFrame(data)

    # Save to a CSV file
    output_file = f"{target_date.replace('-', '_')}_posts.csv"
    df.to_csv(output_file, index=False)

    print(f"Filtered data for {target_date} saved to {output_file}.")
else:
    print(f"No posts found for {target_date}.")
