from PIL import Image

def ImageExtract():
    filename = input("Please type in the image filename\n")

    try:
        img = Image.open(filename)
    except FileNotFoundError:
        print("It was not possible to read/find the file, please try again.")

    pixels = img.load()
    print(img.size)

    pixels_list = list()
    separated_rgb = list()

    for y in range(0, img.size[1]):
        for x in range(0, img.size[0]): # Bad performance maybe?
            tmp = list(pixels[x, y])
            separated_rgb = [tmp[2], ";", tmp[1], ";", tmp[0], ";"]
            pixels_list += separated_rgb
        pixels_list.append("\n")


    """
    for x in range(0, len(pixels_list)):
        pixels_list[x] = str(pixels_list[x])
    """

    # List comprehension magic, avoid the above
    pixels_list = [str(pixel) for pixel in pixels_list]

    print("Saving to file...")

    with open("pixels.csv", "w+") as f:
        f.writelines(pixels_list)

    return img.size
