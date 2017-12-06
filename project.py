
import os
from flask import Flask, session, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '3028876288'

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)

# defining the database tables
class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    description = db.Column(db.Text)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movies')
def show_all_movies():
    movies = Movie.query.all()
    return render_template('movies-all.html', movies=movies)

@app.route('/movie/add', methods=['GET', 'POST'])
def add_movies():
    if request.method == 'GET':
        return render_template('movies-add.html')
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        intro = request.form['intro']

        # insert the data into the database
        movie = Movie(name=name, intro=intro)
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('show_all_movies'))

@app.route('/movie/edit/<int:id>', methods=['GET', 'POST'])
def edit_movie(id):
    movie = Movie.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('movie-edit.html', movie=movie)
    if request.method == 'POST':
        # update data based on the form data
        movie.title = request.form['title']
        movie.description = request.form['description']
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_movies'))

@app.route('/members')
def members_page():
    return render_template('members.html')


if __name__ == '__main__':
    app.run(debug=True)
