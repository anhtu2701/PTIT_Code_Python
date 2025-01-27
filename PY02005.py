# Cho dãy số A[] gồm có N phần tử.
# Một cặp nghịch thế là một cặp số (u, v) sao cho u < v và A[u] > A[v]. Nhiệm vụ của bạn là hãy đếm số lượng cặp nghịch thế trong dãy số A[] ban đầu.

n = int(input())
arr = [int(i) for i in input().split()]
cnt = 0
for k in range(len(arr)-1):
    for j in range(k+1,len(arr)):
        if arr[k] > arr[j]:
            cnt += 1
print(cnt)