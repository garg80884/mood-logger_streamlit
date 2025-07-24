import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Create model directory if it doesn't exist
os.makedirs("model", exist_ok=True)

# Load emotion labels (each line = one emotion)
with open("goemotions/emotions.txt", "r") as f:
    id2label = [line.strip() for line in f]

# Load training data
df = pd.read_csv("goemotions/train.tsv", sep="\t", header=None, names=["text", "labels", "split"])

# Convert multi-label IDs to first label only (for basic model)
def extract_first_label(label_str):
    try:
        first_id = int(label_str.split(",")[0])
        return id2label[first_id]
    except:
        return None  # skip malformed

df["label"] = df["labels"].apply(extract_first_label)
df = df.dropna(subset=["label"])  # drop rows with no valid label

# Separate text and labels
X = df["text"]
y = df["label"]

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer(max_features=5000)
X_vect = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_vect, y)

# Save model and vectorizer
joblib.dump(model, "model/saved_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("✅ Model and vectorizer saved to /model/")
