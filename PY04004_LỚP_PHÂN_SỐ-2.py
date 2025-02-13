from math import gcd

class PhanSo:
    def __init__(self, tu, mau):
        self.ucln = gcd(tu, mau)
        self.tu = tu // self.ucln
        self.mau = mau // self.ucln

    def __str__(self):
        return f"{self.tu}/{self.mau}"
    
if __name__ == "__main__":
    p1, p2, q1, q2 = map(int, input().split())
    tu = p1 * q2 + q1 * p2
    mau = p2 * q2
    phanso = PhanSo(tu, mau)
    print(phanso)
