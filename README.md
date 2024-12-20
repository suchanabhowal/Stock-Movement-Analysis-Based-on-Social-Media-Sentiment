
# Stock Movement Analysis Based on Social Media Sentiment


## Introduction

This repository contains the source code for a Machine Learning model designed to analyze stock trends. The model scrapes  different posts and related comments of a social media page of any company from Reddit. It then performs sentiment analysis on posts and comments, and predicts whether a company's stock price is likely to move positively or negatively on a given day.


## Objective
The primary goal is to predict stock price trends based on the sentiments of reddit posts and comments generated by the ML model.
## Detailed Description of Files

- The first python script DateWisePost.py performs the initial scraping process from Reddit. 
- The next two files - CommentToText.py and TextToExcel.py files retrieves the comments on each post and find out the sentiment of them.
- The fourth file SentimentOfPost.py performs sentiment analysis on the title of the Reddit post.
- the fifth file combines the result of the first file, third file and fourth file to evaluaie the final sentiment.
### 1. DateWisePost.py

This script scrapes specified Reddit post(posts) for a particular date, which is provided at runtime.

Output File:
The script generates a csv file named {target-date}-post.csv, where  {target-date} corresponds to the date entered during runtime.

Columns in the Output File:

    Title: Reddit post
    Submission ID: Unique identifier for the post
    Author: Username of the post author
    Score: Reddit score of the post(Score = Upvote - downvote, where upvotes= number of likes, downvotes= number of dsilikes)
    Upvote Ratio: Ratio of upvotes to total votes
    Posted Date: Date when the post was posted
    URL: Link to the Reddit post
Example Input:
```yaml 
Enter the target date (YYYY-MM-DD): 2024-04-25
 ```
Example Output Filename:
```yaml 
 2024-12-05-post.csv
 ```

### 2. CommentToText.py

This script processes the URLs from the CSV file(2024-12-05-post.csv). It extracts the comments from each post and saves the data in a text file.

Output File : A text file, named according to the date of the posts (e.g., 5th-december.txt), is generated.
The file name has to be given manually based on the date.

Contents of the Text File:

    Title: Reddit post
    URL: Link to the Reddit post
    Username: Reddit username of the commenter
    First Comment: The comments on the post

### 3. TextToExcel.py

This script takes the text file generated in the previous stage(e.g., 5th-december.txt) as input. Using the VADER sentiment analysis model, it evaluates the sentiment of all comments for each post to determine the overall sentiment.

Output File:
    
     A CSV file named after the date of the posts being produced (e.g., 5th-December.csv).
The file name must be updated manually.
Contents of the Excel File:

    Title: Reddit post
    URL: Link to the Reddit post
    Positive Avg: Average positive sentiment score
    Negative Avg: Average negative sentiment score
    Neutral Avg: Average neutral sentiment score
    Compound Avg: Average sentiment score on the basis of above positive, negative, neutral averages
    Overall Sentiment: Categorical column which identifies overall sentiment as Positive, Negative, Neutral depending on the range selected by programmer.

### 4. SentimentOfPost.py

This script takes the CSV file generated in Step 1 (e.g., 2024-12-05.csv) as input and performs sentiment analysis on the titles of Reddit posts for the specified date.

Output File :
            
     A CSV file named SentimentOfPost-5th-december.csv, 
This output file contains the sentiment analysis results for the titles of each post.

Contents of the Excel File:

    Title: Reddit post
    Submission ID: Unique identifier for the post
    Author: Username of the post author
    Score: Reddit score of the post
    Upvote Ratio: Ratio of upvotes to total votes
    Posted Date: Date the post was created
    URL: Link to the Reddit post
    Positive: Positive sentiment score of the title
    Neutral: Neutral sentiment score of the title
    Negative: Negative sentiment score of the title
    Compound: Average sentiment score on the basis of above positive, negative, neutral averages

### 5. WeightedAnalysis.py

This script takes the following columns as input:
- Upvote Ratio from the CSV file generated in Stage 1 (2024_12_05.xlsx),
- Compound Avg from the CSV file generated in Stage 3 (5th-december.csv),
- Compound from the CSV file generated in Stage 4 (SentimentOfPost.csv)

It then performs a weighted scoring on these three parameters, assigning the highest weight to the sentiment of comments (i.e., the Compound Avg), and computes a final sentiment value based on this weighted scoring.

