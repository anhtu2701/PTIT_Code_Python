import math
def isPrime(n):
    if n < 2: return False
    for t in range(2, math.isqrt(n)+1):
        if n % t == 0:
            return False
    return True

x = int(input())
n = [int(i) for i in input().split()]
prime_count = {}
for num in n:
    if isPrime(num):
        if num in prime_count:
            prime_count[num] += 1
        else:
            prime_count[num] = 1
for num in prime_count:
    print(str(num) + " " + str(prime_count[num]))