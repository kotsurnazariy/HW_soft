#1
# a = 0
# while a < 100:
#     print (a)
#     a += 2

# a = 0
# for a in range(0, 100, 2):
#     print(a)

#2
# a = 1
# while a < 100:
#     print(a)
#     a += 2

# a = 1
# for a in range(100):
#     if a % 2 == 0:
#         continue
#     print(a, end=' ')

#3
# a = [2, 4, 6, 7, 10]
# for a in a:
#     if a % 2 == 1:
#         print('This list have odd number', a)
#         break
#     else:
#         print('This even number:', a)

#4
# my_list = [1, 2, 3, 4, 5]
# i = 0
# for my_list[i] in my_list:
#     b_len = float(my_list[i])
#     print(b_len)
#     i += 1

#5
# n = input("Enter any-thing number: ")
# n = int(n)
# fib_1 = 0
# fib_2 = 1
# print(fib_1)
# while fib_2 <= n:
#     temp = fib_2
#     fib_2 = fib_1 + fib_2
#     fib_1 = temp
#     print(temp)

#6
# my_list = ['one', 'two', 'three', 'four']
# i = 0
# for my_list[i] in my_list:
#     print(my_list[i])
#     i += 1

#7
# my_list = ['one', 'two', 'three', 'four']
# i = 0
# a = 0
# for my_list[i] in my_list:
#     for a in my_list[i]:
#         print(a, end="#")
#     i += 1

#8


#9
# import random
# num_rund = random.randint(100, 1000)
# print(num_rund)
# list_rund = list(str(num_rund))
# print(list_rund)
# print(max(list_rund))

#10
# word = input('Enter word: ')
# word_polin = word[::-1]
# if word == word_polin:
#     print('Polinom:', word)
# else:
#     print("Not polinom:", word)