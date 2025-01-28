#Một số được xem là số may mắn nếu chỉ có các chữ số 4 và 7. Cho số nguyên dương N không quá 200 chữ số. Hãy kiểm tra xem N có phải số may mắn hay không.

def test_so_dep(n):
    while n != 0:
        if n % 10 != 4 and n % 10 != 7:
            return "NO"
        n = n // 10
    return "YES"

tc = int(input())
for i in range(tc):
    n = int(input())
    print(test_so_dep(n))