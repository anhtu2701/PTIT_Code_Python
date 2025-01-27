fibo = [1] * 93
for i in range(3,93):
    fibo[i] = fibo[i-2] + fibo[i-1]

for _ in range(int(input())):
    a,b = map(int,input().split())
    for i in range(a,b+1):
        print( fibo[i], end = ' ')
    print()