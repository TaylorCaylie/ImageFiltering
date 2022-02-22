
# import the image
from PIL import Image, ImageDraw
import math

# import the image
img = Image.open("sampleimages/lena30.jpg")
pix = img.load()


kernelx = [[-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]]

kernely = [[-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]]

# obtain the size of images in pixels
width, height = img.size

offset = int(len(kernelx) / 2)

# iterate over each pixel starting in the middle of the kernel
# onwards to the end of the image minus offset
# and for each pixel get the sum of the neighboring pixels
# rbg values and multiply by the associated filter
for x in range(offset, img.width - offset):
    for y in range(offset, img.height - offset):
        valuesX = [0,0,0]
        valuesY = [0,0,0]
        for kernelX in range(len(kernelx)):
            for kernelY in range(len(kernelx)):
                newPxl = pix[x+kernelX-offset, y+kernelY-offset]
                valuesX[0] += newPxl[0] * kernelx[kernelX][kernelY]
                valuesX[1] += newPxl[1] * kernelx[kernelX][kernelY]
                valuesX[2] += newPxl[2] * kernelx[kernelX][kernelY]
                valuesY[0] += newPxl[0] * kernely[kernelX][kernelY]
                valuesY[1] += newPxl[1] * kernely[kernelX][kernelY]
                valuesY[2] += newPxl[2] * kernely[kernelX][kernelY]
        pix[x, y] = (int(math.sqrt(valuesX[0]**2 + valuesY[0]**2)), int(math.sqrt(valuesX[1]**2 + valuesY[1]**2)), int(math.sqrt(valuesX[1]**2 + valuesY[1]**2)))
img.show()
img.save("outputImages/cannyedge.jpg")