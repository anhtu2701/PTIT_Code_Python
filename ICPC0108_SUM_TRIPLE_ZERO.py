for _ in range(int(input())):
    n = int(input())
    lst = [int(i) for i in input().split()]
    cnt = 0
    for j in range(len(lst)):
        for k in range(j+1,len(lst)):
            for h in range(k+1,len(lst)):
                if lst[j] + lst[k] + lst[h] == 0:
                    cnt += 1
    print(cnt)
