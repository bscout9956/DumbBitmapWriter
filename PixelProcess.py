# PixelProcesser for BitmapWriter
import re

def processFile(reverse):
    listy = []

    with open("pixels.csv", "r") as pfile:
        for single_line in pfile:
            listy2 = re.findall(r'(\d+)', single_line)
            listy2.reverse()
            listy += listy2

    for x in range(0, len(listy)):
        listy[x] = int(listy[x])
        listy[x] = listy[x].to_bytes(1, byteorder="little", signed=False)

    print(len(listy))
    if reverse == True:
        listy.reverse() # You may want to reverse the list for some reason?

    return listy
