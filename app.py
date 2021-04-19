from datetime import datetime
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Текущее время (✿◡‿◡) --> ' + str(datetime.now().time())


if __name__ == '__main__':
    app.run()
