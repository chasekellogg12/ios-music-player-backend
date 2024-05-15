import requests
import json

# URL for the Flask app
url = "https://musicplayer-d1169b8bdeeb.herokuapp.com/get_audio_link"

# Data to be sent in the POST request
data = {
    "youtube_link": "https://www.youtube.com/watch?v=whNOfvyPpaM&ab_channel=lwilkers"
}

# Send the POST request
response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

# Print the response
print(response.json())