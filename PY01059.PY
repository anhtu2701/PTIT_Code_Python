# Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số. Xét các vị trí từ trái qua phải (tính từ 0). Hãy tính:
# Tổng các chữ số ở vị trí chẵn
# Tích các chữ số ở vị trí lẻ. – giá trị tích chữ số có thể đến 18 chữ số. Chú ý khi tính tích bỏ qua các chữ số 0, nhưng nếu tất cả các vị trí lẻ đều là giá trị 0 thì tích = 0.
def tinh_tich(m):
    tich = 1
    while m != 0:
        tich *= m % 10
        m //= 10
    return tich
        
for _ in range(int(input())):
    n = input()
    tich = ''
    tong = ''
    for i in range (len(n)):
        if  i % 2 == 0:
            tong += n[i]
        else:
            tich += n[i]
    if tich.count('0') == len(tich):
        print(sum(map(int,tong)),0,sep = ' ')
    else:
        tich = tich.replace('0','')
        print(sum(map(int,tong)),tinh_tich(int(tich)),sep = ' ')

# cách 2:( tối ưu hơn)
# for t in range(int(input())):
#     a = list(int(i) for i in input())
#     su, mu = 0, 0
#     for i in range(len(a)):
#         if i % 2 == 0:
#             su += a[i]
#         else:
#             if a[i] != 0:
#                 if mu == 0:
#                     mu = a[i]
#                 else:
#                     mu *= a[i]
#     print(str(su) + " " + str(mu))