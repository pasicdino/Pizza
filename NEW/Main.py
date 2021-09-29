import sqlalchemy as db
#import pandas as pd
from sqlalchemy.orm import declarative_base
from sqlalchemy import *

engine = db.create_engine("mysql://root:TimeforPizza@localhost", echo=True)
engine.execute("USE Pizza")

Base = declarative_base()

class Pizzas(Base):
    __tablename__ = 'pizzas'

    pizza_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    pizza_name = Column(String(50), nullable=False, unique=True)
    vegetarian = Column(Boolean, nullable=True)

    def __repr__(self):
        return "<User(pizza_id='%s', pizza_name='%s', vegetarian='Vegetarian: %s')>" % (self.pizza_id, self.pizza_name, self.vegetarian)

class Toppings(Base):
    __tablename__ = 'toppings'
    topping_id = Column(Integer(), primary_key = True, autoincrement = True)
    topping = Column(String(50), nullable = False)
    topping_price = Column(Float(), nullable = False)

class PizzaToppings(Base):
    __tablename__ = 'pizza_toppings'
    topping_id = Column(Integer(), ForeignKey('toppings.topping_id'), nullable = False, primary_key=True)
    pizza_id = Column(Integer(), ForeignKey('pizzas.pizza_id'), nullable = False, primary_key=True)

class Drinks(Base):
    __tablename__ = 'drinks'
    drink_id = Column(Integer(), primary_key = True, autoincrement = True, nullable = False)
    drink_name = Column(String(50), nullable = False)
    drink_price = Column(Float(), nullable = False)

class Desserts(Base):
    __tablename__ = 'desserts'
    dessert_id = Column(Integer(), primary_key= True, autoincrement=True, nullable=False)
    dessert_name = Column(String(50), nullable=False)
    dessert_price = Column(Float(), nullable=False)

class Sizes(Base):
    __tablename__ = 'sizes'
    size_id = Column(Integer(), primary_key= True, autoincrement=True, nullable=False)
    size = Column(String(50), nullable = False)
    price = Column(Float(), nullable = False)

class Orders(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    customer_id = Column(Integer(), ForeignKey('customers.customer_id'), nullable=False,)
    order_time = Column(DateTime(), nullable=False)
    order_price = Column(Float(), nullable=False)
    delivery_person_id = Column(Integer(), ForeignKey('delivery_persons.delivery_person_id'), nullable=False)

class Discount_codes(Base):
    __tablename__ = 'discount_codes'

    discount_id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    discount_code = (String(50), nullable=False, unique=True)
    customer_id = (Integer(), ForeignKey('customers.customer_id'), nullable=False)

class Pizza_orders(Base):
    __tablename__ = 'pizza_orders'

    order_id = Column(Integer(), ForeignKey('orders.order_id'), nullable=False)
    pizza_id = Column(Integer(), ForeignKey('pizzas.pizza_id'), nullable=False)
    size = Column(Integer(), nullable=False)
    amount = Column(Integer(), nullable=False)



def main():
    print(repr(Pizza.__table__))
    print(Base.metadata.create_all(engine))

if __name__ == "__main__":
    main()


