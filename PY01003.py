# Cho số nguyên dương không quá 9 chữ số. Hãy làm tròn số N theo quy tắc sau:
# Nếu N>10, làm tròn đến số hàng chục gần nhất
# Sau đó nếu kết quả lớn hơn 100 thì làm tròn đến số hàng trăm gần nhất
# Sau đó nếu kết quả lớn hơn 1000 thì làm trong đến số hàng nghìn gần nhất
# Cứ tiếp tục như vậy …
# Chú ý: Giá trị 5 sẽ được làm tròn lên.

for _ in range(int(input())):
    xau = [int(i) for i in input()]
    for j in range(len(xau)-1,0,-1):
        if xau[j] >= 5:
            xau[j-1] = xau[j-1] + 1
        xau[j] = 0
    if xau[0] == 10:
        xau[0] = 0
        xau = [1] + xau
    for k in xau:
        print(k, end = "")
    print()
        