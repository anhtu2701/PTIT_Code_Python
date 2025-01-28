import itertools

# Đọc giá trị N
N = int(input())

# Tạo danh sách lưu các xâu thỏa mãn điều kiện
result = []

# Duyệt qua các độ dài từ 1 đến N
for length in range(1, N + 1):
    # Tạo các tổ hợp với độ dài `length`
    for comb in itertools.product("ABC", repeat=length):
        # Đếm số lần xuất hiện của mỗi ký tự
        countA = comb.count('A')
        countB = comb.count('B')
        countC = comb.count('C')
        
        # Kiểm tra điều kiện
        if countA <= countB <= countC and countA > 0 and countB > 0 and countC > 0:
            # Chuyển tuple sang chuỗi và thêm vào kết quả
            result.append("".join(comb))

# Sắp xếp kết quả theo thứ tự từ độ dài ngắn nhất đến dài nhất, và từ điển
result.sort(key=lambda x: (len(x), x))

# In kết quả
for r in result:
    print(r)
