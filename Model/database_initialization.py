from app import app
from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:TimeforPizza@localhost/pizza"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Pizzas(db.Model):
    __tablename__ = 'pizzas'

    pizza_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    pizza_name = db.Column(db.String(50), nullable=False, unique=True)
    vegetarian = db.Column(db.Boolean, nullable=True)


class Toppings(db.Model):
    __tablename__ = 'toppings'
    topping_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    topping = db.Column(db.String(50), nullable=False)
    topping_price = db.Column(db.Float(), nullable=False)


class PizzaToppings(db.Model):
    __tablename__ = 'pizza_toppings'
    topping_id = db.Column(db.Integer(), db.ForeignKey('toppings.topping_id'), nullable=False, primary_key=True)
    pizza_id = db.Column(db.Integer(), db.ForeignKey('pizzas.pizza_id'), nullable=False, primary_key=True)


class Drinks(db.Model):
    __tablename__ = 'drinks'
    drink_id = db.Column(db.Integer(), primary_key=True, autoincrement=True, nullable=False)
    drink_name = db.Column(db.String(50), nullable=False)
    drink_price = db.Column(db.Float(), nullable=False)


class Desserts(db.Model):
    __tablename__ = 'desserts'
    dessert_id = db.Column(db.Integer(), primary_key=True, autoincrement=True, nullable=False)
    dessert_name = db.Column(db.String(50), nullable=False)
    dessert_price = db.Column(db.Float(), nullable=False)


class Sizes(db.Model):
    __tablename__ = 'sizes'
    size_id = db.Column(db.Integer(), primary_key=True, autoincrement=True, nullable=False)
    size = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float(), nullable=False)


class Orders(db.Model):
    __tablename__ = 'orders'

    order_id = db.Column(db.Integer(), primary_key=True, autoincrement=True, nullable=False)
    customer_id = db.Column(db.Integer(), db.ForeignKey('customers.customer_id'), nullable=False, )
    order_time = db.Column(db.DateTime(), nullable=False)
    order_price = db.Column(db.Float(), nullable=False)
    delivery_person_id = db.Column(db.Integer(), db.ForeignKey('delivery_persons.delivery_person_id'), nullable=False)


class DiscountCodes(db.Model):
    __tablename__ = 'discount_codes'

    discount_id = db.Column(db.Integer(), primary_key=True, autoincrement=True, nullable=False)
    discount_code = db.Column(db.String(50), nullable=False, unique=True)
    customer_id = db.Column(db.Integer(), db.ForeignKey('customers.customer_id'), nullable=False)


class Customers(db.Model):
    __tablename__ = 'customers'
    customer_id = db.Column(db.Integer(), primary_key=True, autoincrement=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    phone_number = db.Column(db.String(50), nullable=False)
    street_name = db.Column(db.String(255), nullable=False)
    street_number = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)


class DeliveryPersons(db.Model):
    __tablename__ = 'delivery_persons'
    delivery_person_id = db.Column(db.Integer(), primary_key=True, autoincrement=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    phone_number = db.Column(db.String(50), nullable=False)
    street_name = db.Column(db.String(255), nullable=False)
    street_number = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)


class PizzaOrders(db.Model):
    __tablename__ = 'pizza_orders'

    order_id = db.Column(db.Integer(), db.ForeignKey('orders.order_id'), primary_key=True, nullable=False)
    pizza_id = db.Column(db.Integer(), db.ForeignKey('pizzas.pizza_id'), primary_key=True, nullable=False)
    size = db.Column(db.Integer(), nullable=False)
    amount = db.Column(db.Integer(), nullable=False)


class DessertOrders(db.Model):
    __tablename__ = 'dessert_orders'
    order_id = db.Column(db.Integer(), db.ForeignKey('orders.order_id'), primary_key=True, nullable=False)
    dessert_id = db.Column(db.Integer(), db.ForeignKey('desserts.dessert_id'), primary_key=True, nullable=False)
    amount = db.Column(db.Integer(), nullable=False)


