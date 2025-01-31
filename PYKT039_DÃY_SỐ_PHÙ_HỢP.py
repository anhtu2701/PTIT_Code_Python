def solve(A,B):
    for i in range(len(A)):
        if A[i] > B[i]:
            return "NO"
    return "YES"

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        A = sorted([int(i) for i in input().split()])
        B = sorted([int(i) for i in input().split()])
        print(solve(A,B))