import math
class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def magnitude(self):#magnitude of vector
        return math.sqrt(self.x ** 2 + self.y ** 2)
    def normalized(self):#return a normalized vector
        magnitude = self.magnitude()
        return Vector2(self.x / magnitude, self.y / magnitude)
    def normalize(self):#normalize the vector itself
        magnitude = self.magnitude()
        self.x = self.x/magnitude
        self.y = self.y/magnitude
    def add(a, b):#add two vectors
        return Vector2(a.x + b.x, a.y + b.y)
    def subtract(a, b):#subtract vectors
        return Vector2(a.x - b.x, a.y - b.y)
    def dot(a, b):#dot product
        return a.x*b.x + a.y*b.y
    def scale(self, scalar):#multiply by a scalar
        return Vector2(self.x * scalar, self.y * scalar)
