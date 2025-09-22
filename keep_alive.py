import time
import requests

# Replace with your panel/site URL
url = "https://idx.google.com/vps123-49539420"

while True:
    try:
        requests.get(url)
        print(f"Pinged {url}")
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(240)  # Wait 4 minutes before next ping

