# Một số nguyên dương được gọi là ưu thế nguyên tố nếu thỏa mãn cả hai điều kiện:

# Số chữ số của nó là một số nguyên tố
# Số lượng chữ số nguyên tố nhiều hơn số lượng chữ số không nguyên tố
# Viết chương trình kiểm tra một số nguyên có thỏa mãn ưu thế nguyên tố hay không.
def ktra_SNT(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def soluong(x):
    cnt = 0
    for j in x:
        if j in {'2', '3', '5', '7'}:
            cnt += 1
    if cnt <= len(x) - cnt:
        return False
    return True

for _ in range(int(input())):
    n = input().strip()
    if soluong(n) and ktra_SNT(len(n)):
        print("YES")
    else:
        print("NO")

