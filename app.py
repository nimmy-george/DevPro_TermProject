import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Use an absolute path for the SQLite database
project_dir = os.path.dirname(os.path.abspath(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(project_dir, "database.db")}'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

# Database initialization
def init_db():
    db.create_all()

# Route for the home page
@app.route('/')
def home():
    users = User.query.all()
    return render_template('index.html', users=users)

# Route for adding a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form['username']
    email = request.form['email']

    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('home'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=4000)
