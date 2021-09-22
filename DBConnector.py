import mysql.connector
import null as null

import Transform


class DBConnector:
    db = null
    mycursor = null

    def __init__(self):
        self.db = mysql.connector.connect(host='localhost', user='root', password='appelsap1!', port='3306', database='pizzas')
        self.mycursor = self.db.cursor()

    def getPizzaNames(self):
        self.mycursor.execute('SELECT pizza_name FROM pizzas;')
        return Transform.listOfTuplesToList(self.mycursor.fetchall())

    def getPizza(self, pizzaID):
        self.mycursor.execute('SELECT pizza_name FROM pizzas WHERE pizza_id LIKE +' + str(pizzaID) + ';')

        return self.mycursor.fetchall()[0][0]

    def getToppings(self, pizzaID):
        self.mycursor.execute('SELECT topping FROM toppings WHERE topping_id IN (SELECT topping_id FROM pizza_toppings WHERE pizza_id LIKE ' + str(pizzaID) + ');')
        return Transform.listOfTuplesToList(self.mycursor.fetchall())

    def getDrinks(self):
        self.mycursor.execute('SELECT drink_name FROM drinks;')
        return Transform.listOfTuplesToList(self.mycursor.fetchall())

    def getDrink(self, drinkID):
        self.mycursor.execute('SELECT drink_name FROM drinks WHERE drink_id LIKE +' + str(drinkID) + ';')
        return self.mycursor.fetchall()[0][0]

    def getDrinkPrice(self, drinkID):
        self.mycursor.execute('SELECT drink_price FROM drinks WHERE drink_id LIKE ' + str(drinkID) + ';')
        return self.mycursor.fetchall()[0][0]

    def getDesserts(self):
        self.mycursor.execute('SELECT dessert_name FROM desserts')
        return Transform.listOfTuplesToList(self.mycursor.fetchall())

    def getDessertPrice(self, dessertID):
        self.mycursor.execute('SELECT dessert_price FROM desserts WHERE dessert_id LIKE ' + str(dessertID) + ';')
        return self.mycursor.fetchall()[0][0]

    def getDessert(self, dessertID):
        self.mycursor.execute('SELECT dessert_name FROM desserts WHERE dessert_id LIKE +' + str(dessertID) + ';')
        return self.mycursor.fetchall()[0][0]

    def getSmallPizzaPrice(self, pizzaID):
        self.mycursor.execute('SELECT topping_price FROM toppings WHERE topping_id IN (SELECT topping_id FROM pizza_toppings WHERE pizza_id LIKE ' + str(pizzaID) + ');')
        toppings = Transform.listOfTuplesToList(self.mycursor.fetchall())
        x = 0
        for i in range(0, len(toppings)):
            x += toppings[i]
        return x + 3


