import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.feature_extraction.text import CountVectorizer

# Step 1: Load the log file
with open("../logs/app.log", "r") as file:
    logs = file.readlines()

# Step 2: Convert logs to feature vectors using bag-of-words
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(logs)

# Step 3: Apply Isolation Forest
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(X)

# Step 4: Predict anomalies
predictions = model.predict(X)  # -1 = anomaly, 1 = normal

# Step 5: Show anomalous logs
print("=== Anomalies Detected by ML ===")
for i, prediction in enumerate(predictions):
    if prediction == -1:
        print(logs[i].strip())
