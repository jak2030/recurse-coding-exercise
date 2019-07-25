from flask import Flask
app = Flask(__name__)

@app.route('/')
def get_law():
    return 'Such a good law.'