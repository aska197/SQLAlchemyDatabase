from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:mysecretreira@localhost:5432/postgres')
Session = sessionmaker(bind=engine)
session = Session()
