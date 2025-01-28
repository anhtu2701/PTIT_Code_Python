# Cho dãy số A[] chỉ có các giá trị nhị phân 0 và 1.
# Hãy đếm xem có bao nhiêu cặp số khác nhau đứng cạnh nhau trong dãy.
 
n= int(input())
n = [int(i) for i in input().split()]
cnt = 0
for i in range(len(n)-1):
    if  n[i] != n[i+1]:
        cnt += 1
print(cnt)