class DrinkOrders(db.Model):
    __tablename__ = 'drink_orders'
    order_id = db.Column(db.Integer(), db.ForeignKey('orders.order_id'), primary_key=True, nullable=False)
    drink_id = db.Column(db.Integer(), db.ForeignKey('drinks.drink_id'), primary_key=True, nullable=False)
    amount = db.Column(db.Integer(), nullable=False)

def initialize_database():
    db.create_all()
    db.session.add(Pizzas(pizza_name='Margherita', vegetarian=True))
    db.session.add(Pizzas(pizza_name='Tonno', vegetarian=True))
    db.session.add(Pizzas(pizza_name='Hawaii', vegetarian=False))
    db.session.add(Pizzas(pizza_name='Pepperoni', vegetarian=False))
    db.session.add(Pizzas(pizza_name='Pollo', vegetarian=False))
    db.session.add(Pizzas(pizza_name='Funghi', vegetarian=True))
    db.session.add(Pizzas(pizza_name='Mozzarella', vegetarian=True))
    db.session.add(Pizzas(pizza_name='Taco', vegetarian=False))
    db.session.add(Pizzas(pizza_name='Vegetariana', vegetarian=True))
    db.session.add(Pizzas(pizza_name='Scampi', vegetarian=True))
    db.session.commit()

    db.session.add(Toppings(topping='cheese', topping_price=1.50))
    db.session.add(Toppings(topping='tomato sauce', topping_price=1.00))
    db.session.add(Toppings(topping='tuna', topping_price=2.50))
    db.session.add(Toppings(topping='pineapple', topping_price=1.00))
    db.session.add(Toppings(topping='ham', topping_price=2.50))
    db.session.add(Toppings(topping='salami', topping_price=2.50))
    db.session.add(Toppings(topping='chicken', topping_price=2.50))
    db.session.add(Toppings(topping='corn', topping_price=0.50))
    db.session.add(Toppings(topping='bell pepper', topping_price=0.50))
    db.session.add(Toppings(topping='spinach', topping_price=0.50))
    db.session.add(Toppings(topping='mozzarella', topping_price=1.50))
    db.session.add(Toppings(topping='cherry tomatoes', topping_price=0.50))
    db.session.add(Toppings(topping='garlic sauce', topping_price=0.50))
    db.session.add(Toppings(topping='minced meat', topping_price=2.50))
    db.session.add(Toppings(topping='olives', topping_price=0.50))
    db.session.add(Toppings(topping='zucchini', topping_price=0.50))
    db.session.add(Toppings(topping='shrimp', topping_price=2.50))
    db.session.add(Toppings(topping='mushroom', topping_price=0.50))
    db.session.commit()

    db.session.add(PizzaToppings(topping_id=1, pizza_id=1))
    db.session.add(PizzaToppings(topping_id=1, pizza_id=2))
    db.session.add(PizzaToppings(topping_id=1, pizza_id=3))
    db.session.add(PizzaToppings(topping_id=1, pizza_id=4))
    db.session.add(PizzaToppings(topping_id=1, pizza_id=5))
    db.session.add(PizzaToppings(topping_id=1, pizza_id=6))
    db.session.add(PizzaToppings(topping_id=1, pizza_id=7))
    db.session.add(PizzaToppings(topping_id=1, pizza_id=8))
    db.session.add(PizzaToppings(topping_id=1, pizza_id=9))
    db.session.add(PizzaToppings(topping_id=1, pizza_id=10))
    db.session.add(PizzaToppings(topping_id=2, pizza_id=1))
    db.session.add(PizzaToppings(topping_id=2, pizza_id=2))
    db.session.add(PizzaToppings(topping_id=2, pizza_id=3))
    db.session.add(PizzaToppings(topping_id=2, pizza_id=4))
    db.session.add(PizzaToppings(topping_id=2, pizza_id=5))
    db.session.add(PizzaToppings(topping_id=2, pizza_id=6))
    db.session.add(PizzaToppings(topping_id=2, pizza_id=7))
    db.session.add(PizzaToppings(topping_id=2, pizza_id=8))
    db.session.add(PizzaToppings(topping_id=2, pizza_id=9))
    db.session.add(PizzaToppings(topping_id=2, pizza_id=10))
    db.session.add(PizzaToppings(topping_id=3, pizza_id=2))
    db.session.add(PizzaToppings(topping_id=4, pizza_id=3))
    db.session.add(PizzaToppings(topping_id=5, pizza_id=3))
    db.session.add(PizzaToppings(topping_id=6, pizza_id=4))
    db.session.add(PizzaToppings(topping_id=7, pizza_id=5))
    db.session.add(PizzaToppings(topping_id=8, pizza_id=5))
    db.session.add(PizzaToppings(topping_id=8, pizza_id=9))
    db.session.add(PizzaToppings(topping_id=9, pizza_id=5))
    db.session.add(PizzaToppings(topping_id=10, pizza_id=5))
    db.session.add(PizzaToppings(topping_id=10, pizza_id=9))
    db.session.add(PizzaToppings(topping_id=11, pizza_id=7))
    db.session.add(PizzaToppings(topping_id=12, pizza_id=7))
    db.session.add(PizzaToppings(topping_id=13, pizza_id=8))
    db.session.add(PizzaToppings(topping_id=14, pizza_id=8))
    db.session.add(PizzaToppings(topping_id=15, pizza_id=9))
    db.session.add(PizzaToppings(topping_id=16, pizza_id=9))
    db.session.add(PizzaToppings(topping_id=17, pizza_id=10))
    db.session.add(PizzaToppings(topping_id=18, pizza_id=6))
    db.session.commit()

    db.session.add(Sizes(size='Small', price='3.00'))
    db.session.add(Sizes(size='Medium', price='4.50'))
    db.session.add(Sizes(size='Large', price='6.00'))
    db.session.commit()

    db.session.add(Drinks(drink_name='Fanta', drink_price=2.50))
    db.session.add(Drinks(drink_name='Coca Cola', drink_price=2.50))
    db.session.add(Drinks(drink_name='Sprite', drink_price=2.50))
    db.session.add(Drinks(drink_name='Water', drink_price=1.50))
    db.session.commit()

    db.session.add(Desserts(dessert_name='Tiramisu', dessert_price=4.00))
    db.session.add(Desserts(dessert_name='Ice Cream', dessert_price=3.00))
    db.session.commit()

    db.session.add(DeliveryPersons(first_name='Dino', last_name='Pasic', email='01dino@live.nl', phone_number='0683329208', street_name='Kant', street_number='20', city='Kerkrade'))
    db.session.add(DeliveryPersons(first_name='Laurence', last_name='Nickel', email='laurencenickel00@gmail.com', phone_number='0630409715', street_name='Putstraat', street_number='30', city='Kerkrade'))
    db.session.add(DeliveryPersons(first_name='Chris', last_name='Smalling', email='chris.smalling@outlook.com', phone_number='0637295017', street_name='Welterlaan', street_number='16', city='Heerlen'))
    db.session.add(DeliveryPersons(first_name='Phil', last_name='Jones', email='jonesphil@gmail.com', phone_number='0675942167', street_name='Akerstraat', street_number='83', city='Heerlen'))
    db.session.add(DeliveryPersons(first_name='Bukayo', last_name='Saka', email='bukayosaka7@gmail.com', phone_number='0613248794', street_name='Ringoven', street_number='60', city='Landgraaf'))
    db.session.add(DeliveryPersons(first_name='Sead', last_name='Kolasinac', email='seadkolasinac@live.nl', phone_number='0645971348', street_name='Eijkhagenlaan', street_number='31', city='Landgraaf'))
    db.session.commit()

# if __name__ == "__main__":
#     initialize_database()

