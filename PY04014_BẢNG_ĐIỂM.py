def change(avg):
    if avg >= 9: return "XUAT SAC"
    elif avg >= 8: return "GIOI"
    elif avg >= 7: return "KHA"
    elif avg >= 5: return "TB"
    else: return "YEU"

n = int(input())
arr = []
for _ in range(1,n+1):
    ma = f"HS{_:02}"
    ten = input().title()
    score = [float(i) for i in input().split()]
    sum = (score[0]*2 + score[1]*2 + score[2] + score[3] + score[4] + score[5] + score[6] + score[7] + score[8] + score[9])/12
    avg = round(sum + 1e-9, 1)
    thanh_tich = change(avg)
    arr.append((ma, ten, avg, thanh_tich))
arr.sort(key=lambda x: ((-x[2], x[0])))
for i in arr:
    print(*i)
