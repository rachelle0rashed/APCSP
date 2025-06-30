# Constants for the image
IMAGE_URL = "https://codehs.com/uploads/e07cd01271cac589cc9ef1bf012c6a0c"
IMAGE_WIDTH = 280
IMAGE_HEIGHT = 200
DARKENING_FACTOR = 50
MIN_PIXEL_VALUE = 0
image = Image(IMAGE_URL)
image.set_position(70, 70)
image.set_size(IMAGE_WIDTH, IMAGE_HEIGHT)
add(image)

# This function should take a pixel and return a tuple
# with the new color
def darken_filter(pixel):
    new_red = pixel[0] - DARKENING_FACTOR
    new_green = pixel[1] - DARKING_FACTOR
    new_blue = pixel[2] - DARKING_FACTOR
    return (new_red, new_green, new_blue)

# This function should loop through each pixel on the
# left hand side and call the darken filter to calculate 
# the new color then update the color.
def change_picture():
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            pixel = image.get_pixel
            new_color = darken_filter
            image.set_red(x, y, new_color[0])
            image.set_green(x ,y, new_color[1])
            image.set_blue(x, y, new_color[2])
            

# Give the image time to load
print("Making Darker....")
print("Might take a minute....")
timer.set_timeout(change_picture, 1000)