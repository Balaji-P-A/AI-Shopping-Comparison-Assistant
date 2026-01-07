from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download only once
nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(reviews):
    """
    reviews: list of strings
    returns: sentiment summary
    """
    if not reviews:
        return "No reviews available"

    positive = 0
    negative = 0
    neutral = 0

    for review in reviews:
        score = analyzer.polarity_scores(review)["compound"]
        if score >= 0.05:
            positive += 1
        elif score <= -0.05:
            negative += 1
        else:
            neutral += 1

    total = len(reviews)
    return f"{int((positive/total)*100)}% positive, {int((negative/total)*100)}% negative"
