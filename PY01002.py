phuongtrinh = input().replace(" ", "")
tach2ve = phuongtrinh.split('=')
if eval(tach2ve[0]) == int(tach2ve[1]):
    print("YES")
else:
    print("NO")
