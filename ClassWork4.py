#1
# import random
# num_rund = random.randint(1, 100)
# print(num_rund)
# while True:
#     user = int(input ('Еry to guess the number 1 to 100: '))
#     if user == num_rund:
#         print ('You right this:', num_rund)
#         break
#     elif user < num_rund:
#         print ('try else')
#     elif user > num_rund:
#         print ('try else')

#2
# import math
# while True:
#     user = input('What you want count? 1-Площа прямокутника, 2-Площа трикутника, 3-Площа кола 4-Вихід. Enter 1, 2, 3 or 4: ')
#     if user == '1':
#         x = float(input('Enter x = '))
#         y = float(input('Enter y = '))
#         print ('You result:', x*y)
#     elif user == '2':
#         h = float(input('Enter h = '))
#         a = float(input('Enter a = '))
#         print ('You result:', 0.5*h*a)
#     elif user == '3':
#         r = float(input('Enter r = '))
#         print ('You result:', math.pi * pow(r,2))
#     elif user == '4':
#         break
#     else:
#         print('Press only 1, 2, 3 or 4')