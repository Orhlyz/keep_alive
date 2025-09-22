import time
import requests

# Replace with your panel/site URL
url = "https://your-panel.com/heartbeat"

while True:
    try:
        requests.get(url)
        print(f"Pinged {url}")
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(240)  # Wait 4 minutes before next ping
