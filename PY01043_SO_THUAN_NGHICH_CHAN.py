# Cho số nguyên dương N không quá 6 chữ số.
# Hãy liệt kê các số nhỏ hơn N thỏa mãn cả ba điều kiện:
# N là số thuận nghịch
# Tất cả các chữ số của N đều chẵn
# Số chữ số của N cũng là một số chẵn
# Input
# Dòng đầu ghi số bộ test (không quá 10). Mỗi test viết một số N (22 < N <106)
# Output
# Ghi kết quả của mỗi test trên một dòng, mỗi số cách nhau đúng một khoảng trống.
def check_numbers(n):
    if len(str(n)) % 2 != 0 or n != n[::-1]:
        return False
    for i in n:
        if int(i) % 2!= 0:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    for j in range(22,n,2):
        if check_numbers(str(j)):
            print(j, end=' ')
    print()