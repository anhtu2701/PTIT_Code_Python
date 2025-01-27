# Nhập số lượng sinh viên
N = int(input())

# Danh sách lưu thông tin mỗi sinh viên
students = []

# Vòng lặp để thu thập thông tin của sinh viên
for _ in range(N):
    name = input()  # Tên sinh viên
    C, T = map(int, input().split())  # Số bài làm đúng và số lượt submit
    students.append((name, C, T))  # Lưu vào danh sách dưới dạng tuple

# Sắp xếp danh sách sinh viên theo yêu cầu:
# - Đầu tiên sắp xếp theo C giảm dần
# - Sau đó sắp xếp theo T tăng dần
# - Cuối cùng sắp xếp theo tên theo thứ tự từ điển
students.sort(key=lambda x: (-x[1], x[2], x[0]))

# Xuất kết quả danh sách sinh viên đã sắp xếp
for student in students:
    print(student[0], student[1], student[2])
