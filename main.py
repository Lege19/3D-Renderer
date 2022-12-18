from sdl2 import *
import sys, ctypes, maths, shaders, numpy as np
def testFail(value):#test if a function has failed and return an error message
    if value == None:
        raise Exception(SDL_GetErrorMsg())
def startUp():#initialise values
    global win, outputSurface, pixels, w, h
    w = 640
    h = 480
    SDL_Init(SDL_INIT_VIDEO)
    win = SDL_CreateWindow(b"3D-Renderer", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, w, h, 0)
    testFail(win)
    outputSurface = SDL_GetWindowSurface(win)
    testFail(outputSurface)
    pixels = ctypes.cast(outputSurface[0].pixels, ctypes.POINTER(ctypes.c_uint32))
    #pixels is an array of 32-bit unsigned integers
    #colours can be set as 0xrrggbbaa
    #in standard rgba hexadecimal
def shutDown():#stops the program
    SDL_FreeSurface(outputSurface)
    SDL_Quit()
    sys.exit()
def handleEvents():#handle any events that need handling
    currentEvent = SDL_Event()
    while SDL_PollEvent(ctypes.byref(currentEvent)) != 0:
        if currentEvent.type == SDL_QUIT:
            print("closed")
            shutDown()
def main():
    cube = maths.model.unitCube()
    camera = maths.camera([0, 0, -5, 1], [1, 0, 0, 0], w, h, 30, 0.5, 7)
    t = 0
    while True:
        SDL_FillRect(outputSurface, None, 0)
        if t > 50:
            cube.verts = maths.multiplyPoints(cube.verts, 
                np.array([[0.9962, -0.0872, 0, 0],
                [0.0872, 0.9962, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]]) 
                @
                np.array([[0.9962, 0, -0.0872, 0],
                [0, 1, 0, 0],
                [0.0872, 0, 0.9962, 0],
                [0, 0, 0, 1]]))
        clipVerts = maths.multiplyPoints(cube.verts, camera.transformMatrix())
        clipVerts = maths.multiplyPoints(clipVerts, camera.projectionMatrix())
        print(clipVerts)
        clipVerts = clipVerts * [[h], [w], [1], [1]]
        shaders.vertPixel(maths.model(clipVerts, cube.tris), pixels, 0xffffff)
        SDL_UpdateWindowSurface(win, outputSurface)
        handleEvents()
        SDL_Delay(60)
        t+=1
if __name__ == "__main__":
    startUp()
    main()