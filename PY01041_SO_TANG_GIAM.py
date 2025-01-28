# Một số nguyên dương được gọi là số tăng giảm nếu thỏa mãn các điều kiện:
# Có từ 3 chữ số trở lên
# Tìm ra một vị trí trong dãy chữ số sao cho từ bên trái đến vị trí đó thỏa mãn thứ tự tăng dần (tăng chặt) còn từ vị trí đó đến hết thì thỏa mãn thứ tự giảm dần (giảm chặt).
# Viết chương trình kiểm tra một số có phải số tăng giảm hay không.

def solve(s):
    if len(s) < 3:
        return "NO"
    arr = [int(i) for i in s]
    up = True
    for j in range(1,len(arr)):
        if up and arr[j] <= arr[j-1]:
            up = False
        elif not up and arr[j] >= arr[j-1]:
            return "NO"
    return "YES"

for _ in range(int(input())):
    s = input()
    print(solve(s))




