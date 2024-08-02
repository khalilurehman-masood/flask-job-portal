from flask import Flask

app = Flask(__name__)

#app.route decorator,with '/' as the argument
@app.route("/")
def hello_world():
  return 'hello world'

if __name__ == '__main__':
  app.run(host = '0.0.0.0',debug = True)