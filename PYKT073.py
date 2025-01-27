n = int(input())
arr = ''
while len(arr) < n:
    arr += str(len(input().split()))

arr = arr.replace('68','1')
arr = arr.replace('7777','2')
while '11' in arr:
    arr = arr.replace('11','1')
print(len(arr))
for i in arr:
    print(i)