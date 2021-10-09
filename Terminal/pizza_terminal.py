import sys
from datetime import datetime, timedelta

from PyInquirer import prompt, Separator
import requests
import json

# from ..controller import set_every_item_to_string

BASE_URL = "http://127.0.0.1:5000"

pizza_orders = []
drink_orders = []
dessert_orders = []

PROFIT_MARGIN = 1.4
VAT = 1.09


def get_size_price(size_name):
    response = requests.get(BASE_URL + "/pizzasize/" + size_name)
    result = json.loads(response.text)
    string = round(float(result["price"]) * PROFIT_MARGIN * VAT, 2)
    return string


SMALL_PIZZA_PRICE = float(get_size_price("Small"))
MEDIUM_PIZZA_PRICE = float(get_size_price("Medium"))
LARGE_PIZZA_PRICE = float(get_size_price("Large"))
MEDIUM_MINUS_SMALL = (MEDIUM_PIZZA_PRICE-SMALL_PIZZA_PRICE)
LARGE_MINUS_SMALL = (LARGE_PIZZA_PRICE-SMALL_PIZZA_PRICE)

def get_pizza(pizza_id):
    response = requests.get(BASE_URL + "/pizza/" + pizza_id)
    result = json.loads(response.text)
    return result["pizza_name"]


def get_pizza_id(pizza_name):
    response = requests.get(BASE_URL + "/pizza/" + pizza_name)
    result = json.loads(response.text)
    return result["pizza_id"]


def get_pizza_toppings(pizza_id):
    response = requests.get(BASE_URL + "/pizzatoppings/" + pizza_id)
    result = json.loads(response.text)
    initial_string = "Toppings: "
    string = initial_string
    iterable_dict = result.items()
    for key, value in iterable_dict:
        string = string + str(value) + ", "
    string = string[:-2]
    return string


def get_pizza_vegetarian(pizza_id):
    response = requests.get(BASE_URL + "/pizzavegetarian/" + pizza_id)
    result = json.loads(response.text)
    result = result["0"]
    string = "Vegetarian: "
    if result == "True":
        string = string + "Yes"
    else:
        string = string + "No"
    return string


def get_drink(drink_id):
    response = requests.get(BASE_URL + "/drink/" + drink_id)
    result = json.loads(response.text)
    return result["drink_name"]


def get_dessert(dessert_id):
    response = requests.get(BASE_URL + "/dessert/" + dessert_id)
    result = json.loads(response.text)
    return result["dessert_name"]


def get_pizza_with_price_and_toppings(pizza_id):
    response = requests.get(BASE_URL + "/pizzaprice/" + pizza_id)
    result = json.loads(response.text)
    result_price = float(result["0"])
    result_price_with_margin_and_vat = round(result_price * PROFIT_MARGIN * VAT, 2) + SMALL_PIZZA_PRICE
    price = str(result_price_with_margin_and_vat)
    pizza_names = get_pizza(pizza_id)
    toppings = get_pizza_toppings(pizza_id)
    vegetarian = get_pizza_vegetarian(pizza_id)
    string = pizza_names + "   ---   " + price + " euros" + "   ---   " + toppings + "   ---   " + vegetarian
    return string


def get_drink_with_price(drink_id):
    response = requests.get(BASE_URL + "/drink/" + drink_id)
    result = json.loads(response.text)
    string = result["drink_name"]
    result_price_with_margin_and_vat = round(float(result["drink_price"]) * PROFIT_MARGIN * VAT, 2)
    string = string + " --- " + str(result_price_with_margin_and_vat) + " euros"
    return string


def get_dessert_with_price(dessert_id):
    response = requests.get(BASE_URL + "/dessert/" + dessert_id)
    result = json.loads(response.text)
    string = result["dessert_name"]
    result_price_with_margin_and_vat = round(float(result["dessert_price"]) * PROFIT_MARGIN * VAT, 2)
    string = string + " --- " + str(result_price_with_margin_and_vat) + " euros"
    return string


