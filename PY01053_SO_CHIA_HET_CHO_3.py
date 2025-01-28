#Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.
#Hãy kiểm tra xem N có chia hết cho 3 hay không.
tc = int(input())
for _ in range(tc):
    n = int(input())
    tong = sum(map(int, str(n)))
    if tong % 3 == 0:
        print("YES")
    else:
        print("NO")