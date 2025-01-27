# from math import *
# def test(n):
#     a = str(n % 10000).replace('0','')
#     if a == '':
#         return "NO"
#     a = int(a)
#     if a < 2:
#         return 'NO'
#     for i in range(2,isqrt(a)+1):
#         if a % i == 0:
#             return "NO"
#     return "YES"
        
# tc = int(input())
# for _ in range(tc):
#     n = int(input())
#     print(test(n))


import math

def kiem_tra_SNT(n):
    if n < 2:
        return "NO"
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            return "NO"
    return "YES"

for _ in range(int(input())):
    s = input()
    n = int(s[-4:])
    print(kiem_tra_SNT(n))