def get_pizzas_price(pizza_id, size):
    response = requests.get(BASE_URL + "/pizzaprice/" + pizza_id)
    result = json.loads(response.text)
    price = round(float(result["0"]) * PROFIT_MARGIN * VAT, 2)
    if size == "Medium":
        price = price + MEDIUM_PIZZA_PRICE
    elif size == "Large":
        price = price + LARGE_PIZZA_PRICE
    else:
        price = price + SMALL_PIZZA_PRICE
    return price


def get_drink_price(drink_id):
    response = requests.get(BASE_URL + "/drink/" + drink_id)
    result = json.loads(response.text)
    price = round(float(result["drink_price"]) * PROFIT_MARGIN * VAT, 2)
    return price


def get_dessert_price(dessert_id):
    response = requests.get(BASE_URL + "/dessert/" + dessert_id)
    result = json.loads(response.text)
    price = round(float(result["dessert_price"]) * PROFIT_MARGIN * VAT, 2)
    return price


def get_number_of_pizzas():
    response = requests.get(BASE_URL + "/pizza/count")
    result = json.loads(response.text)
    result = int(result["count"])
    return result


def get_number_of_desserts():
    response = requests.get(BASE_URL + "/dessert/count")
    result = json.loads(response.text)
    result = int(result["count"])
    return result


def get_number_of_drinks():
    response = requests.get(BASE_URL + "/drink/count")
    result = json.loads(response.text)
    result = int(result["count"])
    return result


def get_list_of_drinks():
    drinks = []
    for i in range(1, 5):
        drinks.append(get_drink_with_price(str(i)))
    return drinks

drinks = get_list_of_drinks()


def get_list_of_desserts():
    desserts = []
    for i in range(1, 3):
        desserts.append(get_dessert_with_price(str(i)))
    return desserts

desserts = get_list_of_desserts()


def get_list_of_pizzas():
    pizzas = []
    for i in range(1, 11):
        pizzas.append(get_pizza_with_price_and_toppings(str(i)))
    return pizzas

pizzas = get_list_of_pizzas()


def get_pizza_ordered():
    pizza_orders.append("Go back")
    return pizza_orders


def get_drink_ordered():
    drink_orders.append("Go back")
    return drink_orders


def get_dessert_ordered():
    dessert_orders.append("Go back")
    return dessert_orders


def verify_login(email, password):
    response = requests.post(BASE_URL + "/login", data={"email": email, "password": password})
    result = json.loads(response.text)
    if result["response"] == "success":
        print("-----> LOGIN WAS SUCCESSFUL")
        return email
    else:
        print("-----> LOGIN WAS NOT SUCCESSFUL")
        return sys.exit()


def verify_sign_up(email, password, first_name, last_name, phone_number, street_name, street_number, city):
    response = requests.post(BASE_URL + "/signup", data={"email": email, "password": password, "first_name": first_name, "last_name": last_name, "phone number": phone_number, "street_name": street_name, "street_number": street_number, "city": city})
    result = json.loads(response.text)
    if result["response"] == "success":
        print("-----> SIGN UP WAS SUCCESSFUL")
        return email
    else:
        print("-----> SIGN UP WAS NOT SUCCESSFUL")
        return sys.exit()


def verify_discount_code(discount_code):
    response = requests.post(BASE_URL + "/discount", data={"discount_code": discount_code})
    result = json.loads(response.text)
    if result["response"] == "success":
        return "True"
    else:
        return "False"


def get_city_by_email(email):
    response = requests.get(BASE_URL + "/city/" + email)
    result = json.loads(response.text)
    string = result["city"]
    return string


def get_delivery_person_by_city(city):
    response = requests.get(BASE_URL + "/deliveryperson/" + city)
    result = json.loads(response.text)
    result_delivery_person = result["delivery_person_id"]
    return result_delivery_person


def get_pizza_price(pizza_name):
    response = requests.get(BASE_URL + "/pizzapricebyname/" + pizza_name)
    result = json.loads(response.text)
    result_price = round(float(result["0"]) * PROFIT_MARGIN * VAT, 2)
    price = result_price + SMALL_PIZZA_PRICE
    return price


home = {
    "type": "list",
    "name": "home",
    "message": "Welcome to Back to the Pizza in Hill Valley. Do you already have an account or do you want to sign up? Once you are signed up, you are logged in",
    "choices": ["Log in", "Sign up", "Quit"]
}

