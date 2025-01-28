# Cho một ký tự S[] chỉ có các chữ số, độ dài không quá 1000, và số nguyên dương N (không quá 9 chữ số). Hãy đếm xem số N xuất hiện bao nhiêu lần trong S[].
# Chú ý: các ký tự số không được đếm lặp. Tức là mỗi ký tự chỉ được xét một lần.
# Ví dụ: S[] = “1212121112211221121”, N = 121 thì đáp án là 3. 

for _ in range(int(input())):
    s = input()
    n = input()
    l,id,count = len(n),s.find(n),0
    while id != -1:
        count += 1
        id = s.find(n,id + l)
    print(count)
    