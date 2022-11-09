class vert:
    def __init__(self, position, normal = None):
        self.position = position
        self.normal = normal
class tri:
    def __init__(self, p1, p2, p3, normal = None):#points should be passed as indexes of vert list
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
class model:
    def __init__(self, verts, tris):
        self.verts = verts
        self.tris = tris
class simpleCamera:
    def __init__(self, position, angle, nearClip, farClip, fov):
        self.position = position
        self.angle = angle
        self.nearClip = nearClip
        self.farClip = farClip
        self.fov = fov