def check(s):
    if len(s) != 4:
        return "NO"
    for i in s:
        if str(i).isnumeric() == 0 or not (0 <= i <= 255):
            return "NO"
    return "YES"

for _ in range(int(input())):
    s = [int(i) for i in input().split('.')]
    print(check(s))
    