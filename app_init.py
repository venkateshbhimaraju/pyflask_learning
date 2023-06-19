from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/newpage')
def new_page():
    return render_template('newpage.html')

if __name__ == '__main__':
    app.run(port=5001)
