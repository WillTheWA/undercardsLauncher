# Python support for opening a wrapped undercards web app
import webview
import os
from flask import Flask, render_template

app = Flask(__name__)

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

@app.route('/')

def index():
    return render_template('main.html')

if __name__ == '__main__':
    # Run the Flask app in a separate thread
    from threading import Thread
    thread = Thread(target=lambda: app.run(port=5000, debug=False, use_reloader=False))
    thread.daemon = True
    thread.start()

    window = webview.create_window('Undercards', 'http://127.0.0.1:5000', fullscreen=True)

    webview.start()