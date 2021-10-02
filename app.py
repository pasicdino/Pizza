from flask import Flask, request, render_template, make_response

app = Flask(__name__)

from Model.pizza_sql_model import find_single_pizza, find_number_of_pizzas, find_size_price, find_single_drink, \
    find_single_dessert


@app.route("/pizza/<pizza_id>")
def get_pizza(pizza_id: int):
    pizza = find_single_pizza(pizza_id=pizza_id)
    if pizza:
        return make_response({"pizza_name": pizza.pizza_name, "id": pizza_id}, 200)
    else:
        return make_response({"error": f"Pizza with pizza_id {pizza_id} does not exist"})


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
        return make_response({"count()": count.count()})
    else:
        return make_response({"error": f"There exists no pizza"})


@app.route("/pizzasize/<size_name>")
def get_size_price(size_name: str):
    price = find_size_price(size=size_name)
    if price:
        return make_response({"price": price.price}, 200)
    else:
        return make_response({"error": f"Size with size_name {size_name} does not exist"})
