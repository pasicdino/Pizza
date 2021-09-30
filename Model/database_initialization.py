import sqlalchemy as db
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import *

engine = db.create_engine("mysql://root:TimeforPizza@localhost", echo=True)
#engine.execute("CREATE DATABASE Pizza")
engine.execute("USE Pizza")

Base = declarative_base()

class Pizzas(Base):
    __tablename__ = 'pizzas'

    pizza_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    pizza_name = Column(String(50), nullable=False, unique=True)
    vegetarian = Column(Boolean, nullable=True)



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
    discount_code = Column(String(50), nullable=False, unique=True)
    customer_id = Column(Integer(), ForeignKey('customers.customer_id'), nullable=False)

class Customer(Base):
    __tablename__ = 'customers'
    customer_id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    phone_number = Column(String(50), nullable=False)
    street_name = Column(String(255), nullable=False)
    street_number = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)

class Delivery_person(Base):
    __tablename__ = 'delivery_persons'
    delivery_person_id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    phone_number = Column(String(50), nullable=False)
    street_name = Column(String(255), nullable=False)
    street_number = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)

class Pizza_orders(Base):
    __tablename__ = 'pizza_orders'

    order_id = Column(Integer(), ForeignKey('orders.order_id'), primary_key=True, nullable=False)
    pizza_id = Column(Integer(), ForeignKey('pizzas.pizza_id'), primary_key=True, nullable=False)
    size = Column(Integer(), nullable=False)
    amount = Column(Integer(), nullable=False)

class Dessert_order(Base):
    __tablename__ = 'dessert_orders'
    order_id = Column(Integer(), ForeignKey('orders.order_id'), primary_key=True, nullable=False)
    dessert_id = Column(Integer(), ForeignKey('desserts.dessert_id'), primary_key=True, nullable=False)
    amount = Column(Integer(), nullable=False)

class Drink_order(Base):
    __tablename__ = 'drink_orders'
    order_id = Column(Integer(), ForeignKey('orders.order_id'), primary_key=True, nullable=False)
    drink_id = Column(Integer(), ForeignKey('drinks.drink_id'), primary_key=True, nullable=False)
    amount = Column(Integer(), nullable=False)

