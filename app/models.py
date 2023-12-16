from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column,Integer, String,ForeignKey
from sqlalchemy.ext.associationproxy import association_proxy


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

    reviews = relationship("Review", back_populates = 'restaurant')
    customers = association_proxy('reviews', 'customer', 
                creator = lambda cs:Review(customer = cs )                  )

    def __repr__(self):
        return f'Restauraunt(id={self.id})' + \
               f'name={self.name}' + \
               f'price={self.price}' 
    #all reviews for restaurant
    def reviews_for_restaurant(self):
        comments = [comment.comments for comment in self.reviews]
        return comments
    #customer who reviewed restaurant
    def customer_who_reviewed(self):
        return [review.customer.first_name for review in self.reviews]
    @classmethod
    def fanciest(cls, session):
        fanciest = session.query(cls).order_by(cls.price.desc()).first()
        return fanciest
    
    def all_reviews(self,session):
        reviews = session.query(Review).filter(Review.restaurant_id == self.id).all()
        reviews_list = [f'Review for {self.name} by {review.customer.full_name()}: {review.star_rating} stars.' for review in reviews]
        return reviews_list

    
    
    
#Customer Table
class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    reviews = relationship("Review", back_populates = 'customer')
    restaurants = association_proxy('reviews', 'restaurant',
                creator = lambda rs:Review(restaurant = rs))

    def __repr__(self):
        return f'Customer(id={self.id})' + \
               f'firstName={self.first_name}' + \
               f"last_name={self.last_name}"
    
    #reviews by particular customer
    def reviews_by_customer(self):
        return [review.comments for review in self.reviews]
    
    #restaurant particular customer has reviewed
    def restaurant_by_customer(self):
        restaurants =  [restaurant.name for restaurant in self.restaurants]
        return restaurants
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def favorite_restaurant(self, session):
        favorite = session.query(Restaurant).join(Review, Restaurant.id == Review.restaurant_id).filter(Review.customer_id == self.id).order_by(Review.star_rating.desc().first())
        return favorite
        
    def add_review(self,session,restaurant,rating,comments=""):
        review = Review(
                customer = self,
                restaurant = restaurant,
                star_rating = rating,
                comments = comments
        )
        session.add(review)
        session.commit()


    def delete_review(self,session,restaurant):
        delete_review = session.query(Review).filter(Review.customer_id == self.id, Review.restaurant_id == restaurant.id).all()
        for review in delete_review:
            session.delete(review)
        session.commit()

    
#REVIEWS TABLE
class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    comments = Column(String())
    star_rating = Column(Integer())

    customer_id = Column(Integer(), ForeignKey('customers.id'))
    restaurant_id = Column(Integer(), ForeignKey("restaurants.id"))

    customer = relationship("Customer", back_populates = 'reviews')
    restaurant = relationship ('Restaurant', back_populates="reviews")
    
    def __repr__(self):
        return f'Review(id={self.id}' + \
               f'comments={self.comments}' + \
               f'star_rating={self.star_rating})'
    

    def customer_reviewed_this(self):
        return self.customer.full_name()
    
    def restaurant_of_review(self):
        return self.restaurant.name
    
    def full_review(self):
        return f'Review for{self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars.'
    


    



