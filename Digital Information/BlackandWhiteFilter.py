set_size(480, 400)
# Constants for the image
IMAGE_URL = "https://codehs.com/uploads/e07cd01271cac589cc9ef1bf012c6a0c"
IMAGE_WIDTH = 280
IMAGE_HEIGHT = 200
image = Image(IMAGE_URL)
image.set_position(70, 70)
image.set_size(IMAGE_WIDTH, IMAGE_HEIGHT)
add(image)
    

#######################################################
# Filter that takes an image as a parameter
# and applies a black and white filter to the image.
# For every pixel,
# compute the average of the R, G, and B values
# set the R, G, and B values of this pixel all to the computed average.
#######################################################
def black_and_white(pixel):
    new_color = (pixel[0] + pixel[1] + pixel[2]) // 3
    return new_color

def change_picture():
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            pixel = image.get_pixel(x,y)
            new_color = black_and_white(pixel)
            image.set_red(x, y, new_color)
            image.set_green(x, y, new_color)
            image.set_blue(x, y, new_color)
            

# Give the image time to load
print("Making Grayscale....")
print("It might take a minute....")
timer.set_timeout(change_picture, 1000)