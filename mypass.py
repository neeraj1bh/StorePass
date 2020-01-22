from random import *
import string
import random
import pyperclip 
from tkinter import *
from tkinter.ttk import *


characters = "!@# $%^&*().?" + string.digits + string.ascii_letters
l_char = list(characters)
symbols = "!@# $%^&*().?"
l_symb = list(symbols)


# Functions for calculation of password 
def generate_password1():
    entry1.delete(0, END)
    length = var1.get() 
    password = "".join(random.sample(characters, length))
    return password


def generate_password2():
    entry2.delete(0, END)
    length = var1.get() 
    password = "".join(choice(characters) for x in range(length))
    return password


def generate_password3():
    entry3.delete(0, END)
    length = var1.get() 
    password = ""
    for n in range(length):
        x = random.randint(0, 69)
        password += l_char[x]
    return password


def generate_password4():
    entry4.delete(0, END)
    length = var1.get() 
    password = []
    for n in range(length):
        alpha = random.choice(string.ascii_letters)
        symbol = random.choice(l_symb)
        number = random.choice(string.digits)
        password.append(alpha)
        password.append(symbol)
        password.append(number)

    password = "".join(str(x) for x in password)
    password = "".join(choice(password) for x in range(length))
    return password


# Function for generation of password 
def generate(): 
    password1 = generate_password1()
    entry1.insert(10, password1)
    password2 = generate_password2()
    entry2.insert(10, password2)
    password3 = generate_password3()
    entry3.insert(10, password3)
    password4 = generate_password4()
    entry4.insert(10, password4)


# Function for copying password to clipboard 
def scopy1(): 
    random_password = entry1.get() 
    pyperclip.copy(random_password) 


def scopy2(): 
    random_password = entry2.get() 
    pyperclip.copy(random_password) 


def scopy3(): 
    random_password = entry3.get() 
    pyperclip.copy(random_password) 


def scopy4(): 
    random_password = entry4.get() 
    pyperclip.copy(random_password) 

# Main Function 

# create GUI window 
root = Tk()
var1 = IntVar()

# Title of your GUI window 
root.title("Random Password Generator") 

# create label and entry to show 
# password generated 
Random_password1 = Label(root, text="Password1") 
Random_password1.grid(row=1)
Random_password2 = Label(root, text="Password2") 
Random_password2.grid(row=2)
Random_password3 = Label(root, text="Password3") 
Random_password3.grid(row=3)
Random_password4 = Label(root, text="Password4") 
Random_password4.grid(row=4)
entry1 = Entry(root) 
entry1.grid(row=1, column=1)
entry2 = Entry(root) 
entry2.grid(row=2, column=1)
entry3 = Entry(root) 
entry3.grid(row=3, column=1)
entry4 = Entry(root) 
entry4.grid(row=4, column=1)

# create label for length of password 
c_label = Label(root, text="Length") 
c_label.grid(row=0) 

# create Buttons Save & Copy which will save & copy 
# password to clipboard and Generate 
# which will generate the password 
generate_button = Button(root, text="Generate", command=generate) 
generate_button.grid(row=0, column=2) 
scopy_button1 = Button(root, text="Save & Copy", command=scopy1) 
scopy_button1.grid(row=1, column=2) 
scopy_button2 = Button(root, text="Save & Copy", command=scopy2) 
scopy_button2.grid(row=2, column=2) 
scopy_button3 = Button(root, text="Save & Copy", command=scopy3) 
scopy_button3.grid(row=3, column=2) 
scopy_button4 = Button(root, text="Save & Copy", command=scopy4) 
scopy_button4.grid(row=4, column=2) 

# Combo Box for length of your password 
combo = Combobox(root, textvariable=var1) 
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 
                17, 18, 19, 20, 21, 22, 23, 24, 25, 
                26, 27, 28, 29, 30, "Length") 
combo.current(0) 
combo.bind('<<ComboboxSelected>>') 
combo.grid(row=0, column=1) 

# start the GUI 
root.mainloop() 

