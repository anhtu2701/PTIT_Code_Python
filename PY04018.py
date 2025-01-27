def mon(s):
    if s[0] == "A": return "TOAN"
    if s[0] == "B": return "LY"
    return "HOA"

def ut(s):
    if s[1] == "1": return 2.0
    if s[1] == "2": return 1.5
    if s[1] == "3": return 1.0
    return 0.0

n = int(input())
lst = []
for i in range(1, n + 1):
    ten = f"GV{i:02} {input().title()}"
    ma = input()
    mon_hoc = mon(ma)
    diem_uu_tien = ut(ma)
    tin = float(input())
    chuyenmon = float(input())
    tong_diem = diem_uu_tien + tin*2+ chuyenmon
    tthai = "TRUNG TUYEN" if tong_diem >= 18 else "LOAI"
    lst.append((ten, mon_hoc, tong_diem, tthai))
lst.sort(key = lambda x: -x[2] )
for i in lst:
    print(f"{i[0]} {i[1]} {i[2]:.1f} {i[3]}")
