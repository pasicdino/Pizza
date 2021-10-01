import sqlalchemy as db

engine = db.create_engine

class Toppings(db.Model):
    __tablename__ = 'toppings'
    topping_id = db.Column(Integer(), primary_key = True, autoincrement = True)
    topping = db.Column(String(50), nullable = False)
    topping_price = db.Column(String(50), nullable = False)

class PizzaToppings(db.Model):
    __tablename__ = 'pizza_toppings'
    topping_id = db.Column(Integer(), db.ForeignKey('toppings.topping_id'), nullable = False)
    pizza_id = db.Column(Integer(), db.ForeignKey('pizzas.pizza_id'), nullable = False)

class Drinks(db.Model):
    __tablename__ = 'drinks'
    drink_id = db.Column(Integer(), primary_key = True, autoincrement = True, nullable = False)
    drink_name = db.Column(String(50), nullable = False)
    drink_price = db.Column(String(50), nullable = False)

class Desserts(db.Model):
    __tablename__ = 'drinks'
    dessert_id = db.Column(Integer(), primary_key= True, autoincrement=True, nullable=False)
    dessert_name = db.Column(String(50), nullable=False)
    dessert_price = db.Column(String(50), nullable=False)

class Sizes(db.Model):
    __tablename__ = 'sizes'
    size_id = db.Column(Integer(), primary_key= True, autoincrement=True, nullable=False)
    size = db.Column(String(50), nullable = False)
    price = db.Column(String(50), nullable = False)