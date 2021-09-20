import os
import niconico_dl
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

def check_url(url):
    nico = niconico_dl.NicoNicoVideo(url)

    try:
        nico.get_info()
        return True
    except:
        return False

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')

    if check_url(url):
        with niconico_dl.NicoNicoVideo(url) as nico:
            return redirect(nico.get_download_link())
    else:
        return "Error: Invalid URL"

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)