from shapely.geometry import Polygon
from shapely.ops import unary_union

def calculate_total_area(triangles):
    # Tạo các tam giác dưới dạng Polygon
    polygons = [Polygon(triangle) for triangle in triangles if Polygon(triangle).is_valid]
    
    # Hợp nhất tất cả tam giác (loại bỏ phần chồng lấn)
    union_polygon = unary_union(polygons)
    
    # Tính diện tích vùng che phủ
    return union_polygon.area

def main():
    # Nhập số lượng tam giác
    n = int(input("Nhập số tam giác: "))
    triangles = []
    
    # Đọc từng tam giác
    for _ in range(n):
        x1, y1, x2, y2, x3, y3 = map(int, input().split())
        triangles.append([(x1, y1), (x2, y2), (x3, y3)])
    
    # Tính diện tích
    total_area = calculate_total_area(triangles)
    
    # In kết quả với độ chính xác 6 chữ số
    print(f"{total_area:.6f}")

if __name__ == "__main__":
    main()
