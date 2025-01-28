# Trong 10 chữ số thập phân thì có 4 chữ số nguyên tố là 2, 3, 5, 7.
# Một số nguyên dương được coi là thỏa mãn nguyên tố đúng vị trí nếu thỏa mãn cả hai điều kiện:
# Nếu i là nguyên tố thì vị trí thứ i cũng phải là chữ số nguyên tố.
# Ngược lại nếu i không phải là số nguyên tố thì vị trí thứ i không phải là chữ số nguyên tố. 
# Ví dụ: số 14239567 thỏa mãn nguyên tố đúng vị trí vì các vị trí thứ 2, 3, 5, 7 là các chữ số nguyên tố, các vị trí khác không nguyên tố. 
# Viết chương trình kiểm tra một số nguyên dương không quá 500 chữ số có thỏa mãn tính chất trên hay không. 
import math
def isPrime(x):
    if x < 2:
        return False
    for t in range(2, math.isqrt(x)+1):
        if  x % t == 0:
            return False
    return True

def check_PrimeDigits(n):
    for j in range(len(n)):
        if (isPrime(j) and not isPrime(n[j])) or (not isPrime(j) and isPrime(n[j])):
            return False
    return True

for _ in range(int(input())):
    n = [int(i) for i in input()]
    print("YES" if check_PrimeDigits(n) else "NO")



        