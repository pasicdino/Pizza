from OLD.DBMenu import DBMenu
from OLD.DBOrders import DBOrders

db = DBMenu()
dbOrders = DBOrders()

amountOfPizzas = len(db.getPizzaNames())
for i in range(1, amountOfPizzas):
    print(db.getPizza(i) + " - " + str(db.getSmallPizzaPrice(i)))

amountOfDesserts = len(db.getDesserts())
for i in range(1, amountOfDesserts+1):
    print(db.getDessert(i) + " - " + str(db.getDessertPrice(i)))

amountOfDrinks = len(db.getDrinks())
for i in range(1, amountOfDrinks+1):
    print(db.getDrink(i) + " - " + str(db.getDrinkPrice(i)))


dbOrders.customerDetails()