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

class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.x**2)
    def normalized(self):
        magnitude = self.magnitude()
        return Vector3(self.x / magnitude, self.y / magnitude, self.z / magnitude)
    def normalize(self):
        magnitude = self.magnitude()
        self.x = self.x / magnitude
        self.y = self.y / magnitude
        self.z = self.z / magnitude
    def add(a, b):
        return Vector3(a.x+b.x, a.y+b.y, a.z+b.z)
    def subtract(a, b):
        return Vector3(a.x-b.x, a.y-b.y, a.z-b.z)
    def dot(a, b):
        return a.x*b.x + a.y*b.y + a.z*b.z
    def cross(a, b):
        return Vector3(a.y*b.z - a.z*b.y, a.z*b.x - a.x*b.z, a.x*b.y - a.y*b.x)
    def scale(self, scalar):
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)
class TMatrix33:
    def __init__(self, xx, xy, xt, yx, yy, yt, tx, ty, tt):
        self.xx = xx
        self.xy = xy
        self.xt = xt
        self.yx = yx
        self.yy = yy
        self.yt = yt
        self.tx = tx
        self.ty = ty
        self.tt = tt
class TMatrix44:
    def __init__(self, xx, xy, xz, xt, yx, yy, yz, yt, zx, zy, zz, zt, tx, ty, tz, tt):
        self.xx = xx
        self.xy = xy
        self.xz = xz
        self.xt = xt
        self.yx = yx
        self.yy = yy
        self.yz = yz
        self.yt = yt
        self.zx = zx
        self.zy = zy
        self.zz = zz
        self.zt = zt
        self.tx = tx
        self.ty = ty
        self.tz = tz
        self.tt = tt
class quaternion:
    def __init__(self, w, i, j, k):
        self.w = w
        self.i = i
        self.j = j
        self.k = k
    def axisAngle(axis, angle):
        angle = angle/2
        sinAngle = math.sin(angle)
        return quaternion(math.cos(angle), sinAngle * axis.x, sinAngle * axis.y, sinAngle * axis.z)
    def _applyFirstHalf(self, vector):
        i = self.w*vector.x + self.j*vector.z - self.k*vector.y
        j = self.w*vector.y + self.k*vector.x - self.i*vector.z
        k = self.w*vector.z + self.i*vector.y - self.j*vector.x
        return Vector3(i, j, k)
#    def _applySecondHalf(self, vector):#with some rearanging its the same as first half
#        i = vector.x*self.w - vector.y*self.k + vector.z*self.j
#        j = vector.y*self.w - vector.z*self.i + vector.x*self.k
#        k = vector.z*self.w - vector.x*self.j + vector.y*self.i
    def apply(self, vector):
        return self._applyFirstHalf(self._applyFirstHalf(vector))
    def combine(q1, q2):
        w = q1.w*q2.w - q1.i*q2.i - q1.j*q2.j - q1.k*q2.k
        i = q1.w*q2.i + q1.i*q2.w + q1.j*q2.k - q1.k*q2.j
        j = q1.w*q2.j + q1.j*q2.w + q1.k*q2.i - q1.i*q2.k
        k = q1.w*q2.k + q1.k*q2.w + q1.i*q2.j - q1.j*q2.i
        return quaternion(w, i, j, k)