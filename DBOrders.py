import mysql.connector
import null as null

import Transform
class DBOrders:
    db = null
    mycursor = null

    def __init__(self):
        self.db = mysql.connector.connect(host='localhost', user='root', password='appelsap1!', port='3306', database='pizzas')
        self.mycursor = self.db.cursor()

    def customerDetails(self):
        firstName = input("Enter first name: ")
        lastName = input("Enter last name: ")
        email = input("Enter your email")
        phoneNumber = input("Enter phone number: ")
        streetName = input("Enter street name: ")
        streetNumber = input("Enter street number: ")
        city = input("Enter city name: ")

        self.mycursor.execute('SELECT COUNT(*) FROM customers WHERE email LIKE ' + str(email) + ';')
        customerExists = self.mycursor.fetchall()





