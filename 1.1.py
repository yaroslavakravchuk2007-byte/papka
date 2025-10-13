import math
from itertools import combinations

class Vector:
    def __init__(self, x, y=None, z=None):

        if isinstance(x, str):
            x = x.strip("{} ")
            parts = x.split(',')
            assert len(parts) == 3, "формат строки: {x, y, z}"
            self.x, self.y, self.z = map(float, parts)
        else:
            
            assert all(isinstance(i, (int, float)) for i in (x, y, z)), "x, y, z должны быть числами"
            self.x, self.y, self.z = x, y, z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, Vector):
            
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, (int, float)):
            
            return Vector(self.x * other, self.y * other, self.z * other)
        raise TypeError("пж умножьте  на число или другой вектор")
    def __abs__(self):
        
        return math.sqrt(self.x**2 + self.y**2 + self.z**2) # вот тут длина вектора (это для меня, чтобы не забыть)

    def __repr__(self):
        return f"{{{self.x}, {self.y}, {self.z}}}"
 #3.1
def center_of_mass(vectors):
    n = len(vectors)
    sx = sum(v.x for v in vectors)
    sy = sum(v.y for v in vectors)
    sz = sum(v.z for v in vectors)
    return Vector(sx / n, sy / n, sz / n)
#3.2
def triangle_area(a, b, c):
    ab = b - a
    ac = c - a
    cross_x = ab.y * ac.z - ab.z * ac.y
    cross_y = ab.z * ac.x - ab.x * ac.z
    cross_z = ab.x * ac.y - ab.y * ac.x
    area = 0.5 * math.sqrt(cross_x**2 + cross_y**2 + cross_z**2)
    return area

def largest_triangle(vectors):
    max_area = 0
    best_triangle = None
    for a, b, c in combinations(vectors, 3):
        area = triangle_area(a, b, c)
        if area > max_area:
            max_area = area
            best_triangle = (a, b, c)
    return best_triangle, max_area
