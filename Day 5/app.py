# Day 5 of 100

# For practice sum of even numbers
# maxnum = input("Number ")
# sum = 0
# for number in range (1,int(maxnum)+1):
#     if int(number) % 2 == 0:
#         sum = sum+number
# print(sum)

# Practice FizzBuzz game
# print("This is the solution of the first 100 turns in FizzBuzz:")
# for number in range (1,101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# Proyect 5 - PyPassword generator
import random

letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
symbols_list = ['!', '?', '¡', '¿']
number_list = ['1', '2', '3', '4']

letters = input("How many letters would you like in your password? ")
symbols = input("How many symbols would you like? ")
numbers = input("How many numbers would you like? ")

# Not random order in password

# password = ""
# for number in range(1, int(letters) + 1):
#     password += random.choice(letters_list)
# for number in range(1, int(symbols) + 1):
#     password += random.choice(symbols_list)
# for number in range(1, int(numbers) + 1):
#     password += random.choice(number_list)
# print(password)

# Random order in password
password_list = []
for number in range(1, int(letters) + 1):
    password_list += random.choice(letters_list)
for number in range(1, int(symbols) + 1):
    password_list += random.choice(symbols_list)
for number in range(1, int(numbers) + 1):
    password_list += random.choice(number_list)
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(password)