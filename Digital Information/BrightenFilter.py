# Constants for the image
IMAGE_URL = "https://codehs.com/uploads/e07cd01271cac589cc9ef1bf012c6a0c"
IMAGE_WIDTH = 280
IMAGE_HEIGHT = 200
BRIGHTENING_FACTOR = 50
MAX_PIXEL_VALUE = 255

image = Image(IMAGE_URL)
image.set_position(70, 70)
image.set_size(IMAGE_WIDTH, IMAGE_HEIGHT)
add(image)


# Filter to brighten an image
def brighten_filter(pixel):
    new_red = brighten_color(pixel[0])
    new_green = brighten_color(pixel[1])
    new_blue = brighten_color(pixel[2])
    return (new_red, new_green, new_blue)

def brighten_color(color_value):
    #If the value is over 255, set it to 255
    return min(color_value + BRIGHTENING_FACTOR, MAX_PIXEL_VALUE)

def change_picture():
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            pixel = image.get_pixel(x,y)
            new_colors = brighten_filter(pixel)
            image.set_red(x, y, new_colors[0])
            image.set_green(x, y, new_colors[1])
            image.set_blue(x, y, new_colors[2])
            

# Give the image time to load
print("Making Brighter....")
print("Might take a minute....")
timer.set_timeout(change_picture, 1000)