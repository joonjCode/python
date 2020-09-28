from dataclasses import dataclass
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# @dataclass
class Movie(Base):
	# create table
	__tablename__ = 'movies'

	# Create column
	id = Column(Integer, primary_key=True)
	name = Column(String)
	genre = Column(String)
	desc = Column(String)
	year = Column(Integer, nullable=True)

	def __repr__ (self):
		return f'<movie name = {self.name}'



engine = create_engine('sqlite:///app.db') # mysql, postgres
Session = sessionmaker(bind = engine)
my_sess = Session()

# Add table to db
# Base.metadata.create_all(engine)

# movie1 = Movie(name='interstellar', genre='scifi')
# movie2 = Movie(name='Martian', genre='scifi')

# # prepare
# my_sess.add(movie1, movie2)
# # commit
# my_sess.commit()

# Retrieve
# movie_a = my_sess.query(Movie).get(1)
# print(movie_a)

# Get all
# qs = my_sess.query(Movie).all()
# print(qs)

# filter by column value
# qs = my_sess.query(Movie).filter_by(name = 'interstellar').all()

# filter by column value containing sth
# qs = my_sess.query(Movie).filter(Movie.name.contains('Inter')).all()


# Update
movie_a = my_sess.query(Movie).get(1)
movie_a.desc = 'great movie'
# my_sess.commit()
print(movie_a.id, movie_a.desc)
# qs = my_sess.query(Movie).filter(Movie.name.contains('Inter')).all()

# print(qs)

# Delete
# my_sess.delete(movie_a)
# session.commit()
# session.flush()