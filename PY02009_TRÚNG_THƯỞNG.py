from collections import Counter
for _ in range(int(input())):
    n = int(input())
    data = [input() for _ in range(n)]
    counter = Counter(data)
    sorted_data = sorted(counter.items(), key = lambda x: (-x[1], int(x[0])))
    print(sorted_data[0][0])
        