# from nltk.sentiment import SentimentIntensityAnalyzer

# def run(texts):
#     sia = SentimentIntensityAnalyzer()
#     results = []
#     for t in texts:
#         score = sia.polarity_scores(t)["compound"]
#         sentiment = "positive" if score > 0 else "negative" if score < 0 else "neutral"
#         results.append(sentiment)
#     return results


from nltk.sentiment import SentimentIntensityAnalyzer

def run(texts):
    sia = SentimentIntensityAnalyzer()
    results = []

    for t in texts:
        if not t.strip():
            continue
        score = sia.polarity_scores(t)["compound"]
        sentiment = (
            "positive" if score > 0
            else "negative" if score < 0
            else "neutral"
        )
        results.append(sentiment)

    return results
