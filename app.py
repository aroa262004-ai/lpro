from flask import Flask

import os

app = Flask(__name__)

@app.route('/')
def inicio():
    return "<h1>El mejor proyecto de LPRO</h1>"




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
