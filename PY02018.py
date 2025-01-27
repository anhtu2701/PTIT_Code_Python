n = int(input())
a = [int(i) for i in input().split()]
a.sort()
for j in a:
    if j + 1 not in a:
        print(j+1)
        break