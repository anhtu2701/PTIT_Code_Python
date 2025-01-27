# Hãy kiểm tra xem số đó có thỏa mãn đồng thời ba tính chất sau hay không?
# Vị trí chẵn là chữ số chẵn
# Vị trí lẻ là chữ số lẻ
# Tổng chữ số là một số nguyên tố.
import math
def isPrimeNumber(s):
    if s < 2:
        return False
    for k in range(2,math.isqrt(s)+1):
        if  s % k == 0:
            return False
        return True
    
def check_Vi_Tri(y):
    for i in range(len(y)):
        if i % 2 == 0:
            if y[i] % 2 == 0:
                return True
            return False
        else:
            if  y[i] % 2 != 0:
                return True
            return False

for _ in range(int(input())):
    n = [int(i) for i in input()]
    if check_Vi_Tri(n) and isPrimeNumber(sum(map(int,n))):
        print("YES")
    else:
        print("NO")
