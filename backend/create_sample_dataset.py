import pandas as pd
import re
from urllib.parse import urlparse
import os

# Sample URLs (phishing + safe)
url_list = [
    "https://secure-login-bank.com/login",
    "https://www.wikipedia.org",
    "http://paypal.com@scamverify.ru",
    "https://www.google.com",
    "https://login-update-free.com",
    "http://192.168.0.1/login",
    "https://amazon.com",
    "https://free-bonus-gifts.net",
    "https://stackoverflow.com",
    "https://verify-account-security.com"
]

def extract_features(url):
    parsed = urlparse(url)
    hostname = parsed.hostname or ""

    num_dots = url.count('.')
    url_length = len(url)
    at_symbol = 1 if "@" in url else 0
    num_dash = url.count('-')
    num_percent = url.count('%')
    num_query_components = len(parsed.query.split('&')) if parsed.query else 0
    ip_address = 1 if re.match(r'^\d{1,3}(\.\d{1,3}){3}$', hostname) else 0
    https_in_hostname = 1 if 'https' in hostname.lower() else 0
    path_level = parsed.path.count('/')
    path_length = len(parsed.path)
    num_numeric_chars = len(re.findall(r'\d', url))

    suspicious_keywords = ['secure', 'login', 'verify', 'account', 'update', 'free', 'bonus']
    keyword_flag = 1 if any(k in hostname.lower() for k in suspicious_keywords) else 0

    return [
        num_dots, url_length, at_symbol, num_dash, num_percent,
        num_query_components, ip_address, https_in_hostname,
        path_level, path_length, num_numeric_chars, keyword_flag
    ]

# Build dataset
phishing_indicators = [
    'secure-login-bank.com',
    'scamverify.ru',
    'login-update-free.com',
    'free-bonus-gifts.net',
    'verify-account-security.com'
]

data = []
for url in url_list:
    features = extract_features(url)
    label = 1 if any(ind in url for ind in phishing_indicators) else 0
    data.append(features + [label, url])

columns = [
    'NumDots', 'UrlLength', 'AtSymbol', 'NumDash', 'NumPercent',
    'NumQueryComponents', 'IpAddress', 'HttpsInHostname',
    'PathLevel', 'PathLength', 'NumNumericChars', 'KeywordFlag', 'Phising', 'Url'
]

df = pd.DataFrame(data, columns=columns)

# Save to CSV
output_path = os.path.join(os.path.dirname(__file__), '..', 'dataset', 'sample_phishing_data.csv')
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)

print("✅ Sample dataset created with KeywordFlag and saved as 'dataset/sample_phishing_data.csv'")
print(df)
