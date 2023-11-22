from flask import Flask, render_template
import requests


app = Flask(__name__)

# Routes and functionality will be added here

def fetch_random_meme():
    response = requests.get("https://meme-api.com/gimme")
    meme_data = response.json()
    meme_image_url = meme_data['url']
    meme_caption = meme_data['title']
    
    return meme_image_url, meme_caption

@app.route('/')
def home():
    meme_image_url, meme_caption = fetch_random_meme()
    return render_template('index.html', meme_image_url=meme_image_url, meme_caption=meme_caption)

@app.route('/generate_meme')
def generate_meme():
    meme_image_url, meme_caption = fetch_random_meme()
    return {'meme_image_url': meme_image_url, 'meme_caption': meme_caption}

if __name__=='__main__':
    app.run()