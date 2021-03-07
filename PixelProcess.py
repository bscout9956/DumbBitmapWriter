# PixelProcesser for BitmapWriter
import re

def processFile(reverse):
    listy = list()

    with open("pixels.csv", "r") as pfile:
        # Weird sorcery that I cannot understand anymore
        for single_line in pfile:
            listy2 = re.findall(r'(\d+)', single_line)
            listy2.reverse()
            listy += listy2

    for x in range(0, len(listy)):
        listy[x] = int(listy[x]) # No idea, there's probably a more efficient way of doing this
        listy[x] = listy[x].to_bytes(1, byteorder="little", signed=False) # Each?

    print(len(listy))
    if reverse == True:
        listy.reverse() # You may want to reverse the list for some reason?

    return listy
