from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('profile.html')

@app.route('/rawdata')
def rawdata():
    file = open('raw_json.txt', 'r')
    data = file.read()
    return data

if __name__ == "__main__":
    app.run(debug=True)
