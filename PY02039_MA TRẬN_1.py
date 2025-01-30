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