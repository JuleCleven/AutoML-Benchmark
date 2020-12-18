from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///AutoML.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('form.html')

if __name__ == '__main__':
    app.run()