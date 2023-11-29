# app.py
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__, template_folder='app_temp')

messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/post_message', methods=['POST'])
def post_message():
    message = request.form.get('message')
    if message and len(message) <= 128:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        messages.insert(0, {'message': message, 'timestamp': timestamp})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)