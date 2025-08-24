from textblob import TextBlob

texts= [
    "I love this phone, the camera quality is amazing!",
    "This movie was so boring and too long.",
    "I ordered the book yesterday and it arrived today."
]

for sentence in texts:
    blob = TextBlob(sentence)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        result = "Positive 🙂"
    elif sentiment < 0:
        result = "Negative 😞"
    else:
        result = "Neutral 😐"

    print(f"Text: {sentence}\nSentiment:{result}\n")
