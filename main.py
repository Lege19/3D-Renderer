from sdl2 import *
import sdl2.ext
import sys
import ctypes
def testFail(value):#test if a function has failed and return an error message
    if value == None:
        raise Exception(SDL_GetErrorMsg())
def startUp():#initialise values
    global win, renderer, outputTexture
    SDL_Init(SDL_INIT_VIDEO)
    win = SDL_CreateWindow(b"3D-Renderer", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 640, 480, 0)
    testFail(win)
    renderer = SDL_CreateRenderer(win, -1, 0)
    testFail(renderer)
    outputTexture = SDL_CreateTexture(renderer, SDL_PIXELFORMAT_RGB888, SDL_TEXTUREACCESS_STREAMING, 640, 480)
    testFail(outputTexture)
def shutDown():#stops the program
    SDL_DestroyTexture(outputTexture)
    SDL_DestroyRenderer(renderer)
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
def updateWindow():#draw the outputTexure to the Window
    SDL_RenderCopy(renderer, outputTexture, None, None)
def main():
    startUp()
    updateWindow()
    SDL_Delay(5000)
    handleEvents()
    SDL_Delay(1000)
    shutDown()
if __name__ == "__main__":
    main()