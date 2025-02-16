from flask import Flask, render_template
import requests
import json
import random

app = Flask(__name__)

def get_meme():
    try:
        # Using a different meme API that doesn't require authentication
        url = "https://api.imgflip.com/get_memes"
        response = json.loads(requests.request("GET", url).text)
        memes = response['data']['memes']
        # Select a random meme from the list
        meme = random.choice(memes)
        return meme['url'], meme['name']
    except Exception as e:
        return "https://i.imgur.com/6yYM1KL.png", "fallback_meme"

@app.route('/')
def home():
    meme_pic, meme_name = get_meme()
    return render_template('meme_index.html',
                         meme_pic=meme_pic,
                         meme_name=meme_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
