def kiem_tra_so_dep(num):
    # Kiểm tra các chữ số ở vị trí cách nhau 2 có giống nhau không
    for i in range(len(num) - 2):
        if num[i] != num[i + 2]:
            return False
    return True

def main():
    tc = int(input())  
    for _ in range(tc):
        num = input().strip()  # Đọc vào số nguyên dưới dạng chuỗi
        if kiem_tra_so_dep(num):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
