import praw
import re

# Initialize PRAW with your credentials
UG = " "
reddit = praw.Reddit(
    client_id=' ',
    client_secret=' ',
    user_agent=UG,
)

# List of URLs to process
# URLS OF 5 TH DECEMBER
#change the urls according to the date 
urls = [ " https://www.reddit.com/r/teslamotors/comments/1h7b3kb/cybertruck_production_halt_at_giga_texas_is_due/",
        " https://www.reddit.com/r/teslamotors/comments/1h7cske/teslas_nacs_set_to_become_official_us_federal_ev/",
        " https://www.reddit.com/r/teslamotors/comments/1h7kx90/new_tesla_app_for_apple_watch/",
        " https://www.reddit.com/r/teslamotors/comments/1h76v3c/tesla_engineer_talks_about_the_cybercab_to_a/"

]
# File to save comments
output_file = "5th-december.txt"

# Scrape data for each URL
with open(output_file, "w", encoding="utf-8") as file:
    for url in urls:
        # Fetch the submission
        submission = reddit.submission(url=url)
        submission.comments.replace_more(limit=0)

        # Write submission title to the file
        file.write(f"Post Title: {submission.title}\n")
        file.write(f"URL: {url}\n\n")

        # Dictionary to store the first comment from each unique user
        user_comments = {}
        for comment in submission.comments:
            user = comment.author.name if comment.author else None  # Handle deleted users
            if user and user not in user_comments:
                # Remove links and clean the comment
                clean_comment = re.sub(r'http\S+', '', comment.body).strip()
                user_comments[user] = clean_comment

        # Write comments to the file
        for user, comment in user_comments.items():
            file.write(f"User: {user}\n")
            file.write(f"First Comment: {comment}\n\n")

        # Separator between posts
        file.write("=" * 50 + "\n\n")

print(f"Comments from all posts saved to {output_file}.")




