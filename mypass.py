from random import *
import string
import random


characters = "!@# $%^&*().?" + string.digits + string.ascii_letters
l_char = list(characters)
symbols = "!@# $%^&*().?"
l_symb = list(symbols)
letters = int(input("Enter no. of letters in password : "))


def generate_password(num):
    password = "".join(random.sample(characters, letters))
    return password


def generate_password2(num):
    password = "".join(choice(characters) for x in range(num))
    return password


def generate_password3(num):
    password = ""
    for n in range(num):
        x = random.randint(0, 69)
        password += l_char[x]
    return password


def generate_password4(num):
    password = []
    for n in range(num):
        alpha = random.choice(string.ascii_letters)
        symbol = random.choice(l_symb)
        number = random.choice(string.digits)
        password.append(alpha)
        password.append(symbol)
        password.append(number)
    password = "".join(str(x) for x in password)
    password = "".join(choice(password) for x in range(num))
    return password


print(generate_password(letters))
print(generate_password2(letters))
print(generate_password3(letters))
print(generate_password4(letters))
