while True:
    A = [int(t) for t in input().split()]
    if A.count(0) == 4:
        break
    cnt = 0
    while len(set(A)) != 1:
        new_A = A.copy()
        for i in range(4):
            if i == 3:
                A[i] = abs(new_A[3] - new_A[0])
            else:
                A[i] = abs(new_A[i] - new_A[i+1])
        cnt += 1
    print(cnt)
