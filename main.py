import sdl2
import sdl2.ext
win = sdl2.SDL_CreateWindow(b"3D-Renderer", sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED, 640, 480, 0)
if win == None:
    raise Exception(sdl2.SDL_GetError())
renderer = sdl2.SDL_CreateRenderer(win, -1, 0)
if renderer == None:
    raise Exception(sdl2.SLD_GetError())
outputTexture = sdl2.SDL_CreateTexture(renderer, sdl2.SDL_PIXELFORMAT_RGB888, sdl2.SDL_TEXTUREACCESS_STREAMING, 640, 480)
if outputTexture == None:
    raise Exception(sdl2.SDL_GetError())
sdl2.SDL_RenderCopy(renderer, outputTexture, None, None)
sdl2.SDL_Delay(10000)