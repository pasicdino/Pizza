import json

from flask import Flask, request, make_response

app = Flask(__name__)

from Model.pizza_sql_model import find_single_pizza, find_number_of_pizzas, find_size_price, find_single_drink, \
    find_single_dessert, find_single_customer, create_new_customer, find_city, find_price_of_pizza, \
    find_toppings_of_pizza, find_pizza_vegetarian, find_number_of_drinks, find_number_of_desserts, \
    find_price_of_pizza_by_name, find_delivery_person, create_new_order, update_order_price, find_latest_order, \
    create_new_pizza_order, create_new_drink_order, create_new_dessert_order
from controller import password_complexity, check_password, hash_password

INVALID_MESSAGE = "email or password is not valid"

@app.route("/pizzaprice/<pizza_id>")
def get_price(pizza_id: int):
    pizza_price = find_price_of_pizza(pizza_id=pizza_id)
    if pizza_price:
        return make_response({"0": pizza_price}, 200)
    else:
        return make_response({"error": f"Pizza with pizza_id {pizza_id} does not exist"})


@app.route("/pizzapricebyname/<pizza_name>")
def get_pizza_price(pizza_name: str):
    pizza_price = find_price_of_pizza_by_name(pizza_name=pizza_name)
    if pizza_price:
        return make_response({"0": pizza_price}, 200)
    else:
        return make_response({"error": f"Pizza with pizza_name {pizza_name} does not exist"})


@app.route("/pizzatoppings/<pizza_id>")
def get_toppings(pizza_id: int):
    pizza_toppings = find_toppings_of_pizza(pizza_id=pizza_id)
    if pizza_toppings:
        return make_response(pizza_toppings, 200)
    else:
        return make_response({"error": f"Pizza with pizza_id {pizza_id} does not exist"})


@app.route("/pizzavegetarian/<pizza_id>")
def get_pizza_vegetarian(pizza_id: int):
    pizza_vegetarian = find_pizza_vegetarian(pizza_id=pizza_id)
    if pizza_vegetarian:
        return make_response({"0": pizza_vegetarian}, 200)
    else:
        return make_response({"error": f"Vegetarian label on pizza with pizza_id {pizza_id} does not exist"})


@app.route("/pizza/<pizza_id>")
def get_pizza(pizza_id: int):
    pizza = find_single_pizza(pizza_id=pizza_id)
    if pizza:
        return make_response({"pizza_name": pizza.pizza_name}, 200)
    else:
        return make_response({"error": f"Pizza with pizza_id {pizza_id} does not exist"})


@app.route("/pizza/<pizza_name>")
def get_pizza_id(pizza_name: str):
    pizza = find_single_pizza(pizza_name=pizza_name)
    if pizza:
        return make_response({"pizza_id": pizza.pizza_id}, 200)
    else:
        return make_response({"error": f"Pizza with pizza_name {pizza_name} does not exist"})


@app.route("/drink/<drink_id>")
def get_drink(drink_id: int):
    drink = find_single_drink(drink_id=drink_id)
    if drink:
        return make_response({"drink_name": drink.drink_name, "drink_price": drink.drink_price}, 200)
    else:
        return make_response({"error": f"Drink with drink_id {drink_id} does not exist"})


@app.route("/dessert/<dessert_id>")
def get_dessert(dessert_id: int):
    dessert = find_single_dessert(dessert_id=dessert_id)
    if dessert:
        return make_response({"dessert_name": dessert.dessert_name, "dessert_price": dessert.dessert_price}, 200)
    else:
        return make_response({"error": f"Dessert with dessert_id {dessert_id} does not exist"})


@app.route("/pizza/count")
def get_number_of_pizzas():
    count = find_number_of_pizzas()
    if count:
        return make_response({"count": count}, 200)
    else:
        return make_response({"error": f"There exists no pizza"})


@app.route("/dessert/count")
def get_number_of_desserts():
    count = find_number_of_desserts()
    if count:
        return make_response({"count": count}, 200)
    else:
        return make_response({"error": f"There exists no dessert"})


@app.route("/drink/count")
def get_number_of_drinks():
    count = find_number_of_drinks()
    if count:
        return make_response({"count": count}, 200)
    else:
        return make_response({"error": f"There exists no drink"})


@app.route("/pizzasize/<size_name>")
def get_size_price(size_name: str):
    price = find_size_price(size=size_name)
    if price:
        return make_response({"price": price.price}, 200)
    else:
        return make_response({"error": f"Size with size_name {size_name} does not exist"})


@app.route("/customer/<email>")
def get_customer_by_email(email):
    customer = find_single_customer(email=email)
    if customer:
        return make_response({"customer_id": customer.customer_id}, 200)
    else:
        return make_response({"error": f"Customer with email {email} does not exist"})


