from math import *
def tim_tong_chu_so(n):
    tong = sum(map(int,str(n)))
    return tong

def kiem_tra_SNT(tong):
    if tong < 2:
        return "NO"
    else:
        for i in range(2,isqrt(tong)+1):
            if tong % i == 0:
                return "NO"
        return "YES"

tc = int(input())
for _ in range(tc):
    n = int(input())
    tong = tim_tong_chu_so(n)
    print(kiem_tra_SNT(tong))

