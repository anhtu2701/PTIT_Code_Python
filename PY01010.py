# Viết chương trình kiểm tra xem số nguyên dương N có thỏa mãn tính chất: nếu ta lấy hai chữ số đầu và hai chữ số cuối của nó thì sẽ tạo ra số có hai chữ số giống nhau hay không?

# Input

# Dòng đầu ghi số số test (không quá 20). Mỗi test là 1 số nguyên dương N có ít nhất 4 chữ số, nhưng không quá 18 chữ số.

# Output

# Ghi ra YES hoặc NO

for i in range(int(input())):
    n = input()
    s = len(n)
    if n[0] == n[s-2] and n[1] == n[s-1]:
        print("YES")
    else:
        print("NO")
