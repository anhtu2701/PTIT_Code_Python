# Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số. Xét các vị trí từ trái qua phải (tính từ 0). Hãy tính:
# Tích các chữ số ở vị trí chẵn – giá trị tích chữ số có thể đến 18 chữ số. Chú ý khi tính tích bỏ qua các chữ số 0.
# Tổng các chữ số ở vị trí lẻ
# Input
# Dòng đầu ghi số bộ test (không quá 20)
# Mỗi bộ test ghi trên một dòng số nguyên dương N (ít nhất 2 chữ số và không quá 500 chữ số)

for _ in range(int(input())):
    n = [int(i) for i in input()]
    sum, product = 0, 0
    for j in range(len(n)):
        if j % 2 == 1:
            sum += n[j]
        else:
            if n[j] != 0:
                if product == 0:
                    product = n[j]
                else:
                    product *= n[j]
    print(str(product), str(sum),sep = ' ')

    

    

