# Cho số nguyên dương N, hãy liệt kê các số thuận nghịch nhỏ hơn N thỏa mãn điều kiện:
# Chỉ có các chữ số 0,2,4,6,8
# Số chữ số của N chia cho 2 dư 1
# Input
# Dòng đầu ghi số bộ test (không quá 10). Mỗi test viết một số N (22 < N <10^6)
def check_number(n):
    for i in n:
        if i not in {'0','2','4','6','8'}: return False
    if len(n) % 2 != 0 or n != n[::-1]: return False 
    else: return True
        

for _ in range(int(input())):
    n = input()
    for j in range(22, int(n),2):
        if check_number(str(j)):
            print(j, end=' ')
    print()
