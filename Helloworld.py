# from collections import defaultdict

# def sang():
#     """Hàm sàng Eratosthenes để tìm ước nguyên tố nhỏ nhất của các số."""
#     for i in range(2, MAX_A + 1):
#         p[i] = i
#     for i in range(2, int(MAX_A**0.5) + 1):
#         if p[i] == i:  # i là số nguyên tố
#             for j in range(i * i, MAX_A + 1, i):
#                 if p[j] == j:
#                     p[j] = i

# def phan_tich(n):
#     """Phân tích số n thành thừa số nguyên tố và cập nhật số mũ."""
#     while n > 1:
#         prime_factor = p[n]
#         while n % prime_factor == 0:
#             n //= prime_factor
#             cnt[prime_factor] += 1

# # Khởi tạo các biến
# MAX_A = 10**6
# MOD = 10**9 + 7
# p = [0] * (MAX_A + 1)  # Mảng lưu ước nguyên tố nhỏ nhất
# cnt = defaultdict(int)  # Lưu số mũ của các thừa số nguyên tố

# # Tìm ước nguyên tố nhỏ nhất cho mỗi số từ 1 đến MAX_A
# sang()

# # Đọc đầu vào
# n = int(input())
# A = list(map(int, input().split()))

# # Phân tích từng phần tử của mảng
# for x in A:
#     phan_tich(x)

# # Tính số ước
# ans = 1
# for prime, power in cnt.items():
#     ans *= (power + 1)
#     ans %= MOD

# print(ans)

# def convert_dis(km):
#   m = km * 1000
#   return m
# km = 55
# m = convert_dis(km)
# print("The distance in mile is: " + str(m))

# def print_seconds(hours,minutes,seconds):
#   res = hours * 3600 + minutes * 60 + seconds
#   print("Tổng số giây là:",res)
# print_seconds(2,30,20)

