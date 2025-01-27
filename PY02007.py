A = [int(i) for i in input().split()]
while len(A) < 10:
    A += list(map(int,input().split()))
for i in range(len(A)):
    A[i] = A[i]  % 42
print(len(set(A)))



