# Cho N số nguyên. Nhiệm vụ của bạn là phân tích các số nguyên đã cho dưới dạng tích của các thừa số nguyên tố, sau đó tính tổng các ước số nguyên tố này.
import math
def sum_number(n):
    sum = 0
    for i in range(2,math.isqrt(n)+1):
        while n % i == 0:
            sum += i
            n /= i
    if n > 1:
        sum += n
    return sum

res = 0
for _ in range(int(input())):
    n = int(input())
    res += sum_number(n)
print(int(res))
print()



