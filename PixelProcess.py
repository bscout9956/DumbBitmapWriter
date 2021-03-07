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

    """
    for x in range(0, len(listy)):
        listy[x] = int(listy[x]) # No idea, there's probably a more efficient way of doing this
        listy[x] = listy[x].to_bytes(1, byteorder="little", signed=False) # Each?

    """

    # List comprehension
    listy = [int(l_element) for l_element in listy]
    listy = [l_element.to_bytes(1, byteorder="little", signed=False) for l_element in listy]
    

    #print(len(listy))
    if reverse == True:
        listy.reverse() # You need to reverse the list

    return listy
