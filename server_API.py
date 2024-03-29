import web
import json
from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route('/')
def index():
    return 'Under construction!'


@app.route('/getinfo')
def get_info():
    with open("person_info.txt", "rb") as fin:
        person_info = fin.read()
        # print person_info
        return person_info


@app.route('/setauth', methods=['POST'])
def set_auth():
    with open("auth_stat.txt", "w") as f:
        f.write("1")
    return "Auth set!"


@app.route('/resetauth', methods=['POST'])
def set_auth():
    with open("auth_stat.txt", "w") as f:
        f.write("0")
    return "Auth reset!"


@app.route('/getimg')
def get_img():
    return send_from_directory('video', 'test.jpg')