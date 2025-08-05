from joblib import load
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'phishing_model.joblib')
model = load(MODEL_PATH)

def predict_url(features):
    prob = model.predict_proba(features)[0]  # [prob_safe, prob_phishing]
    print("🔍 Prediction probabilities:", prob)
    return int(prob[1] > 0.6)  # Phishing hole 1, na hole 0
