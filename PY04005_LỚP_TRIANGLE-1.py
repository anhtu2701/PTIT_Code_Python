from math import sqrt

def Decimal(x):
    return float(x) 

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.res = self.check()

    def check(self):
        if self.a + self.b <= self.c or self.c + self.b <= self.a or self.a + self.c <= self.b:
            return "INVALID"
        else:
            return f"{self.a + self.b + self.c:.3f}"
        
    def __str__(self):
        return f"{self.res}"
    
if __name__ == "__main__":
    for _ in range(int(input())):
        arr = [int(i) for i in input().split()]
        A = Point(Decimal(arr[0]), Decimal(arr[1]))
        B = Point(Decimal(arr[2]), Decimal(arr[3]))
        C = Point(Decimal(arr[4]), Decimal(arr[5]))
        c = A.distance(B)
        b = A.distance(C)
        a = B.distance(C)
        print(Triangle(a, b, c))