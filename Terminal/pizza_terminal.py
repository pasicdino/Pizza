from PyInquirer import prompt
import requests

BASE_URL = "http://localhost:3306"

start_menu = {
    "type": "list",
    "name": "choice",
    "message": "Welcome to Back to the Pizza in Hill Valley. What would you like to do?",
    "choices": ["See the menu", "See your order", "Place your order", "Quit"],
}

if __name__ == "__main__":
    while True:
        answers = prompt(start_menu)