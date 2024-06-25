#!/usr/bin/env python3
"""User Model"""


from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)


# Example usage:
if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    
    # Assuming you have a SQLite database named 'test.db'
    engine = create_engine('sqlite:///test.db')
    Base.metadata.create_all(engine)
    
    # Create a new session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Example of adding a new user
    new_user = User(
        email="example@example.com",
        hashed_password="hashed_password_example"
    )
    session.add(new_user)
    session.commit()

    print(User.__tablename__)

    for column in User.__table__.columns:
        print("{}: {}".format(column, column.type))
