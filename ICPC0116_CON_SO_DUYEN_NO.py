# Con số duyên nợ là con số có chữ số đầu và chữ số cuối giống nhau.
#
# Viết chương trình kiểm tra xem một số nguyên dương n ghi trong hệ thập phân có chữ số đầu và chữ số cuối giống nhau không?

def check_number(n):
    a = len(n)
    if n[0] == n[a-1]:
        return 'YES'
    return 'NO'

for _ in range(int(input())):
    n = input()
    print(check_number(n))