from flask import Flask, request

from fingerprint import Fingerprint

app = Flask(__name__)


@app.route('/fingerprint', methods=['POST'])
def fingerprint_router():
    data = request.get_json()
    url = data['url']
    fing = Fingerprint().get_all(url)
    return fing


@app.route('/fingerprint/md5', methods=['POST'])
def fingerprint_md5_router():
    data = request.get_json()
    url = data['url']
    fing = Fingerprint().get_md5(url)
    return fing


@app.route('/fingerprint/sha1', methods=['POST'])
def fingerprint_sha1_router():
    data = request.get_json()
    url = data['url']
    fing = Fingerprint().get_sha1(url)
    return fing


@app.route('/fingerprint/sha256', methods=['POST'])
def fingerprint_sha256_router():
    data = request.get_json()
    url = data['url']
    fing = Fingerprint().get_sha256(url)
    return fing


app.run()
