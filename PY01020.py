# Một số kết thúc bởi hai chữ số 86 được gọi là số phát lộc. Cho một số nguyên dương không quá 500 chữ số, hãy kiểm tra số đó có phải số phát lộc hay không.
for i in range(int(input())):
    n = int(input())
    if n % 100 == 86:
        print("YES")
    else:
        print("NO")
