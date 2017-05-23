
import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, jsonify, request,send_from_directory,abort
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('',filename,as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