@app.route("/deliveryperson/<city>")
def get_delivery_person_by_city(city):
    delivery_person = find_delivery_person(city=city)
    if delivery_person:
        return make_response({"delivery_person_id": delivery_person.delivery_person_id}, 200)
    else:
        return make_response({"error": f"Delivery person with delivery_person_id {delivery_person} does not exist"})

@app.route("/city/<email>")
def get_city(email):
    city = find_city(email=email)
    if city:
        return make_response({"city": city.city}, 200)
    else:
        return make_response({"error": f"City with city_name {city} does not exist"})


@app.route("/order/latest")
def get_latest_order():
    order_id = find_latest_order()
    if order_id:
        return make_response({"order_id": order_id}, 200)
    else:
        return make_response({"error": f"There is no order"})


@app.route("/login", methods=["POST"])
def check_customer():
    email = request.form.get('email')
    password = request.form.get('password')

    the_customer = find_single_customer(email=email)
    if the_customer is None:
        return INVALID_MESSAGE

    if check_password(the_customer, password):
        return make_response({"result": "Login successful", "response": "success"}, 200)
    else:
        return make_response({"error": INVALID_MESSAGE, "response": "failure"}, 400)


@app.route("/signup", methods=["POST"])
def create_customer():
    email = request.form.get('email')
    password = request.form.get('password')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    phone_number = request.form.get('phone_number')
    street_name = request.form.get('street_name')
    street_number = request.form.get('street_number')
    city = request.form.get('city')

    the_customer = find_single_customer(email=email)
    if the_customer is not None:
        print("Please select a different email. This one already exists")
        return make_response({"error": "Please select a different email. This one already exists"}, 400)

    if message := password_complexity(password):
        print(f"Password does not meet complexity: {message}")
        return make_response({"error": "Password does not meet complexity", "failed": message}, 400)
    try:
        create_new_customer(first_name=first_name, last_name=last_name, email=email, hashed_password=hash_password(password), phone_number=phone_number, street_name=street_name, street_number=street_number, city=city)
    except Exception as ex:
        print(f"Could not create customer with email: {email}")
        return make_response({"error": f"Could not create customer with email: {email}"}, 400)

    return make_response({"result": "success"}, 200)


@app.route("/order/create", methods=["POST"])
def create_order():
    customer_id = request.form.get('customer_id')
    order_time = request.form.get('order_time')
    order_price = request.form.get('order_price')
    delivery_person_id = request.form.get('delivery_person_id')

    try:
        create_new_order(customer_id=customer_id, order_time=order_time, order_price=order_price, delivery_person_id=delivery_person_id)
    except Exception as ex:
        print(f"Could not create an order")
        return make_response({"error": f"Could not create order"}, 400)

    return make_response({"result": "success"}, 200)


@app.route("/order/updateprice", methods=["POST"])
def update_price_order():
    order_price = request.form.get('order_price')
    order_id = request.form.get('order_id')

    try:
        update_order_price(order_id=order_id, order_price=order_price)
    except Exception as ex:
        print(f"Could not update the price of the order with order_id {order_id}")
        return make_response({"error": f"Could not update the price of the order with order_id {order_id}"}, 400)

    return make_response({"result": "success"}, 200)


@app.route("/pizzaorder/create", methods=["POST"])
def create_pizza_order():
    order_id = request.form.get('order_id')
    pizza_id = request.form.get('pizza_id')
    size = request.form.get('size')
    amount = request.form.get('amount')

    try:
        create_new_pizza_order(order_id=order_id, pizza_id=pizza_id, size=size, amount=amount)
    except Exception as ex:
        print(f"Could not create a pizza_order with order_id {order_id}")
        return make_response({"error": f"Could not create a pizza_order with order_id {order_id}"}, 400)

    return make_response({"result": "success"}, 200)


@app.route("/drinkorder/create", methods=["POST"])
def create_drink_order():
    order_id = request.form.get('order_id')
    drink_id = request.form.get('drink_id')
    amount = request.form.get('amount')

    try:
        create_new_drink_order(order_id=order_id, drink_id=drink_id, amount=amount)
    except Exception as ex:
        print(f"Could not create a drink_order with order_id {order_id}")
        return make_response({"error": f"Could not create a drink_order with order_id {order_id}"}, 400)

    return make_response({"result": "success"}, 200)


@app.route("/dessertorder/create", methods=["POST"])
def create_dessert_order():
    order_id = request.form.get('order_id')
    dessert_id = request.form.get('dessert_id')
    amount = request.form.get('amount')

    try:
        create_new_dessert_order(order_id=order_id, dessert_id=dessert_id, amount=amount)
    except Exception as ex:
        print(f"Could not create a dessert_order with order_id {order_id}")
        return make_response({"error": f"Could not create a dessert_order with order_id {order_id}"}, 400)

    return make_response({"result": "success"}, 200)