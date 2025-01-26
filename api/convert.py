import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_video_key():
    response = requests.get(
        'https://api.mp3youtube.cc/v2/sanity/key',
        headers={
            'Referer': 'https://y2mate.lol/',
            'Origin': 'https://y2mate.lol'
        }
    )
    if response.status_code == 200:
        return response.json().get('key', '')
    else:
        return None

@app.route('/api/convert', methods=['POST'])
def convert_video_to_mp3():
    data = request.json
    video_link = data.get('link')

    if not video_link:
        return jsonify({'error': 'No video link provided'}), 400

    key = get_video_key()
    if not key:
        return jsonify({'error': 'Failed to fetch the key'}), 500

    conversion_data = {
        'link': video_link,
        'format': 'mp3',
        'audioBitrate': '128',
        'videoQuality': '720',
        'vCodec': 'h264'
    }
    headers = {
        'Referer': 'https://y2mate.lol/',
        'Origin': 'https://y2mate.lol',
        'key': key,
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(
        'https://api.mp3youtube.cc/v2/converter',
        headers=headers,
        data=conversion_data
    )

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({'error': 'Error converting video', 'details': response.text}), 500
