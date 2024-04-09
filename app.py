# app.py (Flask App)
from flask import Flask, request, jsonify
from pytube import YouTube

app = Flask(__name__)

@app.route('/get_audio_link', methods=['POST'])
def get_audio_link():
    data = request.json
    yt_url = data['youtube_link']
    #print(yt_url)
    yt = YouTube(yt_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    print(audio_stream)
    stream_url = audio_stream.url
    print(stream_url)
    return jsonify({'audio_stream_url': stream_url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
