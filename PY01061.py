# Cho số nguyên dương N có ít nhất 4 chữ số và không quá 500 chữ số.

# Một số được gọi là số đầu cuối nguyên tố nếu thỏa mãn cả hai điều kiện:

# Ba chữ số đầu ghép lại được một số nguyên tố
# Ba chữ số cuối ghép lại được một số nguyên tố
# Viết chương trình kiểm tra xem N có phải là đầu cuối nguyên tố hay không?
import math
def kiem_tra_SNT(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

for _ in range(int(input())):
    n = input()
    if kiem_tra_SNT(int(n[0:3])) and kiem_tra_SNT(int(n[-3:])):
        print("YES")
    else: 
        print("NO")