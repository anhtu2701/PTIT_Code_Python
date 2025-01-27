#Một cặp số nguyên dương (a,b) được gọi là nguyên tố cùng nhau nếu a và b có ước chung lớn nhất bằng 1.Cho hai số nguyên dương N và K trong đó 10 < N < 10000; 1 < K < 6.Hãy liệt kê các số có K chữ số thỏa mãn nguyên tố cùng nhau với N.
from math import *
N,K = map(int, input().split())
count = 0
for i in range(10**(K-1),10**K):
    if gcd(i,N) == 1:
        print(i, end=' ')
        count += 1
        if count % 10 == 0:
            print()