def rgb(r, g, b):
    if r < 0:
        r = 0
    elif r > 255:
        r = 255

    if g < 0:
        g = 0
    elif g > 255:
        g = 255

    if b < 0:
        b = 0
    elif b > 255:
        b = 255

    answer = '%02x%02x%02x' % (r, g, b)
    print(answer.upper())


rgb(0,0,0)
rgb(1,2,3)
rgb(255,255,255)
rgb(254,253,252)
rgb(-20,275,125)
