# Cho hai số a và b trong đó a≤1012, b≤10250. Nhiệm vụ của bạn là tìm ước số chung lớn nhất của hai số a, b.
#
# Input:
#
# Dòng đầu tiên đưa vào T là số lượng bộ test.
# T dòng tiếp đưa các bộ test. Mỗi bộ test gồm hai dòng: dòng đầu tiên đưa vào số a; dòng tiếp theo đưa vào số b.
# Các số T, a, b thỏa mãn ràng buộc: 1≤T≤100; 1≤a≤1012; 1≤b≤10250;
# Output:
#
# Đưa ra kết quả mỗi test theo từng dòng.

import math
for _ in range(int(input())):
    a = int(input())
    b = int(input())
    print(math.gcd(a,b))
