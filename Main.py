import mysql.connector



db = mysql.connector.connect(host='localhost', user='root', password='appelsap1!', port='3306', database='test')

mycursor = db.cursor()

mycursor.execute('SELECT * FROM pizza')

pizzas = mycursor.fetchall()

for pizza in pizzas:
    print(pizza)
