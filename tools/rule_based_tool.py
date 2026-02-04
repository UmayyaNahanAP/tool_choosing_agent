POSITIVE = ["good", "excellent", "awesome", "nice"]
NEGATIVE = ["bad", "terrible", "worst", "poor"]

def run(texts):
    results = []
    for t in texts:
        t = t.lower()
        if any(w in t for w in POSITIVE):
            results.append("positive")
        elif any(w in t for w in NEGATIVE):
            results.append("negative")
        else:
            results.append("neutral")
    return results
