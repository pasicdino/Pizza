from PyInquirer import prompt, Separator
import requests
import json

BASE_URL = "http://127.0.0.1:5000"


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


start_menu = {
    "type": "list",
    "name": "start",
    "message": "Welcome to Back to the Pizza in Hill Valley. What would you like to do?",
    "choices": ["See the menu", "See your previous orders", "Place your order", "Quit"],
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
            #TODO: DrinkOrder logic

    for i in range(1, 3):
        if menu_item_selected.startswith(get_dessert_with_price(str(i))):
            print("-----> " + get_dessert(str(i)) + " is added to your order!")
            #TODO: DessertOrder logic


def check_for_sizes(size_selected, i):
    if size_selected.startswith("Small"):
        print("-----> " + get_pizza(str(i)) + " of size Small is added to your order!")
        #TODO: PizzaOrder logic
    if size_selected.startswith("Medium"):
        print("-----> " + get_pizza(str(i)) + " of size Medium is added to your order!")
        # TODO: PizzaOrder logic
    if size_selected.startswith("Large"):
        print("-----> " + get_pizza(str(i)) + " of size Large is added to your order!")
        # TODO: PizzaOrder logic
    if size_selected.startswith("Go back"):
        return

def check_for_order_type(order_selected):
    # Check in database for id.
    if order_selected == "order":
        viewOrder()



def viewOrder():
    print("orderdetails")

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


