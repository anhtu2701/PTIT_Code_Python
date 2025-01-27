# Một số được gọi là xen kẽ nếu thỏa mãn cả ba tính chất sau:

# Số chữ số là số lẻ
# Chữ số đầu tiên khác chữ số thứ hai.
# Các số ở vị trí đầu tiên, vị trí thứ 3, vị trí thứ 5…  và vị trí cuối cùng có giá trị bằng nhau
# Viết chương trình kiểm tra một số có phải xen kẽ hay không.

def check(n):
    for i in range(2,len(n),2):
        if n[i] != n[0]:
            return False
    return True


for _ in range(int(input())):
    n = input()
    if len(n) % 2 == 1 and n[0] != n[1] and check(n):
        print("YES")
    else:
        print("NO")