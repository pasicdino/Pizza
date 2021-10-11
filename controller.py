import os
import random
import hashlib
import string
from datetime import datetime, timedelta

from Model.pizza_sql_model import Customers

pepper_letters = ["a", "b", "c", "d", "e", "f"]


def hash_password(password: str):
    salt = os.urandom(32)

    pepper_loc = random.randint(0, len(password))
    pepper_char = random.choice(pepper_letters)
    password = password[:pepper_loc] + pepper_char + password[pepper_loc:]

    key = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        100000,
    )

    return salt + key


def check_password(the_customer: Customers, password: str):
    salt = the_customer.hashed_password[:32]
    key = the_customer.hashed_password[32:]
    for pepper_letter in pepper_letters:
        for pepper_loc in range(len(password)):
            pepper_password = password[:pepper_loc] + pepper_letter + password[pepper_loc:]
            new_key = hashlib.pbkdf2_hmac(
                "sha256", pepper_password.encode("utf-8"), salt, 100000
            )
            if new_key == key:
                return True

    return False


# Function to validate the password
def password_complexity(password):
    message = []

    if len(password) < 6:
        message.append("length should be at least 6<br/>")

    if len(password) > 20:
        message.append("length should be not be greater than 20<br/>")

    if not any(char.isdigit() for char in password):
        message.append("Password should have at least one numeral<br/>")

    if not any(char.isupper() for char in password):
        message.append("Password should have at least one uppercase letter<br/>")

    if not any(char.islower() for char in password):
        message.append("Password should have at least one lowercase letter<br/>")

    if message:
        return message
    else:
        return False


def set_every_item_to_string(initial_string: str, dict_to_attach):
    string = initial_string
    iterable_dict = dict_to_attach.items()
    for value in iterable_dict:
        string = string + str(value)
    return string


def check_time(latest_update):
    #last_update = datetime.strptime(latest_update, '%a, %d %b %Y %H:%M:%S %Z')
    last_update_plus_5 = latest_update + timedelta(minutes=5)
    last_update_plus_30 = latest_update + timedelta(minutes=30)
    current_time = datetime.now()
    if (current_time < last_update_plus_5) | (current_time > last_update_plus_30):
        return "True"
    else:
        return "False"


def create_random_string():
    length = 8
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str
