# Bitmap Creator (out of bytes) - MAIN FILE
import os
import re
import PixelProcess
import ImageExtract

# Grabs Width and Height from Original Image and Extracts Pixels

img_dimensions = ImageExtract.ImageExtract()

# Image Parameters
img_width_int, img_height_int = (img_dimensions[0], img_dimensions[1]) # Tuple unpacking is fun
plane_count_int = 1 # Airbus?
bpp_int = 24
bytespp = bpp_int // 8
image_size_int = img_width_int * img_height_int * bytespp
image_dimensions = img_width_int * img_height_int

# PixelArray -- BEGIN

# First argument reverses the orientation of each line, fixes mirrored images
pixels = PixelProcess.processFile(True)

# PixelArray -- END

# DIB Header -- BEGIN -- Has to come after the PixelArray Data

# DIB Header Size
dib_header_size_int = 36 + 4 # 36 bytes of information + the size information itself
dib_header_size = dib_header_size_int.to_bytes(4, byteorder="little", signed=False)

# Image Width and Height Byte Data
img_width = img_width_int.to_bytes(4, byteorder="little", signed=False)
img_height = img_height_int.to_bytes(4, byteorder="little", signed=False)

# Planes Data
plane_count = plane_count_int.to_bytes(2, byteorder="little", signed=False)

# Bits per Pixel Data
bpp = bpp_int.to_bytes(2, byteorder="little", signed=False)

# Compression (Not compressed at any time, but still...)
compression = bytes(4)

# Image Size (Relates to the PixelArray)
print("Image Size is %d" % image_size_int + " bytes")
image_size = image_size_int.to_bytes(4, byteorder="little", signed=False)

# Trailing Crap
trailing_crap = bytes(16)

# DIB Header List
dib_header = [dib_header_size, img_width, img_height,
plane_count, bpp, compression,
image_size, trailing_crap]

# DIB Header -- END

# Bitmap File Header -- BEGIN

# ----------------------------------

"""
bfh_size description:

BMP Signature +
2 sets of 2 bytes of reserved data +
4 bytes for the file_offset value in the header +
4 bytes for the file_size value in the header
"""

bfh_size = 2 + 2 + 2 + 4 + 4

# ----------------------------------

bmp_signature = b'\x42\x4D'
file_size = image_size_int + dib_header_size_int + bfh_size
file_size = file_size.to_bytes(4, byteorder="little", signed=False)

# 2 Areas of Reserved Bytes
reserve1 = bytes(2)
reserve2 = bytes(2)

# Offset to PixelArray, bytes until pixel array starts
# Probably unsigned int
file_offset = 54
file_offset = file_offset.to_bytes(4, byteorder="little", signed=False)

# Bitmap File Header List
bitmap_file_header = [bmp_signature, file_size, reserve1, reserve2, file_offset]

# Bitmap File Header -- END

# Write all the header information

with open("result.bmp", "wb") as bitmap_file:
    for header_element in bitmap_file_header:
        bitmap_file.write(header_element)
    for header_element in dib_header:
        bitmap_file.write(header_element)
    # Write the PixelArray
    for px in pixels:
        bitmap_file.write(px)

#os.remove("pixels.csv")

print("Done")
