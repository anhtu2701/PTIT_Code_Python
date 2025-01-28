n = int(input())
ds = []
# while len(ds) < n:
#     ma_mon = input()
#     ten_mon = input()
#     hinh_thuc = input()
#     ds.append((ma_mon,ten_mon,hinh_thuc))
# Tối ưu:
ds = [tuple(input() for _ in range(3)) for _ in range(n)]

ds.sort(key = lambda x: x[0])
for i in ds:
    print(i[0] + ' ' + i[1] + ' ' + i[2])