login_questions = [
    {"type": "input", "name": "email", "message": "Please enter your email"},
    {"type": "password", "name": "password", "message": "Please enter your password"}
]

sign_up_questions = login_questions + [
    {"type": "input", "name": "first_name", "message": "Please enter your first name"},
    {"type": "input", "name": "last_name", "message": "Please enter your last name"},
    {"type": "input", "name": "phone_number", "message": "Please enter your phone number"},
    {"type": "input", "name": "street_name", "message": "Please enter your street name"},
    {"type": "input", "name": "street_number", "message": "Please enter your street number"},
    {"type": "input", "name": "city", "message": "Please choose either Kerkrade, Heerlen or Landgraaf as your city"}
]

start_menu = {
    "type": "list",
    "name": "start",
    "message": "Welcome to the FANCY Back to the Pizza in Hill Valley. What would you like to do?",
    "choices": ["See the menu", "See your current order", "See your delivery time for latest order", "Place your order", "Quit"],
}


# TODO: Display toppings and whether it is vegetarian.
menu = {
    "type": "list",
    "name": "menu",
    "message": "Select which items you want to order, the prices for the pizzas are the prices for a small pizza including a VAT of 9%.",
    "choices": [Separator("-- Pizzas --"), pizzas[0], pizzas[1], pizzas[2], pizzas[3], pizzas[4], pizzas[5], pizzas[6], pizzas[7], pizzas[8], pizzas[9], Separator(" "), Separator("-- Drinks --"), drinks[0], drinks[1], drinks[2], drinks[3], Separator(" "), Separator("-- Desserts --"), desserts[0], desserts[1], Separator(""), "Go back"]
}

sizes = {
    "type": "list",
    "name": "selectSize",
    "message": "Select the size of your pizza.",
    "choices": ["Small", "Medium" + " + " + str(MEDIUM_MINUS_SMALL) + " euros", "Large" + " + " + str(LARGE_MINUS_SMALL) + " euros", Separator(""), "Go back"]
}

which_kind_of_order = {
    "type": "list",
    "name": "kind_of",
    "message": "Which part of your order would you like to see?",
    "choices": ["Pizzas", "Drinks", "Desserts", Separator(""), "Go back"]
}

pizzas_ordered = {
    "type": "list",
    "name": "pizzas_ordered",
    "message": "Here are the pizzas present in your order.",
    "choices": get_pizza_ordered()
}

drinks_ordered = {
    "type": "list",
    "name": "drinks_ordered",
    "message": "Here are the drinks present in your order.",
    "choices": get_drink_ordered()
}

desserts_ordered = {
    "type": "list",
    "name": "desserts_ordered",
    "message": "Here are the desserts present in your order.",
    "choices": get_dessert_ordered()
}

place_order = {
    "type": "list",
    "name": "place_order",
    "message": "Are you sure you want to place your order?",
    "choices": ["Yes", "No"]
}

got_discount = {
    "type": "list",
    "name": "got_discount",
    "message": "Do you have a discount code?",
    "choices": ["Yes", "No"]
}

input_discount = [
    {"type": "input", "name": "discount_code", "message": "Please enter your discount code"}
]

order_choices = {
    "type": "list",
    "name": "order_choices",
    "message": "What would you like to do?",
    "choices": ["See order status", "See estimated delivery time", "Cancel order", Separator(""), "Exit"]
}


def check_for_menu(menu_item_selected):
    for i in range(1, get_number_of_pizzas() + 1):
        if menu_item_selected.startswith(get_pizza_with_price_and_toppings(str(i))):
            pizza_size = prompt(sizes)
            size_selected = pizza_size["selectSize"]
            check_for_sizes(size_selected, i)

    for i in range(1, get_number_of_drinks() + 1):
        if menu_item_selected.startswith(get_drink_with_price(str(i))):
            print("-----> " + get_drink(str(i)) + " is added to your order!")
            drink_orders.append(get_drink(str(i)))

    for i in range(1, get_number_of_desserts() + 1):
        if menu_item_selected.startswith(get_dessert_with_price(str(i))):
            print("-----> " + get_dessert(str(i)) + " is added to your order!")
            dessert_orders.append(get_dessert(str(i)))


