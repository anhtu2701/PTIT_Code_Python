# Cho ba số nguyên dương a, K, N. Hãy liệt kê tất cả các số nguyên dương b thỏa mãn cả hai điều kiện:
# a + b ≤ N
# a + b chia hết cho K
# Input
# Chỉ có một dòng ghi ba số nguyên dương theo thứ tự a, K, N (không quá 9 chữ số).
# Output
# Ghi ra lần lượt các số b tìm được theo thứ tự tăng dần.

a,K,N = map(int, input().split())
min_b = K - (a%K) if a % K != 0 else 0
if min_b > N-a or min_b == 0:
    print(-1)
else:
    for b in range(min_b,N-a+1,K):
        print(b, end = " ")


