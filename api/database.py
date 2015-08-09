from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import Base

# Create the connection engine
engine = create_engine('sqlite:///sqlite/data.db', echo=False)
# Create the database session
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Function to generate the database
def init_db():
	Base.metadata.create_all(engine)