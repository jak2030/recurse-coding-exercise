from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/laws')
def get_law():
    return jsonify('Such a good law.')