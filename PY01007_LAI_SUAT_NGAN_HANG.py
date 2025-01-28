tc = int(input())
for i in range(tc):
    count = 0
    N,X,M = map(float, input().split())
    while N <= M:
        count += 1
        N = N + N*(X/100)
    print(count)