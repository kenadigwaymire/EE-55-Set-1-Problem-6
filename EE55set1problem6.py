from PIL import Image
import numpy as np

SMALL_PIXEL_VAL = 127
LARGE_PIXEL_VAL = 128
SMALL_QUANT_VAL = 0
LARGE_QUANT_VAL = 255
VARIANCE = [0.5, 5, 50]

def loadImage(image_name: str):
    image = Image.open(image_name)
    pixels = np.asarray(image)
    return pixels

def quantizeImage(image_name: str):
    pixels = loadImage(image_name)
    new_image = []
    for i in range(len(pixels)):
        new_image.append([])
        for j in range(len(pixels[i])):
            new_image[i].append(valCheck(pixels[i][j]))
    new_arr = np.array(new_image)
    new_img = Image.fromarray(new_arr)
    new_image_name = "quantized_boat"
    new_img.save(new_image_name, format="tiff")
    new_img.show()

def valCheck(val: int):
    if val < SMALL_PIXEL_VAL:
        val = SMALL_QUANT_VAL
    elif val > LARGE_PIXEL_VAL:
        val = LARGE_QUANT_VAL
    return val

def randomizeImage(image_name: str):
    pixels = loadImage(image_name)
    for x in VARIANCE:
        new_image = []
        for i in range(len(pixels)):
            new_image.append([])
            for j in range(len(pixels[i])):
                new_image[i].append(pixels[i][j]+ np.random.normal(0, x))
        for x in range(len(new_image)):
            for y in new_image[x]:
                y = valCheck(y)
        new_arr = np.array(new_image)
        img = Image.fromarray(new_arr)
        img_name = "quantized_randomized_boat" + str(x)
        img.save(img_name, format="tiff")
        img.show()


quantizeImage("boat.tiff")
randomizeImage("boat.tiff")