def check_for_sizes(size_selected, i):
    if size_selected.startswith("Small"):
        print("-----> " + get_pizza(str(i)) + " of size Small is added to your order!")
        pizza_orders.append(get_pizza(str(i)) + " - Small")
    if size_selected.startswith("Medium"):
        print("-----> " + get_pizza(str(i)) + " of size Medium is added to your order!")
        pizza_orders.append(get_pizza(str(i)) + " - Medium")
    if size_selected.startswith("Large"):
        print("-----> " + get_pizza(str(i)) + " of size Large is added to your order!")
        pizza_orders.append(get_pizza(str(i)) + " - Large")
    if size_selected.startswith("Go back"):
        return


def check_kind_of_order(kind_selected):
    if kind_selected == "Pizzas":
        while True:
            order_pizza = prompt(pizzas_ordered)
            pizza_selected = order_pizza["pizzas_ordered"]
            if pizza_selected == "Go back":
                break

    if kind_selected == "Drinks":
        while True:
            order_drink = prompt(drinks_ordered)
            drink_selected = order_drink["drinks_ordered"]
            if drink_selected == "Go back":
                break

    if kind_selected == "Desserts":
        while True:
            order_dessert = prompt(desserts_ordered)
            dessert_selected = order_dessert["desserts_ordered"]
            if dessert_selected == "Go back":
                break


def get_info_for_order_customer(email_customer):
    response = requests.get(BASE_URL + "/customer/" + email_customer)
    result = json.loads(response.text)
    customer_id = result["customer_id"]
    return customer_id


def get_info_for_order_city(email_customer):
    city = get_city_by_email(email_customer)
    delivery_person_id = get_delivery_person_by_city(city)
    return delivery_person_id


def create_order(customer_id_order, order_time, delivery_person_id_order):
    response = requests.post(BASE_URL + "/order/create", data={"customer_id": customer_id_order, "order_time": order_time, "order_price": 0, "delivery_person_id": delivery_person_id_order})
    order_id = get_latest_order()
    return order_id


def set_order_time_for_delivery_person(time_of_order, order_id):
    response = requests.post(BASE_URL + "/deliveryperson/update", data={"order_time": time_of_order, "order_id": order_id})


def get_latest_order():
    response = requests.get(BASE_URL + "/order/latest")
    result = json.loads(response.text)
    order_id_latest = result["order_id"]
    return order_id_latest


def set_price_for_order(price):
    response = requests.post(BASE_URL + "/order/updateprice", data={"order_price": price, "order_id": order_id})


def get_delivery_person_by_order_id(order_id):
    response = requests.get(BASE_URL + "/deliverypersonname/" + order_id)
    result = json.loads(response.text)
    first_name = result["first_name"]
    last_name = result["last_name"]
    full_name = first_name + " " + last_name
    return full_name


def create_dict_of_counts(list_of_orders):
    dict_of_counts = {item:list_of_orders.count(item) for item in list_of_orders}
    return dict_of_counts


def get_info_for_pizza_orders():
    pizza_orders.remove("Go back")
    pizza_counts = create_dict_of_counts(pizza_orders)
    return pizza_counts


def get_info_for_drink_orders():
    drink_orders.remove("Go back")
    drink_counts = create_dict_of_counts(drink_orders)
    return drink_counts


def get_info_for_dessert_orders():
    dessert_orders.remove("Go back")
    dessert_counts = create_dict_of_counts(dessert_orders)
    return dessert_counts


def create_pizza_order(order_id, pizza_id, size, amount):
    response = requests.post(BASE_URL + "/pizzaorder/create", data={"order_id": order_id, "pizza_id": pizza_id, "size": size, "amount": amount})


def create_drink_order(order_id, drink_id, amount):
    response = requests.post(BASE_URL + "/drinkorder/create", data={"order_id": order_id, "drink_id": drink_id, "amount": amount})


def create_dessert_order(order_id, dessert_id, amount):
    response = requests.post(BASE_URL + "/dessertorder/create", data={"order_id": order_id, "dessert_id": dessert_id, "amount": amount})


def check_pizza_size(pizza_string: str):
    if "Medium" in pizza_string:
        return "Medium"
    elif "Large" in pizza_string:
        return "Large"
    else:
        return "Small"


