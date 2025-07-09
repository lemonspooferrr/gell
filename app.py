
from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    cid = request.args.get('cid', '')
    to = request.args.get('to', '')
    return render_template('index.html', cid=cid, to=to)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
