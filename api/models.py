from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Model base
Base = declarative_base()

# User model
class User(Base):
	# Table name
	__tablename__ = 'users'
	# Fields
	id = Column(Integer, primary_key=True)
	name = Column(String(50))
	username = Column(String(50))
	gender = Column(String(10))

	# Init this class
	def __init__(self, id=None, name=None, username=None, gender=None):
		self.id = id
		self.name = name
		self.username = username
		self.gender = gender

	# Function to return data as dict
	def to_json(self):
	        return dict(facebookId=self.id, username=self.username,
	                name=self.name, gender=self.gender)

User.__table__