def distinct_pizza_values():
    return list(set(pizza_orders))


def distinct_drink_values():
    return list(set(drink_orders))


def distinct_dessert_values():
    return list(set(dessert_orders))


def create_order_for_pizzas(pizza_counts, order_id):
    price_of_pizzas = 0
    for i in range(0, len(distinct_pizza_values())):
        for j in range(1, len(pizzas) + 1):
            if get_pizza(str(j)) in pizza_orders[i]:
                pizza_id = j
                size = check_pizza_size(distinct_pizza_values()[i])
                amount = pizza_counts.get(distinct_pizza_values()[i])
                pizza_price_single = get_pizzas_price(str(j), size) * amount
                price_of_pizzas = price_of_pizzas + pizza_price_single
                create_pizza_order(order_id, pizza_id, size, amount)
    return price_of_pizzas


def create_order_for_drinks(drink_counts, order_id):
    price_of_drinks = 0
    for i in range(0, len(distinct_drink_values())):
        for j in range(1, len(drinks) + 1):
            if get_drink(str(j)) in drink_orders[i]:
                drink_id = j
                amount = drink_counts.get(distinct_drink_values()[i])
                drink_price_single = get_drink_price(str(j)) * amount
                price_of_drinks = price_of_drinks + drink_price_single
                create_drink_order(order_id, drink_id, amount)
    return price_of_drinks


def create_order_for_desserts(dessert_counts, order_id):
    price_of_desserts = 0
    for i in range(0, len(distinct_dessert_values())):
        for j in range(1, len(desserts) + 1):
            if get_dessert(str(j)) in dessert_orders[i]:
                dessert_id = j
                amount = dessert_counts.get(distinct_dessert_values()[i])
                dessert_price_single = get_dessert_price(str(j)) * amount
                price_of_desserts = price_of_desserts + dessert_price_single
                create_dessert_order(order_id, dessert_id, amount)
    return price_of_desserts


def calculate_total_price(pizza_price, drink_price, dessert_price):
    total_price = pizza_price + drink_price + dessert_price
    return total_price


def get_order_time(order_id):
    response = requests.get(BASE_URL + "/ordertime/" + order_id)
    result = json.loads(response.text)
    time = result["order_time"]
    return time


def get_order_time_check_for_cancel(order_id):
    response = requests.get(BASE_URL + "/ordertime/" + order_id)
    result = json.loads(response.text)
    status = result["response"]
    if status == "success":
        return "False"
    if status == "failure":
        return "True"


def check_number_of_pizzas_for_customer(customer_id):
    response = requests.get(BASE_URL + "/customerpizzas/" + customer_id)
    result = json.loads(response.text)
    final_result = int(result["number"])
    return final_result


def update_number_of_pizzas(new_number, customer_id):
    response = requests.post(BASE_URL + "/customerpizzas/update", data={"number": new_number, "customer_id": customer_id})


def create_discount_code(customer_id):
    response = requests.post(BASE_URL + "/discount/create", data={"customer_id": customer_id})
    result = json.loads(response.text)
    code = result["discount_code"]
    return code


def remove_order():
    response = requests.post(BASE_URL + "/order/delete", data={"order_id": order_id})


def check_order_selected(order_information_selected, order_id):
    if order_information_selected == "See order status":
        if get_order_time_check_for_cancel(order_id) == "True":
            print("-----> Your order is cancelled")
        else:
            order_time_plus_5 = datetime.strptime(get_order_time(order_id), '%a, %d %b %Y %H:%M:%S %Z') + timedelta(minutes=5)
            time_now = datetime.now()
            if time_now < order_time_plus_5:
                print("-----> Your order is in process")
            else:
                print("-----> Your order is out for delivery")

    if order_information_selected == "See estimated delivery time":
        if get_order_time_check_for_cancel(order_id) == "True":
            print("-----> Your order is cancelled")
        else:
            order_time_plus_15 = datetime.strptime(get_order_time(order_id), '%a, %d %b %Y %H:%M:%S %Z') + timedelta(minutes=15)
            print(f"Your estimated delivery time: {order_time_plus_15}")

    if order_information_selected == "Cancel order":
        order_time_plus_5 = datetime.strptime(get_order_time(order_id), '%a, %d %b %Y %H:%M:%S %Z') + timedelta(minutes=5)
        time_now = datetime.now()
        if time_now < order_time_plus_5:
            remove_order()
        else:
            print("-----> Sorry this order cannot be canceled since it is already out for delivery")


