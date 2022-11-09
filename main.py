from sdl2 import *
import sys
import ctypes
def testFail(value):#test if a function has failed and return an error message
    if value == None:
        raise Exception(SDL_GetErrorMsg())
def startUp():#initialise values
    global win, outputSurface
    SDL_Init(SDL_INIT_VIDEO)
    win = SDL_CreateWindow(b"3D-Renderer", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 640, 480, 0)
    testFail(win)
    outputSurface = SDL_GetWindowSurface(win)
    testFail(outputSurface)
def shutDown():#stops the program
    SDL_FreeSurface(outputSurface)
    SDL_Quit()
    sys.exit()
def handleEvents():#handle any events that need handling
    currentEvent = SDL_Event()
    try:#try except used to prevent compiler from raising error with NoneType.type
        while SDL_PollEvent(ctypes.byref(currentEvent)) != 0:
            if currentEvent.type == SDL_QUIT:
                print("closed")
                shutDown()
    except:
        pass
def main():
    startUp()
    SDL_Delay(1000)
    shutDown()
if __name__ == "__main__":
    main()