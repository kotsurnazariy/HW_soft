#1
def fl(lst):
    s = 0
    i = 0
    for i in lst:
    s += i
    return print(s / len(lst))
fl([2, 4, 6])


#2
# def modul (b):
#     """Modul number"""
#     if b >= 0:
#         return print(b)
#     else:
#         return print(-b)
# modul(10)

#3
# def max_num (g, k):
#     """
#     Print max number
#     """
#     if g > k:
#         print(g)
#     else:
#         print(k)
#     return max(g, k)
# max_num(6, 8)

#4

#5
def suma_num (a):
    i = 1
    while i <= a:
        print(i)
        i += 1
        c = [i].append
        print(c)
    else:
        print('finish')
suma_num(5)