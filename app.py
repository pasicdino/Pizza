from flask import Flask, request, make_response

app = Flask(__name__)

from Model.pizza_sql_model import find_single_pizza, find_number_of_pizzas, find_size_price, find_single_drink, \
    find_single_dessert, find_single_customer, create_new_customer, find_city_by_email
from controller import password_complexity, check_password, hash_password

INVALID_MESSAGE = "email or password is not valid"

@app.route("/pizza/<pizza_id>")
def get_pizza(pizza_id: int):
    pizza = find_single_pizza(pizza_id=pizza_id)
    if pizza:
        return make_response({"pizza_name": pizza.pizza_name, "id": pizza_id}, 200)
    else:
        return make_response({"error": f"Pizza with pizza_id {pizza_id} does not exist"})

@app.route("/pizza/<pizza_id>")
def get_pizzaVegetarian(pizza_id: int):
    pizza = get_pizza(pizza_id)
    if pizza:
        return make_response({"vegetarian": pizza.vegetarian}, 200)
    else:
        return make_response({"error": f"Vegetarian label on pizza with pizza_id {pizza_id} does not exist"})


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
    count = len(find_number_of_pizzas())
    if count:
        return make_response({"count()": count.count()}, 200)
    else:
        return make_response({"error": f"There exists no pizza"})


@app.route("/pizzasize/<size_name>")
def get_size_price(size_name: str):
    price = find_size_price(size=size_name)
    if price:
        return make_response({"price": price.price}, 200)
    else:
        return make_response({"error": f"Size with size_name {size_name} does not exist"})


@app.route("/city")
def find_city(email):
    city = find_city_by_email(email=email)
    if city:
        return make_response({"city": city.city}, 200)
    else:
        return make_response({"error": f"City with city_name {city} does not exist"})


@app.route("/login", methods=["POST"])
def check_customer():
    email = request.form["email"]
    password = request.form["password"]

    the_customer = find_single_customer(email=email)
    if the_customer is None:
        return INVALID_MESSAGE

    if check_password(the_customer, password):
        return make_response({"result": "Login successful"}, 200)
    else:
        return make_response({"error": INVALID_MESSAGE}, 400)


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
        create_new_customer(first_name, last_name, email, hash_password(password), phone_number, street_name, street_number, city)
    except Exception as ex:
        print(f"Could not create customer with email: {email}")
        return make_response({"error": f"Could not create customer with email: {email}"}, 400)

    return make_response({"result": "success"}, 200)