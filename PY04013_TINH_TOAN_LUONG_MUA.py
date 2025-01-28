from collections import defaultdict

# Hàm chuyển đổi thời gian từ hh:mm sang số phút từ 00:00
def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

# Nhập số lần đo
n = int(input())

# Tạo từ điển để lưu trữ thông tin lượng mưa và thời gian đo mưa cho mỗi trạm
stations = defaultdict(lambda: [0, 0])  # Mỗi trạm lưu trữ [tổng lượng mưa, tổng thời gian mưa]

# Nhập dữ liệu đo
for _ in range(n):
    name = input()  # Tên trạm
    start_time = input()  # Thời gian bắt đầu (hh:mm)
    end_time = input()  # Thời gian kết thúc (hh:mm)
    rain = float(input())  # Lượng mưa đo được
    
    # Tính số phút mưa từ thời gian bắt đầu đến kết thúc
    start_minutes = time_to_minutes(start_time)
    end_minutes = time_to_minutes(end_time)
    duration = end_minutes - start_minutes
    
    # Cập nhật lượng mưa và tổng thời gian mưa cho trạm
    stations[name][0] += rain  # Cộng thêm lượng mưa
    stations[name][1] += duration  # Cộng thêm thời gian mưa

# In kết quả
station_index = 1
for name, (total_rain, total_time) in stations.items():
    # Tính lượng mưa trung bình trên 1 giờ
    if total_time > 0:
        avg_rain_per_hour = total_rain / total_time * 60
    else:
        avg_rain_per_hour = 0
    
    # In kết quả: Mã trạm, tên trạm và lượng mưa trung bình (làm tròn đến 2 chữ số thập phân)
    print(f"T0{station_index} {name} {avg_rain_per_hour:.2f}")
    station_index += 1
