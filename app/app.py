from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/healthz')
def healthz():
	return "OK"

@app.route('/')
def home():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
