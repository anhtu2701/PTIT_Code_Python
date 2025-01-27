for _ in range (int(input())):
    n = input().split()
    ans = ''
    for i in n:
        if len(ans) + len(i) <= 100:
            ans += i + ' '
        else:
            break
    print(ans)
