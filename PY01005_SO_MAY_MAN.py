#Chữ số 4 và chữ số 7được xem là các chữ số may mắn.
#Cho số nguyên dương N có không quá 18 chữ số. Hãy đếm xem số chữ số 4 cộng với số chữ số 7 trong N có phải bằng 4 hay bằng 7 hay không.

def dem_chu_so_4_va_7():
    count_4 = 0
    count_7 = 0
    N = int(input())
    while N != 0:
        if N % 10 == 4:
            count_4 += 1
        if N % 10 == 7:
            count_7 += 1
        N //= 10
    if count_4 + count_7 == 4:
        print("YES")
    elif count_4 + count_7 == 7:
        print("YES")
    else:
        print("NO")

dem_chu_so_4_va_7()