for _ in range(int(input())):
    n, d = map(int, input().split())
    lst = [int(i) for i in input().split()]
    arr = lst[d:] + lst[:d]
    print(*arr)
    
