import re
from urllib.parse import urlparse

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

    # Suspicious keyword detection (new feature)
    suspicious_keywords = ['secure', 'login', 'verify', 'account', 'update', 'free', 'bonus']
    keyword_flag = 1 if any(k in hostname.lower() for k in suspicious_keywords) else 0

    return [[
        num_dots, url_length, at_symbol, num_dash, num_percent,
        num_query_components, ip_address, https_in_hostname,
        path_level, path_length, num_numeric_chars, keyword_flag
    ]]
