import sqlalchemy as db

engine = db.create_engine

class Toppings(Base):
    __tablename__ = 'toppings'
    topping_id = Column(Integer(), primary_key = True, autoincrement = True)
    topping = Column(String(50), nullable = False)
    topping_price = Column(String(50), nullable = False)

class PizzaToppings(Base):
    __tablename__ = 'pizza_toppings'
    topping_id = Column(Integer(), ForeignKey('toppings.topping_id'), nullable = False)
    pizza_id = Column(Integer(), ForeignKey('pizzas.pizza_id'), nullable = False)

class Drinks(Base):
    __tablename__ = 'drinks'
    drink_id = Column(Integer(), primary_key = True, autoincrement = True, nullable = False)
    drink_name = Column(String(50), nullable = False)
    drink_price = Column(String(50), nullable = False)

class Desserts(Base):
    __tablename__ = 'drinks'
    dessert_id = Column(Integer(), primary_key= True, autoincrement=True, nullable=False)
    dessert_name = Column(String(50), nullable=False)
    dessert_price = Column(String(50), nullable=False)

class Sizes(Base):
    __tablename__ = 'sizes'
    size_id = Column(Integer(), primary_key= True, autoincrement=True, nullable=False)
    size = Column(String(50), nullable = False)
    price = Column(String(50), nullable = False)