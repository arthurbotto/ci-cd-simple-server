import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_home():
    return "Hello, world!"

@app.route('/hero', methods=['GET'])
def get_hero_msg():
    return "I am a CI-CD Hero , I guess.."

if __name__ == '__main__':
    app.run(
      debug=True,
      host="0.0.0.0" # Listen for connections _to_ any server
    )
