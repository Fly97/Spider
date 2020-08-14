from flask import Flask
import time

app = Flask(__name__)


@app.route('/zhx')
def index_bobo():
    time.sleep(2)
    return 'Hello zhx'


@app.route('/lst')
def index_jay():
    time.sleep(2)
    return 'Hello lst'


@app.route('/zxy')
def index_tom():
    time.sleep(2)
    return 'Hello zxy'


if __name__ == '__main__':
    app.run(threaded=True)
