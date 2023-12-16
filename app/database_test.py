#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review, Base

if __name__ == "__main__":
    engine = create_engine('sqlite:///restaurants.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    #OBJECT RELATIONSHIP METHODS
    print("OBJECT RELATIONSHIP METHODS")
                    #REVIEW
    print("REVIEWS TEST")
    review_test = session.query(Review).first()
    print(f"1.First Review was made by:{review_test.customer_reviewed_this()}")
    print(f'2.The review is for the restaurant: {review_test.restaurant_of_review()}')

                    #Restaurant
    print("RESTAURANT TESTS")
    restaurant_test = session.query(Restaurant).first()
    print(f'1.The review comments for the first restaurant are {restaurant_test.reviews_for_restaurant()}')
    print(f'2.customers who reviewed the  first restaurant are {restaurant_test.customer_who_reviewed()}')
    
                    #CUSTOMERS
    print("CUSTOMER TESTS")
    customer_test = session.query(Customer).first()
    print(f'The reviews the first customer has made are:{customer_test.reviews_by_customer()}')
    print(f'The restaurants reviewed by the first customer are: {customer_test.restaurant_by_customer()}')