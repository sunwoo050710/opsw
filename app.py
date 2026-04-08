from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Hello DevOps Sentiment API")

class TextInput(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Hello DevOps!"}

@app.post("/predict")
def predict_sentiment(data: TextInput):
    text = data.text.strip()

    positive_words = ["좋다", "행복", "사랑", "최고", "재밌다", "good", "happy", "love", "great"]
    negative_words = ["싫다", "짜증", "화난다", "최악", "별로", "bad", "angry", "hate", "terrible"]

    score = 0
    for word in positive_words:
        if word in text:
            score += 1
    for word in negative_words:
        if word in text:
            score -= 1

    if score > 0:
        sentiment = "positive"
    elif score < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return {
        "input_text": text,
        "sentiment": sentiment,
        "score": score
    }