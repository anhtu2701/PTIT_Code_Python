# Cho số nguyên dương N có không quá 500 chữ số.
# Hãy kiểm tra xem 4 chữ số cuối cùng ghép lại có tạo thành một số nguyên tố hay không.
# Chú ý: các chữ số 0 ở đầu trong 4 chữ số cuối vẫn được chấp nhận
# Input
# Dòng đầu ghi số bộ test (không quá 20).
# Mỗi test viết trên một dòng số nguyên dương N, không quá 500 chữ số.
# Output
# Với mỗi bộ test ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.
import math
def is_PrimeNumber(n):
    if len(str(n)) > 500:
        return "NO"
    if n < 2:
        return "NO"
    for i in range(2, math.isqrt(n) +1):
        if n % i == 0: return "NO"
    return "YES" if n > 1 else "NO" 

for _ in range(int(input())):
    s = input()
    n = int(s[-4:])
    print(is_PrimeNumber(n))