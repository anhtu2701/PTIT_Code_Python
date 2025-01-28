# Hệ cơ số 3 chỉ biểu diễn các số sử dụng ba chữ số là 0, 1, 2.

# Nhập vào dãy biểu diễn không quá 18 ký tự, hãy kiểm tra xem dãy biểu diễn nào là đúng với hệ cơ số 3.

# Input

# Dòng đầu là số bộ test, mỗi dòng tiếp theo ghi một dãy biểu diễn cần kiểm tra.

# Output

# Nếu đúng in ra YES, nếu sai in ra NO.
def check_number(s):
    for i in s:
        if i not in ('1', '2', '0'):
            return 'NO'
    return 'YES'
        

for i in range(int(input())):
    s = input()
    print(check_number(s))
