from itertools import combinations
if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = sorted(list({int(x) for x in input().split()}))
    lst = combinations(arr, k)
    for i in lst:
        print(" ".join(map(str, i)))
