from transformers import pipeline

def run(texts):
    classifier = pipeline("sentiment-analysis")
    results = classifier(texts)
    return [r["label"] for r in results]
