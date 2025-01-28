#Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.Hãy tính tích các chữ số của N. Chú ý bỏ qua các chữ số 0 nếu có. 
#Input
#Dòng đầu ghi số bộ test (không quá 20).Mỗi test ghi số N (không quá 500 chữ số).
#Output
#Với mỗi bộ test, ghi ra kết quả tính được.Dữ liệu vào đảm bảo kết quả tích các chữ số sẽ không vượt quá 18 chữ số.  

tc = int(input())
for i in range(tc):
    n = int(input())
    #Dùng câu lệnh "replace" này để xóa chữ số 0 trong 1 số
    chuoi_xoa_0 = str(n).replace('0','')
    n = int(chuoi_xoa_0)
    res = 1
    while n != 0:
        res *= n % 10
        n //= 10
    print(res)
    
