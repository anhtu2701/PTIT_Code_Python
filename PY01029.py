#Trong toán học, cặp số (a,b) được gọi là nguyên tố cùng nhau nếu ước số chung lớn nhất của a và b bằng 1.Cho số nguyên dương N không quá 9 chữ số. Hãy kiểm tra xem N và số đảo của N có phải là một cặp số nguyên tố cùng nhau hay không.
from math import *
test_case = int(input())
for i in range(test_case):
    N = int(input())
    M = int(str(N)[::-1]) # [::-1] là cú pháp đảo ngược chuỗi
    if gcd(N,M) == 1:
        print("YES")
    else: print("NO")