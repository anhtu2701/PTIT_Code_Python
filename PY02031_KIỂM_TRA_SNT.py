def isPrime(n):
    if n < 2:
        return 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1

N, M = map(int, input().split())
for i in range(N): # Đề bài yêu cầu là N dòng nên phải chạy vòng lặp N lần
    arr = [isPrime(int(i)) for i in input().split()]
    print(*arr)