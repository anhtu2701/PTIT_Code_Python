# Một cặp số nguyên dương (a,b) được gọi là nguyên tố cùng nhau nếu a và b có ước chung lớn nhất bằng 1. Một bộ ba số (a, b, c) được gọi là bộ ba nguyên tố cùng nhau nếu a < b < c và các cặp (a,b), (b,c), (a,c) đều nguyên tố cùng nhau.
# Cho hai số nguyên dương L và R (10 < L < R < 200). Hãy viết chương trình liệt kê các bộ ba số nguyên tố cùng nhau trong đoạn [L, R].

import math
a, b = map(int,input().split())
for i in range(a,b+1):
    for j in range(i+1,b+1):
        for k in range(j+1,b+1):
            if math.gcd(i,j) == 1 and math.gcd(i,k) == 1 and math.gcd(j,k) == 1:
                print('('+str(i) + ', ' + str(j) + ', ' + str(k)+')')
print()