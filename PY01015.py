#Một số được gọi là số không giảm nếu không có cặp chữ số cạnh nhau (i, i+1) nào mà số thứ i lớn hơn số thứ i+1.Viết chương trình kiểm tra số nguyên dương có thỏa mãn là số không giảm hay không.

def kiem_tra_so_canh_nhau(n):
    chuoi = str(n)
    for i in range(len(chuoi)-1):
        if chuoi[i] > chuoi[i+1]: #không nên dùng chuoi[i] <= chuoi[i+1]: rồi return YES vì nếu code thế thì sẽ chưa kiểm tra được hết cả dãy mà đã in ra YES rồi
            return "NO" 
    return "YES"

test_case = int(input())
for _ in range(test_case):
    n = int(input())
    print(kiem_tra_so_canh_nhau(n))