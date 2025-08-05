# train_model.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from joblib import dump
import os

# ✅ Path config
DATASET_PATH = os.path.join(os.path.dirname(__file__), '..', 'dataset', 'phishing_data.csv')
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'phishing_model.joblib')

# 📥 Load dataset
df = pd.read_csv(DATASET_PATH)

# ✅ Optional: Print phishing ratio
label_counts = df['label'].value_counts(normalize=True)
print("Phishing ratio: {:.2f}".format(label_counts.get(1, 0)))

# 🎯 Features & Labels
X = df.drop(['url', 'label'], axis=1)
y = df['label']

# 🧠 Train model (more robust classifier)
clf = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
clf.fit(X, y)

# 💾 Save model
dump(clf, MODEL_PATH)

print("✅ Model trained and saved at", MODEL_PATH)
