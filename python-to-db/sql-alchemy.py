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
	# name:str = 'unknown' #col
	# genre:str = 'Action'
	# year: int = None
	# def __init__(self, name= '', *args, **kwargs):
	# 	super().__init__(*args, **kwargs)
	# 	self.name = name

# movie1 = Movie(name = 'interstellar', genre='sf')
# print(movie1)


data = [{
	'name':'interstellar',
	'genre':'sf'
},{
	'name':'The martian',
	'genre' : 'sf'
}
]

engine = create_engine('sqlite:///app.db') # mysql, postgres
Session = sessionmaker(bind = engine)
my_sess = Session()

# Add table to db
Base.metadata.create_all(engine)

movie1 = Movie(name='interstellar', genre='scifi')
movie2 = Movie(name='Martian', genre='scifi')

# prepare
my_sess.add(movie1, movie2)
# commit
my_sess.commit()

