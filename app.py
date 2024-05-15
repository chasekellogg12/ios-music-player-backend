import time
from flask import Flask, request, jsonify
from pytube import YouTube
import redis 
import os

app = Flask(__name__)

# Setup Redis connection
redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379')
cache = redis.Redis.from_url(redis_url)

@app.route('/', methods=['GET'])
def test():
    return "Welcome"

@app.route('/get_audio_link', methods=['POST'])
def get_audio_link():
    data = request.json
    #yt_url = data['youtube_link']
    yt_url = "https://www.youtube.com/watch?v=id0kbyKCG8c&ab_channel=VideoGamesMusic" # - for testing
    start_time = time.time()  # Start profiling

    # Check cache first
    cached_url = cache.get(yt_url)
    if cached_url:
        end_time = time.time()  # End profiling
        duration = end_time - start_time
        print(f"Cache hit: {duration} seconds")
        return jsonify({'audio_stream_url': cached_url.decode('utf-8'), 'cached': True, 'duration': duration})
    
    # If not in cache, fetch from YouTube
    yt = YouTube(yt_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    stream_url = audio_stream.url
    
    # Store the result in cache
    cache.set(yt_url, stream_url, ex=3600)  # Cache for 1 hour

    end_time = time.time()  # End profiling
    duration = end_time - start_time
    print(f"Cache miss: {duration} seconds")
    
    return jsonify({'audio_stream_url': stream_url, 'cached': False, 'duration': duration})

if __name__ == '__main__':
    app.run(debug=True)