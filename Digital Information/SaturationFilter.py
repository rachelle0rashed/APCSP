# Constants for the image
IMAGE_URL = "https://codehs.com/uploads/e07cd01271cac589cc9ef1bf012c6a0c"
IMAGE_WIDTH = 280
IMAGE_HEIGHT = 200
MAX_COLOR_VALUE = 255
MIN_COLOR_VALUE = 0
COLOR_THRESHOLD = 128

image = Image(IMAGE_URL)
image.set_position(70, 70)
image.set_size(IMAGE_WIDTH, IMAGE_HEIGHT)
add(image)


def saturate_filter(pixel):
    new_red = saturate_color(pixel[0])
    new_green = saturate_color(pixel[1])
    new_blue = saturate_color(pixel[2])
    return (new_red, new_green, new_blue)

####################################################################
# Given a color value, returns the saturated version of that
# color value.
# If the value is in the upper half of the color range (128 - 255),
# returns the max value of 255.
# If the value is in the lower half of the color range (0 - 127),
# returns the min value of 0.
####################################################################
def saturate_color(color_value):
    if color_value >= COLOR_THRESHOLD:
        return MAX_COLOR_VALUE
    else:
        return MIN_COLOR_VALUE


def change_picture():
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            pixel = image.get_pixel(x,y)
            new_colors = saturate_filter(pixel)
            image.set_red(x, y, new_colors[0])
            image.set_green(x, y, new_colors[1])
            image.set_blue(x, y, new_colors[2])
            

# Give the image time to load
print("Saturating Image ....")
print("Might take a minute....")
timer.set_timeout(change_picture, 1500)