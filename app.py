from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "Heelo World"

@app.route('/smita')

def smita():
    return "Heelo Smita !!"

if __name__ == '__main__':
    app.run(debug=True)

