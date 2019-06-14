import requests
import time


url = 'http://localhost:8000/'
payload = "welcome world"
now = int(time.time())

r = requests.post(url, data=payload)

print("timestamp: " + str(now) + " | message sent! - status: " + str(r.status_code))

