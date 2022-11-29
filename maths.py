import numpy as np, os

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
        verts = np.array([[1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1], 
                    [-1, 1, 1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1]], np.float64)
        tris = np.array([], np.uint)#haven't done this yet
        return model(verts, tris)