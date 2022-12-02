import numpy as np, os, ctypes
from sdl2 import *

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
class scene:
    pass
class camera:
    def __init__(self, fov, nearClip, farClip, w, h):
        self.w = w
        self.h = h
        self.SetAspectRatio()
        self.fov = fov
        self.nearClip = nearClip
        self.farClip = farClip
        self.outputSurface = SDL_CreateRGBSurface(0, w, h, 32, 0, 0, 0, 0)
        self.output = ctypes.cast(self.outputSurface[0].pixels, ctypes.POINTRE(ctypes.c_uint32))
        self.matrix = self.GetMatrix()
    def SetResolution(self, w, h):
        self.w = w
        self.h = h
        self.SetAspectRatio()
    def SetAspectRatio(self):
        self.aspectRatio = self.w/self.h
    def GetMatrix(self):
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