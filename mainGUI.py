import PySimpleGUI as sg

from DBConnector import DBConnector
db = DBConnector()

amountOfPizzas = len(db.getPizzaNames())
for i in range(1, amountOfPizzas):
    print(db.getPizza(i))
    print(db.getSmallPizzaPrice(i))

amountOfDesserts = len(db.getDesserts())
for i in range(1, amountOfDesserts+1):
    print(db.getDessert(i))
    print(db.getDessertPrice(i))

amountOfDrinks = len(db.getDrinks())
for i in range(1, amountOfDrinks+1):
    print(db.getDrink(i))
    print(db.getDrinkPrice(i))


