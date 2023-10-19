from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://username:password@db:5432/fastapi_db', echo=True)
Session = sessionmaker(engine)
