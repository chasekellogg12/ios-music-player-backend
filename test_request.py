import requests
import json

# URL for the local Flask app
url = "http://127.0.0.1:5000/get_audio_link"

# Data to be sent in the POST request
data = {
    "youtube_link": "https://www.youtube.com/watch?v=id0kbyKCG8c&ab_channel=VideoGamesMusic"
}

# Send the POST request
response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

# Print the response
print(response.json())