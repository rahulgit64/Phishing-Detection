from imblearn.over_sampling import SMOTE
from sklearn.tree import DecisionTreeClassifier
from joblib import dump
import pandas as pd
import os

# Paths
DATASET_PATH = os.path.join(os.path.dirname(__file__), '..', 'dataset', 'sample_phishing_data.csv')
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'phishing_model.joblib')

# Load dataset
df = pd.read_csv(DATASET_PATH)

# Drop unnamed index column if exists
if 'Unnamed: 0' in df.columns:
    df = df.drop(['Unnamed: 0'], axis=1)

# Clean label column
df = df.dropna(subset=['Phising'])
df = df[df['Phising'].isin([0, 1])]

# Feature list with new KeywordFlag feature
required_features = [
    'NumDots', 'UrlLength', 'AtSymbol', 'NumDash', 'NumPercent',
    'NumQueryComponents', 'IpAddress', 'HttpsInHostname',
    'PathLevel', 'PathLength', 'NumNumericChars', 'KeywordFlag'
]

# Separate features and label
X = df[required_features]
y = df['Phising']

# Balance dataset using SMOTE
sm = SMOTE(random_state=42)
X_resampled, y_resampled = sm.fit_resample(X, y)

# Train Decision Tree on balanced data
clf = DecisionTreeClassifier()
clf.fit(X_resampled, y_resampled)

# Save the model
dump(clf, MODEL_PATH)

print("✅ Balanced model trained and saved at", MODEL_PATH)
