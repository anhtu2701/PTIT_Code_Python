from collections import Counter
for _ in range(int(input())):
    n = int(input())
    data = [str(i) for i in input().split()]
    counter = Counter(data)

    arr = sorted(counter.items(), key=lambda x: (-x[1], int(x[0])))
    if arr[0][1] > n/2:
        print(arr[0][0])
    else:
        print("NO")