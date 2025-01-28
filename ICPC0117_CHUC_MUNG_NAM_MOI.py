n = int(input())
A = []
while len(A) < n:
    A.append(input())
print(len(set(A)))
