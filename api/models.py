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

	# Init this class
	def __init__(self, id=None, name=None):
		self.id = id
		self.name = name

	# Function to return data as dict
	def to_json(self):
	        return dict(facebookId=self.id, name=self.name)

User.__table__