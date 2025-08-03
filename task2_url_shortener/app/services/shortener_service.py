import random, string, time
from urllib.parse import urlparse

# In-memory database
db = {}

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme in ["http", "https"], result.netloc])
    except:
        return False

def generate_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def shorten_url(url):
    if not url or not is_valid_url(url):
        return None, "Invalid URL"
    
    # Ensure unique code
    code = generate_code()
    while code in db:
        code = generate_code()

    db[code] = {
        "url": url,
        "clicks": 0,
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%S")
    }
    return {
        "short_code": code,
        "short_url": f"http://localhost:5000/{code}"
    }, None

def get_original_url(code):
    if code in db:
        db[code]["clicks"] += 1
        return db[code]["url"]
    return None

def get_stats(code):
    if code in db:
        return {
            "url": db[code]["url"],
            "clicks": db[code]["clicks"],
            "created_at": db[code]["created_at"]
        }
    return None
