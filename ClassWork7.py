#1
# while True:
#     try:
#         num = int(input('Enter eny-thing number: '))
#         if num % 2 == 0:
#             print('This parne num', num)
#         elif num % 2 == 1:
#             print('This neparne num', num)
#     except ValueError:
#         print('Don\'t put word try else')

#2
# class Negativ(Exception):
#     '''check that age is correct'''
#     def __init__(self, data):
#         self.data = data
#     def __str__(self):
#         return repr(self.data)

# def WhatAge():
#     while True:
#         try:
#             age = int(input('Put your age: '))
#             if age < 1:
#                 print("Your age cannot be negative or equal to zero")
#             elif age % 2 == 0:
#                 print("Your age is even number:", age)
#             elif age % 2 == 1:
#                 print("Your age is odd number:", age)
#         except ValueError:
#             print('You can\'t put word try else')

# WhatAge()