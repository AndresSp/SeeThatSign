import os
from flask import send_from_directory, render_template
from giv import app

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template('index.html')