Output File:

    WeightedSentimentAnalysis-5th-december.csv

Contents of the Output File:

    Title: Reddit post
    Compound Average: Average compound sentiment score of the post
    Upvote Ratio: Ratio of upvotes to total votes
    Final Value: The final weighted sentiment value



## Environment Setup

Prerequisites

Python 3.9.18
    
Required Python Libraries:
- Pandas
- Openpyxl
- NLTK
- Vader Lexicon

## Install Required Libraries
``` bash
pip install pandas openpyxl nltk vaderSentiment
```

```python
import nltk
nltk.download('vader_lexicon')
```

## Reddit Client Setup

To access Reddit’s data, we need to set up a Reddit API client. We will need to create an application on Reddit and get the following details:

    Client ID
    Client Secret
    User Agent (Use your Reddit username)

After getting these details, we can use them to authenticate and interact with Reddit's API.

## How VADER Performs Sentiment Analysis
VADER (Valence Aware Dictionary and sEntiment Reasoner) is a widely used sentiment analysis tool that works particularly well for analyzing social media text, short text, and informal language. Below is a detailed explanation of how VADER operates, along with its input and output:

How VADER Works

- #### Rule-Based Sentiment Analysis
    VADER is a lexicon and rule-based sentiment analysis tool, specifically tuned for analyzing social media and informal text.
        It uses a predefined dictionary of words, where each word is assigned a sentiment score (positive, negative, or neutral).

- #### Word Sentiment Scores
    Words in the dictionary have scores ranging from -1 (negative sentiment) to +1 (positive sentiment).

- #### Intensifiers and Modifiers
    VADER adjusts sentiment scores based on modifiers such as adverbs (e.g., "very") or punctuation marks (e.g., exclamation points), which can amplify or diminish sentiment.

- #### Aggregate Scoring
    VADER combines individual word scores to calculate an overall sentiment score for the entire text. The final sentiment score represents the general emotional tone of the text.

Input

    Type of Input: A string (text input).
    Examples of input include the post title and comments from Reddit threads.

Output

The output is a dictionary containing four sentiment metrics:

    Positive:
        Represents the proportion of text conveying positive sentiment (value between 0 and 1).
        Higher values indicate stronger positive sentiment.

    Negative:
        Represents the proportion of text conveying negative sentiment (value between 0 and 1).
        Higher values indicate stronger negative sentiment.

    Neutral:
        Represents the proportion of text that is neutral (value between 0 and 1).
        Reflects text that is neither strongly positive nor strongly negative.

    Compound:
        A normalized score combining positive, negative, and neutral sentiment scores into a single value.
        Range: -1 (most negative) to +1 (most positive).
        Often used as the final sentiment indicator to represent the overall sentiment of the text.
## Future Improvements
This project provides a basic structure for predicting stock prices using sentiment analysis. While it performs the fundamental functionality, several improvements can be made to enhance its efficiency, scalability, and user-friendliness:

1. AUTOMATE THE WORKFLOW :- 
 - Integration of Files:
Combine all five files into a single pipeline, ensuring that each file automatically triggers the next in sequence.
-  Input Automation:
Automate the input handling such that providing a date as input initiates the entire process without manual intervention.
-  Backend Execution:
Perform all sentiment analysis, data merging, and calculations in the backend, ensuring smooth and invisible operations for the user.
-  Final Output:
Directly output the prediction (whether the stock price will increase or decrease the next day) based on the sentiment analysis.

2. Automate URL Input :- 
    The current setup requires manual input for URLs. Future improvements could include automating the URL extraction from Reddit posts or using a more dynamic method to gather Reddit URLs for specific stock-related threads.

3. Improve Sentiment Analysis Accuracy:- 
    Enhance sentiment analysis by incorporating other sentiment analysis models or fine-tuning the existing VADER model. Combining VADER with deep learning models like BERT for sentiment analysis could improve accuracy.

## Conclusion

This project demonstrates the potential of using sentiment analysis to predict stock price movements by analyzing Reddit discussions. By leveraging VADER sentiment analysis on post titles and comments, we can assess public sentiment toward specific stocks and make predictions on their daily performance. While the current model provides a solid foundation, future improvements such as automating data collection, integrating additional data sources, and implementing time-series forecasting will enhance its accuracy and scalability.