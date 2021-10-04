from PyInquirer import prompt, Separator
import requests
import json

BASE_URL = "http://127.0.0.1:5000"

pizza_orders = []
drink_orders = []
dessert_orders = []


def get_pizza(pizza_id):
    response = requests.get(BASE_URL + "/pizza/" + pizza_id)
    result = json.loads(response.text)
    return result["pizza_name"]


def get_drink(drink_id):
    response = requests.get(BASE_URL + "/drink/" + drink_id)
    result = json.loads(response.text)
    return result["drink_name"]


def get_dessert(dessert_id):
    response = requests.get(BASE_URL + "/dessert/" + dessert_id)
    result = json.loads(response.text)
    return result["dessert_name"]


# TODO: Solve query in pizza_sql_model.py containing inner joins. Here we also want to retrieve the toppings and vegetarian.
def get_pizza_with_price(pizza_id):
    response = requests.get(BASE_URL + "/pizza/" + pizza_id)
    result = json.loads(response.text)
    string = result["pizza_name"]
    string = string + " - " + result["id"] + " euros"
    return string


def get_drink_with_price(drink_id):
    response = requests.get(BASE_URL + "/drink/" + drink_id)
    result = json.loads(response.text)
    string = result["drink_name"]
    string = string + " - " + str(result["drink_price"]) + " euros"
    return string


def get_dessert_with_price(dessert_id):
    response = requests.get(BASE_URL + "/dessert/" + dessert_id)
    result = json.loads(response.text)
    string = result["dessert_name"]
    string = string + " - " + str(result["dessert_price"]) + " euros"
    return string


def get_size_price(size_name):
    response = requests.get(BASE_URL + "/pizzasize/" + size_name)
    result = json.loads(response.text)
    string = result["price"]
    return string


SMALL_PIZZA_PRICE = float(get_size_price("Small"))
MEDIUM_PIZZA_PRICE = float(get_size_price("Medium"))
LARGE_PIZZA_PRICE = float(get_size_price("Large"))
MEDIUM_MINUS_SMALL = (MEDIUM_PIZZA_PRICE-SMALL_PIZZA_PRICE)
LARGE_MINUS_SMALL = (LARGE_PIZZA_PRICE-SMALL_PIZZA_PRICE)


def get_number_of_pizzas():
    response = requests.get(BASE_URL + "/pizza/count")
    result = json.loads(response.text)
    string = result["count()"]
    return string

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
        pizzas.append(get_pizza_with_price(str(i)))
    return pizzas

pizzas = get_list_of_pizzas()


def get_pizza_ordered():
    pizza_orders.append("Go back")
    pizza_orders.append(Separator(""))
    return pizza_orders


def get_drink_ordered():
    drink_orders.append("Go back")
    drink_orders.append(Separator(""))
    return drink_orders


def get_dessert_ordered():
    dessert_orders.append("Go back")
    dessert_orders.append(Separator(""))
    return dessert_orders


start_menu = {
    "type": "list",
    "name": "start",
    "message": "Welcome to Back to the Pizza in Hill Valley. What would you like to do?",
    "choices": ["See the menu", "See your current order", "See your previous orders", "Place your order", "Quit"],
}


# TODO: Display toppings and whether it is vegetarian.
menu = {
    "type": "list",
    "name": "menu",
    "message": "Select which items you want to order (prices are small pizza).",
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
    "message": "Here are the pizzas present in your order. Select one to delete it, otherwise select 'go back'",
    "choices": get_pizza_ordered()
}

drinks_ordered = {
    "type": "list",
    "name": "drinks_ordered",
    "message": "Here are the drinks present in your order. Select one to delete it, otherwise select 'go back'",
    "choices": get_drink_ordered()
}

desserts_ordered = {
    "type": "list",
    "name": "desserts_ordered",
    "message": "Here are the desserts present in your order. Select one to delete it, otherwise select 'go back'",
    "choices": get_dessert_ordered()
}

delete_item = {
    "type": "list",
    "name": "deletion",
    "message": "Do you want to delete this item?",
    "choices": ["Yes", "No"]
}

validateEmailForOrders = {
    "type": "input",
    "name": "email",
    "message": "Please input your email address."
}

viewUserOrders = {
    "type": "list",
    "name": "orders",
    "message": "Your order history.",
    "choices": [Separator("-- Current orders --"), "order", Separator("-- Previous orders --"), "Delivered order",
                Separator(""), "Go back"]
}

viewOrder = {
    "type": "list",
    "name": "order",
    "message": "The information of the selected order.",
    "choices": [Separator("ORDER INFO"), Separator(""), "Go back"]
}


def check_for_menu(menu_item_selected):
    # TODO: Fix get_number_of_pizzas(). Only returns 1
    # for i in range(1, get_number_of_pizzas() + 1):
    #     if menu_item_selected.startswith(get_pizza_with_price(str(i))):
    #         pizza_size = prompt(sizes)
    #         size_selected = pizza_size["selectSize"]
    #         check_for_sizes(size_selected, i)

    for i in range(1, 10 + 1):
        if menu_item_selected.startswith(get_pizza_with_price(str(i))):
            pizza_size = prompt(sizes)
            size_selected = pizza_size["selectSize"]
            check_for_sizes(size_selected, i)

    for i in range(1, 5):
        if menu_item_selected.startswith(get_drink_with_price(str(i))):
            print("-----> " + get_drink(str(i)) + " is added to your order!")
            drink_orders.append(get_drink(str(i)))

    for i in range(1, 3):
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
            #check_for_selected_pizza(pizza_selected)

    if kind_selected == "Drinks":
        while True:
            order_drink = prompt(drinks_ordered)
            drink_selected = order_drink["drinks_ordered"]
            if drink_selected == "Go back":
                break
            #check_for_selected_drink(drink_selected)

    if kind_selected == "Desserts":
        while True:
            order_dessert = prompt(desserts_ordered)
            dessert_selected = order_dessert["desserts_ordered"]
            if dessert_selected == "Go back":
                break
            #check_for_selected_dessert(pizza_selected)


# def check_for_selected_pizza(pizza_selected):
#     if pizza_selected.startswith(get_pizza_with_price(str(i))):
#         pizza = prompt(delete_item)
#         to_be_deleted = pizza["deletion"]
#         delete_item(to_be_deleted, )
#
#
# def delete_item(menu):
#     if

def deletePizzaFromOrder(pizza_selected):
    if pizza_selected != "Pizzas"

if __name__ == "__main__":
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

        if answer == "See your previous orders":
            while True:
                emails = prompt(validateEmailForOrders)
                orders = prompt(viewUserOrders)
                order_selected = orders["orders"]
                if order_selected == "Go back":
                    break
                check_for_order_type(order_selected)
                #break



        # if answer == "Place your order":
            # Customer must fill in email-address.
            # Customer must also fill in address, mainly for determining delivery person and attach that id to the order.

        if answer == "Quit":
            break


