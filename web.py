from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return 'hello, this is my sample python web app ... my first review edit NNN'
