# Cho dãy số A[] có n phần tử là các số nguyên dương khác nhau, giá trị không quá 100. Hãy liệt kê các cặp số nguyên tố cùng nhau xuất hiện trong dãy theo thứ tự tăng dần, mỗi cặp số in trên một dòng.
# Một cặp số được gọi là nguyên tố cùng nhau nếu ước chung lớn nhất của chúng bằng 1.
import math
n = int(input())
A = [int(i) for i in input().split()]
A.sort()
for j in range(len(A) - 1):
    for k in range(j+1,len(A)):
        if math.gcd(A[j],A[k]) == 1:
            print(A[j],A[k])

