from math import gcd

class PhanSo:
    def __init__(self, tu, mau):
        self.ucln = gcd(tu, mau)
        self.tu = tu // self.ucln
        self.mau = mau // self.ucln

    def __str__(self):
        return f"{self.tu}/{self.mau}"
    
if __name__ == "__main__":
    tu, mau = map(int, input().split())
    phanso = PhanSo(tu, mau)
    print(phanso)
