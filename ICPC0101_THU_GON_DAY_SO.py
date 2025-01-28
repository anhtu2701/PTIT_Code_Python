# n = int(input())
# ds = [int(i) for i in input().split()]
# i = 1
# while i < len(ds):
#     if (ds[i] + ds[i-1]) % 2 == 0:
#         ds.pop(i)
#         ds.pop(i-1)
#         if i > 1:
#             i -= 1
#     else:
#         i += 1
# print(len(ds))

n = int(input())
ds = [int(i) for i in input().split()]
stack = []

for x in ds:
    if stack and (stack[-1] + x) % 2 == 0:
        stack.pop()
    else:
        stack.append(x)

print(len(stack))

# Khởi tạo:

# n = 10 (đọc vào số lượng phần tử - không dùng trong xử lý).
# ds = [1, 5, 5, 8, 6, 4, 3, 5, 9, 3] (danh sách các số cần xử lý).
# stack = [] (khởi tạo stack trống).
# Duyệt qua các phần tử của ds:

# Phần tử 1:

# stack hiện tại: [] (trống).
# Vì stack trống, chúng ta bỏ qua điều kiện và thêm 1 vào stack.
# Kết quả stack: [1].
# Phần tử 5:

# stack hiện tại: [1].
# Tổng của stack[-1] + x = 1 + 5 = 6, là số chẵn.
# Điều kiện thỏa mãn, ta xóa 1 khỏi stack bằng pop.
# Kết quả stack: [].
# Phần tử 5:

# stack hiện tại: [].
# Vì stack trống, chúng ta bỏ qua điều kiện và thêm 5 vào stack.
# Kết quả stack: [5].
# Phần tử 8:

# stack hiện tại: [5].
# Tổng của stack[-1] + x = 5 + 8 = 13, là số lẻ.
# Điều kiện không thỏa mãn, ta thêm 8 vào stack.
# Kết quả stack: [5, 8].
# Phần tử 6:

# stack hiện tại: [5, 8].
# Tổng của stack[-1] + x = 8 + 6 = 14, là số chẵn.
# Điều kiện thỏa mãn, ta xóa 8 khỏi stack bằng pop.
# Kết quả stack: [5].
# Phần tử 4:

# stack hiện tại: [5].
# Tổng của stack[-1] + x = 5 + 4 = 9, là số lẻ.
# Điều kiện không thỏa mãn, ta thêm 4 vào stack.
# Kết quả stack: [5, 4].
# Phần tử 3:

# stack hiện tại: [5, 4].
# Tổng của stack[-1] + x = 4 + 3 = 7, là số lẻ.
# Điều kiện không thỏa mãn, ta thêm 3 vào stack.
# Kết quả stack: [5, 4, 3].
# Phần tử 5:

# stack hiện tại: [5, 4, 3].
# Tổng của stack[-1] + x = 3 + 5 = 8, là số chẵn.
# Điều kiện thỏa mãn, ta xóa 3 khỏi stack bằng pop.
# Kết quả stack: [5, 4].
# Phần tử 9:

# stack hiện tại: [5, 4].
# Tổng của stack[-1] + x = 4 + 9 = 13, là số lẻ.
# Điều kiện không thỏa mãn, ta thêm 9 vào stack.
# Kết quả stack: [5, 4, 9].
# Phần tử 3:

# stack hiện tại: [5, 4, 9].
# Tổng của stack[-1] + x = 9 + 3 = 12, là số chẵn.
# Điều kiện thỏa mãn, ta xóa 9 khỏi stack bằng pop.
# Kết quả stack: [5, 4].
# Kết quả cuối cùng:

# Sau khi duyệt qua toàn bộ danh sách ds, stack còn lại là [5, 4].
# Độ dài của stack là 2.
# Kết quả in ra: 2.