if __name__ == "__main__":
    # login_information = prompt(home)
    # information_selected = login_information["home"]
    # if information_selected == "Log in":
    #     login_answers = prompt(login_questions)
    #     email_customer = verify_login(**login_answers)
    # if information_selected == "Sign up":
    #     sign_up_answers = prompt(sign_up_questions)
    #     email_customer = verify_sign_up(**sign_up_answers)
    # if information_selected == "Quit":
    #     sys.exit()

    email_customer = "laurencenickel00@gmail.com"

    while True:
        answers = prompt(start_menu)
        answer = answers["start"]
        if answer == "See the menu":
            while True:
                menu_items = prompt(menu)
                menu_item_selected = menu_items["menu"]
                if menu_item_selected == "Go back":
                    break
                check_for_menu(menu_item_selected)

        if answer == "See your current order":
            while True:
                kind_of_order = prompt(which_kind_of_order)
                kind_selected = kind_of_order["kind_of"]
                if kind_selected == "Go back":
                    break
                check_kind_of_order(kind_selected)

        if answer == "Place your order":
            while True:
                order_placed = prompt(place_order)
                order_placed_selected = order_placed["place_order"]
                if order_placed_selected == "Yes":
                    if len(pizza_orders) > 1:
                        discount_check = prompt(got_discount)
                        discount_selected = discount_check["got_discount"]
                        discount = 0
                        if discount_selected == "Yes":
                            discount_code_check = prompt(input_discount)
                            if verify_discount_code(**discount_code_check) == "True":
                                discount = 0.10
                                print("-----> DISCOUNT CODE HAS BEEN ADDED")
                        customer_id = get_info_for_order_customer(email_customer)
                        delivery_person_id = get_info_for_order_city(email_customer)
                        time_of_order = datetime.now()
                        order_id = create_order(customer_id, time_of_order, delivery_person_id)
                        set_order_time_for_delivery_person(time_of_order, order_id)
                        pizza_counts = get_info_for_pizza_orders()
                        pizza_price = create_order_for_pizzas(pizza_counts, order_id)
                        drink_counts = get_info_for_drink_orders()
                        drink_price = create_order_for_drinks(drink_counts, order_id)
                        dessert_counts = get_info_for_dessert_orders()
                        dessert_price = create_order_for_desserts(dessert_counts, order_id)
                        print("-----> YOUR ORDER HAS BEEN PLACED")
                        total_price = calculate_total_price(pizza_price, drink_price, dessert_price)
                        total_price_minus_discount = total_price - (total_price * discount)
                        set_price_for_order(total_price_minus_discount)
                        print(f"-----> YOUR TOTAL IS: {total_price_minus_discount} euros")
                        delivery_person = get_delivery_person_by_order_id(order_id)
                        time_of_delivery = time_of_order + timedelta(minutes=15)
                        print(f"-----> YOUR ORDER WILL BE DELIVERED AT {time_of_delivery} BY {delivery_person}")
                        update_number_of_pizzas(check_number_of_pizzas_for_customer(str(customer_id)) + len(pizza_orders), customer_id)
                        if check_number_of_pizzas_for_customer(str(customer_id)) > 9:
                            code = create_discount_code(customer_id)
                            print(f"-----> THANK YOU FOR BEING A CUSTOMER. FOR 10% OFF ON YOUR NEXT ORDER, USE THIS DISCOUNT CODE: {code}")


                        #TODO: Check number of pizzas ordered and create and send discount code.
                        while True:
                            order_information = prompt(order_choices)
                            order_information_selected = order_information["order_choices"]
                            if order_information_selected == "Exit":
                                sys.exit()
                            check_order_selected(order_information_selected, order_id)
                    else:
                        print("-----> You must order AT LEAST one pizza to complete your order")
                        break
                else:
                    break
        if answer == "Quit":
            break


