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
class Vector4:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2 + self.w**2)
    def normalised(self):
        magnitude = self.magnitude()
        return Vector4(self.x/magnitude, self.y/magnitude, self.z/magnitude)
    def normalise(self):
        magnitude = self.magnitude
        self.x = self.x/magnitude
        self.y = self.y/magnitude
        self.z = self.z/magnitude
        self.w = self.w/magnitude
    def add(a, b):
        return Vector4(a.x+b.x, a.y+b.y, a.z+b.z, a.w+b.w)
    def subtract(a, b):
        return Vector4(a.x-b.x, a.y-b.y, a.z-b.z, a.w-b.w)
    def dot(a, b):
        return a.x*b.x + a.y*b.y + a.z*b.z + a.w*b.w
    def scale(self, scalar):
        return Vector4(self.x*scalar, self.y*scalar, self.z*scalar, self.w*scalar)
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
class Quaternion:
    def __init__(self, r, i, j, k):
        self.r = r
        self.i = i
        self.j = j
        self.k = k
    def axisAngle(axis, angle):
        angle = angle/2
        sinAngle = math.sin(angle)
        return Quaternion(math.cos(angle), sinAngle * axis.x, sinAngle * axis.y, sinAngle * axis.z)
    def complement(self):#only works for normalised quaternions
        return Quaternion(self.r, -self.i, -self.j, -self.k)
    def fromVector(vector):
        return Quaternion(0, vector.x, vector.y, vector.z)
    def toVector(self):
        return Vector3(self.i, self.j, self.k)
    def apply(self, vector):
        qVector = Quaternion.fromVector(vector)
        temp = Quaternion.multiply(self, qVector)
        return Quaternion.multiply(temp, self.complement()).toVector()
    def multiply(q1, q2):
        r = q1.r*q2.r - q1.i*q2.i - q1.j*q2.j - q1.k*q2.k
        i = q1.r*q2.i + q1.i*q2.r + q1.j*q2.k - q1.k*q2.j
        j = q1.r*q2.j + q1.j*q2.r + q1.k*q2.i - q1.i*q2.k
        k = q1.r*q2.k + q1.k*q2.r + q1.i*q2.j - q1.j*q2.i
        return Quaternion(r, i, j, k)