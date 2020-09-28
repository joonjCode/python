import pandas as pd
import sqlacodegen
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


# sqlacodegen sqlite:///app.db
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class MovieApp2(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    genre = Column(String)
    desc = Column(String)
    year = Column(Integer)

    def __repr__(self):
        return f'<movie name = {self.name}'

engine = create_engine('sqlite:///app.db')
Session = sessionmaker(bind=engine)
session = Session()

qs = session.query(MovieApp2).all()
# print(qs)


for old_obj in qs:
	movie_obj = MovieApp2(name=old_obj.name, genre =old_obj.genre, year = old_obj.year)
	print(movie_obj.name)
	my_sess.add(movie_obj)
my_sess.commit()

old_engine = create_engine('sqlite:///app.db')
old_df = pd.read_sql_table('movies', old_engine)
print(old_df)