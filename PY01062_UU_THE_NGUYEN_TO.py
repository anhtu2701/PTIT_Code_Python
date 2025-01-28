# Một số nguyên dương được gọi là ưu thế nguyên tố nếu thỏa mãn cả hai điều kiện:
# Số chữ số của nó là một số nguyên tố
# Số lượng chữ số nguyên tố nhiều hơn số lượng chữ số không nguyên tố
# Viết chương trình kiểm tra một số nguyên có thỏa mãn ưu thế nguyên tố hay không.
import math
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def countPrime(x):
    count_Prime = 0
    count_Number = 0
    for j in x:
        if isPrime(int(j)):
            count_Prime += 1
        else:
            count_Number += 1
    if  count_Prime > count_Number and isPrime(len(x)):
        return "YES"
    else:
        return "NO"
    
for _ in range(int(input())):
    n = input().strip()
    print(countPrime(n))