if __name__ == "__main__":
    print(Base.metadata.create_all(engine))
    Session = sessionmaker(bind=engine)
    sessionPizza = Session()
    sessionPizza.add(Pizzas(pizza_name='Margherita', vegetarian=True))
    sessionPizza.add(Pizzas(pizza_name='Tonno', vegetarian=True))
    sessionPizza.add(Pizzas(pizza_name='Hawaii', vegetarian=False))
    sessionPizza.add(Pizzas(pizza_name='Pepperoni', vegetarian=False))
    sessionPizza.add(Pizzas(pizza_name='Pollo', vegetarian=False))
    sessionPizza.add(Pizzas(pizza_name='Funghi', vegetarian=True))
    sessionPizza.add(Pizzas(pizza_name='Mozzarella', vegetarian=True))
    sessionPizza.add(Pizzas(pizza_name='Taco', vegetarian=False))
    sessionPizza.add(Pizzas(pizza_name='Vegetariana', vegetarian=True))
    sessionPizza.add(Pizzas(pizza_name='Scampi', vegetarian=True))
    sessionPizza.commit()

    sessionToppings = Session()
    sessionToppings.add(Toppings(topping='cheese', topping_price=1.50))
    sessionToppings.add(Toppings(topping='tomato sauce', topping_price=1.00))
    sessionToppings.add(Toppings(topping='tuna', topping_price=2.50))
    sessionToppings.add(Toppings(topping='pineapple', topping_price=1.00))
    sessionToppings.add(Toppings(topping='ham', topping_price=2.50))
    sessionToppings.add(Toppings(topping='salami', topping_price=2.50))
    sessionToppings.add(Toppings(topping='chicken', topping_price=2.50))
    sessionToppings.add(Toppings(topping='corn', topping_price=0.50))
    sessionToppings.add(Toppings(topping='bell pepper', topping_price=0.50))
    sessionToppings.add(Toppings(topping='spinach', topping_price=0.50))
    sessionToppings.add(Toppings(topping='mozzarella', topping_price=1.50))
    sessionToppings.add(Toppings(topping='cherry tomatoes', topping_price=0.50))
    sessionToppings.add(Toppings(topping='garlic sauce', topping_price=0.50))
    sessionToppings.add(Toppings(topping='minced meat', topping_price=2.50))
    sessionToppings.add(Toppings(topping='olives', topping_price=0.50))
    sessionToppings.add(Toppings(topping='zucchini', topping_price=0.50))
    sessionToppings.add(Toppings(topping='shrimp', topping_price=2.50))
    sessionToppings.add(Toppings(topping='mushroom', topping_price=0.50))
    sessionToppings.commit()

    sessionPizzaToppings = Session()
    sessionPizzaToppings.add(PizzaToppings(topping_id=1, pizza_id=1))
    sessionPizzaToppings.add(PizzaToppings(topping_id=1, pizza_id=2))
    sessionPizzaToppings.add(PizzaToppings(topping_id=1, pizza_id=3))
    sessionPizzaToppings.add(PizzaToppings(topping_id=1, pizza_id=4))
    sessionPizzaToppings.add(PizzaToppings(topping_id=1, pizza_id=5))
    sessionPizzaToppings.add(PizzaToppings(topping_id=1, pizza_id=6))
    sessionPizzaToppings.add(PizzaToppings(topping_id=1, pizza_id=7))
    sessionPizzaToppings.add(PizzaToppings(topping_id=1, pizza_id=8))
    sessionPizzaToppings.add(PizzaToppings(topping_id=1, pizza_id=9))
    sessionPizzaToppings.add(PizzaToppings(topping_id=1, pizza_id=10))
    sessionPizzaToppings.add(PizzaToppings(topping_id=2, pizza_id=1))
    sessionPizzaToppings.add(PizzaToppings(topping_id=2, pizza_id=2))
    sessionPizzaToppings.add(PizzaToppings(topping_id=2, pizza_id=3))
    sessionPizzaToppings.add(PizzaToppings(topping_id=2, pizza_id=4))
    sessionPizzaToppings.add(PizzaToppings(topping_id=2, pizza_id=5))
    sessionPizzaToppings.add(PizzaToppings(topping_id=2, pizza_id=6))
    sessionPizzaToppings.add(PizzaToppings(topping_id=2, pizza_id=7))
    sessionPizzaToppings.add(PizzaToppings(topping_id=2, pizza_id=8))
    sessionPizzaToppings.add(PizzaToppings(topping_id=2, pizza_id=9))
    sessionPizzaToppings.add(PizzaToppings(topping_id=2, pizza_id=10))
    sessionPizzaToppings.add(PizzaToppings(topping_id=3, pizza_id=2))
    sessionPizzaToppings.add(PizzaToppings(topping_id=4, pizza_id=3))
    sessionPizzaToppings.add(PizzaToppings(topping_id=5, pizza_id=3))
    sessionPizzaToppings.add(PizzaToppings(topping_id=6, pizza_id=4))
    sessionPizzaToppings.add(PizzaToppings(topping_id=7, pizza_id=5))
    sessionPizzaToppings.add(PizzaToppings(topping_id=8, pizza_id=5))
    sessionPizzaToppings.add(PizzaToppings(topping_id=8, pizza_id=9))
    sessionPizzaToppings.add(PizzaToppings(topping_id=9, pizza_id=5))
    sessionPizzaToppings.add(PizzaToppings(topping_id=10, pizza_id=5))
    sessionPizzaToppings.add(PizzaToppings(topping_id=10, pizza_id=9))
    sessionPizzaToppings.add(PizzaToppings(topping_id=11, pizza_id=7))
    sessionPizzaToppings.add(PizzaToppings(topping_id=12, pizza_id=7))
    sessionPizzaToppings.add(PizzaToppings(topping_id=13, pizza_id=8))
    sessionPizzaToppings.add(PizzaToppings(topping_id=14, pizza_id=8))
    sessionPizzaToppings.add(PizzaToppings(topping_id=15, pizza_id=9))
    sessionPizzaToppings.add(PizzaToppings(topping_id=16, pizza_id=9))
    sessionPizzaToppings.add(PizzaToppings(topping_id=17, pizza_id=10))
    sessionPizzaToppings.add(PizzaToppings(topping_id=18, pizza_id=6))
    sessionPizzaToppings.commit()

    sessionSizes = Session()
    sessionSizes.add(Sizes(size='Small', price='3.00'))
    sessionSizes.add(Sizes(size='Medium', price='4.50'))
    sessionSizes.add(Sizes(size='Large', price='6.00'))
    sessionSizes.commit()

    sessionDrinks = Session()
    sessionDrinks.add(Drinks(drink_name='Fanta', drink_price=2.50))
    sessionDrinks.add(Drinks(drink_name='Coca Cola', drink_price=2.50))
    sessionDrinks.add(Drinks(drink_name='Sprite', drink_price=2.50))
    sessionDrinks.add(Drinks(drink_name='Water', drink_price=1.50))
    sessionDrinks.commit()

    sessionDesserts = Session()
    sessionDesserts.add(Desserts(dessert_name='Tiramisu', dessert_price=4.00))
    sessionDesserts.add(Desserts(dessert_name='Ice Cream', dessert_price=3.00))
    sessionDesserts.commit()

    sessionDeliveryPersons = Session()
    sessionDeliveryPersons.add(
        Delivery_person(first_name='Dino', last_name='Pasic', email='01dino@live.nl', phone_number='0683329208',
                        street_name='Kant', street_number='20', city='Kerkrade'))
    sessionDeliveryPersons.add(
        Delivery_person(first_name='Laurence', last_name='Nickel', email='laurencenickel00@gmail.com',
                        phone_number='0630409715', street_name='Putstraat', street_number='30', city='Kerkrade'))
    sessionDeliveryPersons.add(
        Delivery_person(first_name='Chris', last_name='Smalling', email='chris.smalling@outlook.com',
                        phone_number='0637295017', street_name='Welterlaan', street_number='16', city='Heerlen'))
    sessionDeliveryPersons.add(
        Delivery_person(first_name='Phil', last_name='Jones', email='jonesphil@gmail.com', phone_number='0675942167',
                        street_name='Akerstraat', street_number='83', city='Heerlen'))
    sessionDeliveryPersons.add(
        Delivery_person(first_name='Bukayo', last_name='Saka', email='bukayosaka7@gmail.com', phone_number='0613248794',
                        street_name='Ringoven', street_number='60', city='Landgraaf'))
    sessionDeliveryPersons.add(Delivery_person(first_name='Sead', last_name='Kolasinac', email='seadkolasinac@live.nl',
                                               phone_number='0645971348', street_name='Eijkhagenlaan',
                                               street_number='31', city='Landgraaf'))
    sessionDeliveryPersons.commit()




