from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import Model

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

def init_db() -> None:
    with app.app_context():
        db.create_all()

@app.route('/')
def home() -> str:
    users: List[User] = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['POST'])
def add_user() -> str:
    username: str = request.form['username']
    email: str = request.form['email']

    new_user: User = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('home'))

if __name__ == '__main__':
    init_db()
    app.run(debug=False, port=4000)
