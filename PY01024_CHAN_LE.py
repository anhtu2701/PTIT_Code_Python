# Cho số nguyên dương N. Hãy kiểm tra xem N có thỏa mãn đồng thời hai tính chất sau đây hay không?

# Tổng chữ số của N chia hết cho 10
# Các chữ số cạnh nhau đều khác nhau đúng 2 đơn vị

def tong_chu_so_chia_het_10(n):
    s = int(sum(map(int,n)))
    if s % 10 == 0:
        return True
    return False

def check_number_2(n):
    for i in range(len(n)-1):
        if abs(int(n[i]) - int(n[i+1])) == 2:
            return True
    return False

for _ in range(int(input())):
    n = input()
    if tong_chu_so_chia_het_10(n) and check_number_2(n):
        print("YES")
    else:
        print("NO")