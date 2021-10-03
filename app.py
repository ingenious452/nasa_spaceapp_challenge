from flask import Flask, render_template
from dataHandler import process_data, request_data, 
app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    url = 'https://celestrak.com//NORAD/elements/gp.php'
    request_data(url, '3LE')
    process_data()
    return render_template('index.html')


if __name__ == '__main__':
    app.run()