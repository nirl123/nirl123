import os
from flask import Flask, request, render_template
from datetime import datetime  
import calendar
import time

app = Flask(__name__)

@app.route('/api/chat/<room>', methods=['GET'])
def get_chat(room):
    filename = f'{room}.txt'
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            chat_content = file.read()
        return chat_content
    return ''

@app.route('/api/chat/<room>', methods=['POST'])
def post_message(room):
    str_date_time = get_timestamp()
    message = f"{str_date_time} || username:{request.form['username']} --> massage:{request.form['msg']}\n"
    filename = f'{room}.txt'
    with open(filename, 'a') as file:
        file.write(message)
    return 'Message sent'

@app.route('/<room>')
def chat_room(room):
    return render_template('index.html', current_room=room)

@app.route('/')
def index():
    return chat_room('general')  # Default to 'general' room


def get_timestamp():

    current_GMT = time.gmtime()
    time_stamp = calendar.timegm(current_GMT)
    from datetime import datetime  
    date_time = datetime.fromtimestamp(time_stamp)
    str_date_time = date_time.strftime("%d-%m-%Y %H:%M:%S")
    return str_date_time


if __name__ == '__main__':
    app.run(debug=True)
