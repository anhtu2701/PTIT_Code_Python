for _ in range(int(input())):
    ds = input()
    res = ''
    for i in ds:
        if i.isalpha():
            res += ' '
        else:
            res += i
    while '  ' in res:
        res = res.replace('  ',' ')
    lst = [int(i) for i in res.split()]
    print(min(lst))