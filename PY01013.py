from math import *
def tinh_tong_UCLN(n):
    tong = 0
    while n != 0:
        tong += n % 10
        n //= 10
    return tong

def kiem_tra_SNT(tong):
    if tong < 2:
        return "NO"
    for i in range(2,isqrt(tong)+1):
        if tong % i == 0:
            return "NO"
    return "YES"

tc = int(input())
for j in range(tc):
    a,b = map(int, input().split())
    n = gcd(a,b)
    tong = tinh_tong_UCLN(n)
    print(kiem_tra_SNT(tong))