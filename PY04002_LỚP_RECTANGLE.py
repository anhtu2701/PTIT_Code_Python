class Rectangle:
    def __init__(self, length, width, color):
        self.perimeter = (width + length) * 2
        self.area = length * width
        self.color = color.title()

if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), int(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))

# SAI ĐỀ
