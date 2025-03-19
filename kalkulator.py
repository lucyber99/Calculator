import math as matematika
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type for +")
    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("Unsupported operand type for -")
    def __mul__(self, other):
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        else:
            raise TypeError("Unsupported operand type for *")
    def __truediv__(self, other):
        if isinstance(other, Point):
            return Point(self.x / other.x, self.y / other.y)
        else:
            raise TypeError("Unsupported operand type for /")
    def __pow__(self, other):
        if isinstance(other, Point):
            return Point(self.x ** other.x, self.y ** other.y)
        else:
            raise TypeError("Unsupported operand type for **")
    def __log__(self, other):
        if isinstance(other, Point):
            return Point(matematika.log(self.x,other.x), matematika.log(self.y,other.y))
        else:
            raise TypeError("Unsupported operand type for +")

    def __str__(self):
        return f"Point({self.x}, {self.y})"

point1 = Point(9, 3)
point2 = Point(3, 4)
point3 = point2 * point1
point4 = point3 - point2
point5 = point4  (point2 * point3)
print(point3)  # Output: Point(5, 7)
print(point4)  # Output: Point(5, 7)
print(point5)  # Output: Point(5, 7)