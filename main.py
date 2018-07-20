from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Code Update by Faisal in Dev!'

if __name__ == '__main__':
  app.run()
