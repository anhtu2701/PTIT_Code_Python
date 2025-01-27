q = int(input())
for _ in range(q):
    s = input() + " "
    ans = ""
    cnt = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            cnt += 1
        else:
            ans += str(cnt) + s[i]
            cnt = 1
    print(ans)