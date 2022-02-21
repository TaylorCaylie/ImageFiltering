
# import the image
from PIL import Image, ImageDraw

# import the image
img = Image.open("sampleimages/lena30.jpg")
pix = img.load()

kernel = [[-1, -1, -1],
        [-1,8,-1],
        [-1,-1,-1]]

# obtain the size of images in pixels
width, height = img.size

offset = int(len(kernel) / 2)

# Create output image
output_image = Image.new("RGB", img.size)
draw = ImageDraw.Draw(output_image)

# iterate over each pixel starting in the middle of the kernel
# onwards to the end of the image minus offset
# and for each pixel get the sum of the neighboring pixels
# rbg values and multiply by the associated filter

for x in range(offset, img.width - offset):
    for y in range(offset, img.height - offset):
        values = [0,0,0]
        for kernelX in range(len(kernel)):
            for kernelY in range(len(kernel)):
                newPxl = pix[x+kernelX-offset, y+kernelY-offset]
                values[0] += newPxl[0] * (1/kernel[kernelX][kernelY])
                values[1] += newPxl[1] * (1/kernel[kernelX][kernelY])
                values[2] += newPxl[2] * (1/kernel[kernelX][kernelY])
        pix[x, y] = (int(values[0]), int(values[1]), int(values[2]))
        draw.point((x, y), (int(values[0]), int(values[1]), int(values[2])))
img.show()
# output_image.save("output.png")
# output_image.show()