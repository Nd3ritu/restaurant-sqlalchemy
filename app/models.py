from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column,Integer, String,ForeignKey


Base = declarative_base()

engine = create_engine("sqlite:///restaurants.db") #make connection to database
Base.metadata.create_all(engine)  #creates tables
Session = sessionmaker(bind=engine)
session = Session() # for interaction with database

                   #Data Models
class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer(), primary_key = True)
    name = Column(String(50))
    price = Column(Integer())

    def __repr__(self):
        return f'Restauraunt(id={self.id})' + \
               f'name={self.name}' + \
               f'price={self.price}' 
    
#Customer Table
class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    def __repr__(self):
        return f'Customer(id={self.id})' + \
               f'firstName={self.first_name}' + \
               f"last_name={self.last_name}"
    
    


