def cung_hoang_dao(d,m):
    if m == 1:
        if d < 20:
            return "Ma Ket"
        return "Bao Binh"
    elif m == 2:
        if d < 19:
            return "Bao Binh"
        return "Song Ngu"
    elif m == 3:
        if d < 21:
            return "Song Ngu"
        return "Bach Duong"
    elif m == 4:
        if d < 20:
            return "Bach Duong"
        return "Kim Nguu"
    elif m == 5:
        if d < 21:
            return "Kim Nguu"
        return "Song Tu"
    elif m == 6:
        if d < 21:
            return "Song Tu"
        return "Cu Giai"
    elif m == 7:
        if d < 23:
            return "Cu Giai"
        return "Su Tu"
    elif m == 8:
        if d < 23:
            return "Su Tu"
        return "Xu Nu"
    elif m == 9:
        if d < 23:
            return "Xu Nu"
        return "Thien Binh"
    elif m == 10:
        if d < 23:
            return "Thien Binh"
        return "Thien Yet"
    elif m == 11:
        if d < 23:
            return "Thien Yet"
        return "Nhan Ma"
    else:
        if d < 22:
            return "Nhan Ma"
        return "Ma Ket"

for _ in range(int(input())):
    d,m =  map(int,input().split())
    print(cung_hoang_dao(d,m))