arr = []
N = 10**18
i = 1
while i <= N:
    j = 1
    while j <= N:
        k = 1
        while k <= N:
            arr += [i*j*k]
            k *= 5
        j *= 3
    i *= 2
arr.sort()

def binary_search(l,r,x):
    if l > r:
        return "Not in sequence"
    m = (l+r)//2
    if arr[m] == x:
        return m+1
    if arr[m] > x:
        return binary_search(l,m-1,x)
    return binary_search(m+1,r,x)

for _ in range(int(input())):
    n = int(input())
    print(binary_search(0,len(arr),n))