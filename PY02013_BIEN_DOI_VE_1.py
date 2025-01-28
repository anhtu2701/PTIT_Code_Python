def count(n):
    cnt = 1
    while n != 1:
        if n % 2 == 0:
            cnt += 1
            n /= 2
        else:
            cnt += 1
            n = n*3 +1
    return cnt
n = int(input())
while n >= 0:
    if n == 0:
        break
    else:
        print(count(n))
        n = int(input())