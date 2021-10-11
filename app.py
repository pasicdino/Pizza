from flask import Flask, request, make_response

app = Flask(__name__)

from Model.pizza_sql_model import find_single_pizza, find_number_of_pizzas, find_size_price, find_single_drink, \
    find_single_dessert, find_single_customer, create_new_customer, find_city, find_price_of_pizza, \
    find_toppings_of_pizza, find_pizza_vegetarian, find_number_of_drinks, find_number_of_desserts, \
    find_price_of_pizza_by_name, find_delivery_person, create_new_order, update_order_price, find_latest_order, \
    create_new_pizza_order, create_new_drink_order, create_new_dessert_order, find_delivery_person_by_order_id, \
    find_order_time, delete_the_order, update_delivery_person_order_time, find_number_of_pizzas_of_customer, \
    create_new_discount_code, check_discount_code, update_number_of_customers, delete_discount_code
from controller import password_complexity, check_password, hash_password, check_time, create_random_string

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
    for i in range(0, len(delivery_person)):
        if delivery_person[i].latest_order is not None:
            result = check_time(delivery_person[i].latest_order)
            if result == "True":
                delivery_person_result = delivery_person[i]
                break
        else:
            delivery_person_result = delivery_person[i]
    if delivery_person_result:
        return make_response({"delivery_person_id": delivery_person_result.delivery_person_id, "response": "success"}, 200)
    else:
        return make_response({"error": f"Delivery person with delivery_person_id {delivery_person} does not exist", "response": "failure"}, 400)


@app.route("/deliverypersonname/<order_id>")
def get_delivery_person_by_order_id(order_id):
    delivery_person = find_delivery_person_by_order_id(order_id=order_id)
    if delivery_person:
        return make_response({"first_name": delivery_person.first_name, "last_name": delivery_person.last_name}, 200)
    else:
        return make_response({"error": f"Delivery person with delivery_person_id {delivery_person.delivery_person_id} does not exist"})


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



@app.route("/discount", methods=["POST"])
def check_discount():
    discount_code = request.form.get('discount_code')

    if check_discount_code(discount_code=discount_code):
        return make_response({"response": "success"}, 200)
    else:
        return make_response({"response": "failure"}, 400)


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
        create_new_customer(first_name=first_name, last_name=last_name, email=email, hashed_password=hash_password(password), phone_number=phone_number, street_name=street_name, street_number=street_number, city=city, number_of_pizzas=0)
    except Exception as ex:
        print(f"Could not create customer with email: {email}")
        return make_response({"error": f"Could not create customer with email: {email}", "response": "failure"}, 400)

    return make_response({"result": "success", "response": "success"}, 200)


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


@app.route("/discount/create", methods=["POST"])
def create_code_for_discount():
    customer_id = request.form.get('customer_id')
    discount_code = create_random_string()

    try:
        code = create_new_discount_code(customer_id=customer_id, discount_code=discount_code)
    except Exception as ex:
        print(f"Could not create a discount code")
        return make_response({"error": f"Could not create a discount code"}, 400)

    return make_response({"result": "success", "discount_code": code.discount_code}, 200)

@app.route("/ordertime/<order_id>")
def get_time_of_order(order_id):
    order = find_order_time(order_id=order_id)

    if order:
        return make_response({"order_time": order.order_time, "response": "success"}, 200)
    else:
        return make_response({"error": f"Order with order_id {order_id} does not exist", "response": "failure"}, 400)


@app.route("/order/delete", methods=["POST"])
def delete_order():
    order_id = request.form.get('order_id')

    try:
        delete_the_order(order_id=order_id)
    except Exception as ex:
        print(f"Could not delete the order with order_id {order_id}")
        return make_response({"error": f"Could not delete the order with order_id {order_id}"}, 400)

    print(f"Order with order_id {order_id} has been deleted")
    return make_response({"result": "success"}, 200)


@app.route("/deliveryperson/update", methods=["POST"])
def update_delivery_person():
    order_time = request.form.get('order_time')
    order_id = request.form.get('order_id')

    try:
        update_delivery_person_order_time(latest_order=order_time, order_id=order_id)
    except Exception as ex:
        return make_response({"error": f"Could not update the order at {order_time}"}, 400)

    return make_response({"result": "success"}, 200)


@app.route("/customerpizzas/<customer_id>")
def get_number_of_pizzas_for_customer(customer_id):
    number = find_number_of_pizzas_of_customer(customer_id=customer_id)

    if number:
        return make_response({"number": number.number_of_pizzas, "response": "success"}, 200)
    else:
        return make_response({"error": "No pizza has been ordered", "response": "failure"}, 400)


@app.route("/customerpizzas/update", methods=["POST"])
def update_number_of_pizzas():
    number = request.form.get('number')
    customer_id = request.form.get('customer_id')

    try:
        update_number_of_customers(number=number, customer_id=customer_id)
    except Exception as ex:
        return make_response({"error": f"Could not update the customer with {customer_id}"}, 400)

    return make_response({"result": "success"}, 200)


@app.route("/discount/delete", methods=["POST"])
def delete_discount():
    discount_code = request.form.get('discount_code')

    try:
        delete_discount_code(discount_code=discount_code)
    except Exception as ex:
        return make_response({"error": f"Could not delete discount_code {discount_code}"}, 400)

    return make_response({"result": "success"}, 200)
