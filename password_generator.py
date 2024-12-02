# Importing required module
import random
from art import logo

"""
# Project: Password Generator Program
# Description:
This program generates a random password based on user input for the number of letters, symbols, and numbers. 
The password includes a mix of these characters, with their positions randomized to make it more secure.

Features:
    - Takes user input for the desired number of letters, symbols, and numbers.
    - Ensures randomness by shuffling the final password characters.
    - Includes error handling using a while loop and try-except block to validate user inputs.

This program helps create strong passwords that are harder for hackers to guess.

# Level: Intermediate
Author: Pranjal Sarnaikpi
Date: 2024-12-01
"""

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

while True:
    print(logo)
    print("Welcome to the Python Password Generator!")

    # Asking users to enter how many characters they want in their password

    while True:
        try:
            nr_letters = int(input("How many letters would you like in your password?\n"))
            nr_symbols = int(input(f"How many symbols would you like?\n"))
            nr_numbers = int(input(f"How many numbers would you like?\n"))
            break
        except ValueError:
            print("Error: Invalid input provided.")
            print("Please enter integer values.")

    # Created empty list to store random characters picked from lists
    password_list = []

    # Here We are picking random characters from lists and adding them to password_list
    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list.append(random.choice(symbols))

    for char in range(nr_numbers):
        password_list.append(random.choice(numbers))

    print("")

    # Here we are properly shuffling password_list 3 times
    for rounds in range(3):
        random.shuffle(password_list)

    print("")

    # To convert password list in string we are iterating through it using for loop and storing it in new empty string
    final_password = ""
    for letter in password_list:
        final_password += letter

    # Printing the final output
    print(f"The final password is : {final_password}")
    print("")

    continue_to_generate = input("Do you want to generate again (Y or N): ").upper()
    if continue_to_generate == "Y":
        print("\n"*30)
        continue
    else:
        print("Goodbye! Take care.")
        break
