#Nhập số nguyên dương N (1 < N < 10000).Viết chương trình tính tổng:
#S = 1 + 1/3 + 1/5 + … + 1/N nếu N lẻ
#S = 1/2 + 1/4 + 1/6 + … + 1/N nếu N chẵn
#Kết quả được in ra với 6 chữ số phần thập phân.

tc = int(input())
for i in range(tc):
    N = int(input())
    sum = 0
    if N % 2 == 0:
        for j in range(2, N + 1, 2):
            sum += 1 / j
    else:
        for j in range(1, N + 1, 2):
            sum += 1 / j
    print('%.6f' % sum)