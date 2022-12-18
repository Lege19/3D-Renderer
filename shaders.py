def vertPixel(model, pixels, colour):
    for i in model.verts:
        if 640 > i[0, 0] >= 0 and 480 > i[1, 0] >= 0:
            pixels[int(i[0, 0]) + int(i[1, 0]) * 640] = colour
