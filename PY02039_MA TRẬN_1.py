if __name__ == "__main__":
    n = int(input())
    arr = [[int(i) for i in input().split()] for _ in range(n)]
    k = int(input())
    sum = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                sum += arr[i][j]
            elif i > j:
                sum -= arr[i][j]
    sum = abs(sum)
    if sum > k:
        print("NO",sum,sep="\n")
    else:
        print("YES",sum,sep="\n")

# if __name__ == "__main__":
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     k = int(input())

#     sum_up = sum(arr[i][j] for i in range(n) for j in range(i+1, n))  # Chỉ lấy phần trên đường chéo
#     sum_down = sum(arr[i][j] for i in range(1, n) for j in range(i))  # Chỉ lấy phần dưới đường chéo

#     diff = abs(sum_up - sum_down)  # Chỉ tính hiệu số một lần

#     print("YES" if diff <= k else "NO", diff, sep="\n")
