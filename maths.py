import numpy as np, os
def multiplyPoints(points, matrix):
    output = matrix @ points
    slice = output[:, 3]
    output = output / np.stack([slice for i in range(4)], 1)
    return output
def quaternion2Matrix(q):
    return np.array([
        [2*(q[0]**2+q[1]**2)-1, 2*(q[1]*q[2]-q[0]*q[3]), 2*(q[1]*q[3]+q[0]*q[2]), 0],
        [2*(q[1]*q[2]+q[0]*q[3]), 2*(q[0]**2+q[2]**2)-1, 2*(q[2]*q[3]-q[0]*q[1]), 0],
        [2*(q[1]*q[3]-q[0]*q[2]), 2*(q[2]*q[3]+q[0]*q[1]), 2*(q[0]**2+q[3]**2)-1, 0],
        [0, 0, 0, 1]
    ])
def invertQuaternion(q):
    return np.array([q[0], -q[1], -q[2], -q[3]])
class model:
    def __init__(self, verts, tris):
        self.verts = verts
        self.tris = tris
    def load(path):
        verts = np.load(path + '/verts.npy', False)
        tris = np.load(path + '/tris.npy', False)
        return model(verts, tris)
    def save(self, path):
        os.mkdir(path)
        np.save(path + '/verts.npy', self.verts, False)
        np.save(path + '/tris.npy', self.tris, False)
    def unitCube():
        verts = np.stack([np.array([[1, 1, 1, 1], [1, 1, -1, 1], [1, -1, 1, 1], [1, -1, -1, 1], 
                    [-1, 1, 1, 1], [-1, 1, -1, 1], [-1, -1, 1, 1], [-1, -1, -1, 1]], np.float64)], -1)
        tris = np.array([[0, 1, 2], [1, 2, 3], [4, 5, 6], [5, 6, 7], [0, 1, 4], 
                    [1, 4, 5], [2, 3, 6], [3, 6, 7], [0, 2, 4], [2, 4, 6], [1, 3, 5], [3, 5, 7]], np.uint)#haven't done this yet
        return model(verts, tris)
class camera:
    def __init__(self, position, rotation, w, h, fov, nearClip, farClip):
        self.position = np.array(position)
        self.rotation = rotation
        self.w = w
        self.h = h
        self.aspectRatio = w/h
        self.fov = fov
        self.nearClip = nearClip
        self.farClip = farClip
    def projectionMatrix(self):
        a = 1/self.nearClip - 1/self.farClip
        b = 1/self.nearClip
        w = a/(2*np.tan(np.deg2rad(self.fov)))
        h = w/self.aspectRatio
        return np.array([
            [w, 0, a/2, 0],
            [0, h, a/2, 0],
            [0, 0, b, -1],
            [0, 0, a, 0]
        ])
    def transformMatrix(self):
        return quaternion2Matrix(invertQuaternion(self.rotation))@np.insert(np.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [0, 0, 0]
        ]), 3, self.position*[-1, -1, -1, 1], axis=1)
    def matrix(self):
        return self.projectionMatrix()@self.transformMatrix()