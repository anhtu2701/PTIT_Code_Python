def sang(n):
    a = [True] * (n+1)
    a[0] = a[1] = False
    for i in range(2, n+1):
        if a[i]:
            for j in range(i*i, n+1, i):
                a[j] = False
    return [i for i in range(2, n+1) if a[i]]
n, x = map(int, input().split())
prime = sang(1000)
arr = prime[:n]
lst = [x]
for i in arr:
    lst.append(lst[-1] + i)
print(' '.join(map(str, lst)))
