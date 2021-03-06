"""CRUD operations."""

from datetime import datetime
from model import db, User, Movie, Rating, connect_to_db

if __name__ == '__main__':
    from server import app
    connect_to_db(app)


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def get_movies():
    """Returns all movies"""

    return Movie.query.all()


def create_rating(user, movie, score):
    """Create and return a rating."""

    rating = Rating(user=user, movie=movie, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating

def get_movie_by_id(movie_id):
    """Return movie with the movie's ID"""

    movie_id_q = Movie.query.get(movie_id)

    return movie_id_q

def get_users():
    """Return all users"""

    return User.query.all()

def get_user_by_id(user_id):
    """Return user profile"""

    user_id_q = User.query.get(user_id)

    return user_id_q

def get_user_by_email(email):
    """Return user if email exists; otherwise None"""

    return User.query.filter(User.email == email).first()