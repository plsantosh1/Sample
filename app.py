from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome to this Pipeline Demo!!'


@app.route('/today')
def today():
    return 'Current Date:{dt}'.format(dt=datetime.today().strftime('%d-%m-%Y'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
