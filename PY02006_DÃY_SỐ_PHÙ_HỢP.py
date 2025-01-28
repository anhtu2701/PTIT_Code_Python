def solve(A, B):
    for i in range(len(A)):
        if A[i] > B[i]:
            return "NO"
    return "YES"

for _ in range(int(input())):
    n = int(input())
    A = sorted([int(x) for x in input().split()])
    B = sorted([int(x) for x in input().split()])
    print(solve(A, B))
