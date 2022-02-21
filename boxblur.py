# 1/49	1/49	1/49	1/49	1/49	1/49	1/49
# 1/49	1/49	1/49	1/49	1/49	1/49	1/49
# 1/49	1/49	1/49	1/49	1/49	1/49	1/49
# 1/49	1/49	1/49	1/49	1/49	1/49	1/49
# 1/49	1/49	1/49	1/49	1/49	1/49	1/49
# 1/49	1/49	1/49	1/49	1/49	1/49	1/49
# 1/49	1/49	1/49	1/49	1/49	1/49	1/49


# a 7 x 7 window is centered upon each pixel
# all pixels within the window are summed up and divided by 49
# then the centered pixel is set to that value
from PIL import Image

# import the image
img = Image.open("sampleimages/lena30.jpg")
pix = img.load()

# obtain the size of images in pixels
width, height = img.size

offset = int(7 / 2)

# iterate over each pixel starting in the middle of the kernel
# onwards to the end of the image minus offset
# and for each pixel get the sum of the neighboring pixels
# rbg values and multiply by 1/49
for y in range(offset, height - offset):
    for x in range(offset, width - offset):
        values = [0,0,0]
        for kernelX in range(6):
            for kernelY in range(6):
                newPxl = pix[x+kernelX-offset, y+kernelY-offset]
                values[0] += newPxl[0] * (1/49)
                values[1] += newPxl[1] * (1/49)
                values[2] += newPxl[2] * (1/49)
    pix[x, y] = (int(values[0]), int(values[1]), int(values[2]))

img.show()
# img.save("boxBlurOutput", format="jpg")
