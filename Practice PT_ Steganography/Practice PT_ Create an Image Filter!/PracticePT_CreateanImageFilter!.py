# Constants for the image
#This is the Bright Vibrant filter
IMAGE_URL = "https://codehs.com/uploads/d2f903027025292e22c07e11bb75086f"
IMAGE_WIDTH = 420
IMAGE_HEIGHT = 500
IMAGE_LOAD_TIME = 1000

image = Image(IMAGE_URL)
image.set_size(IMAGE_WIDTH, IMAGE_HEIGHT)
add(image)

"""
 Filter that takes an image as a parameter
 and applies a filter, then returns the filtered image
"""
# This is an example of an invert filter
def custom_filter(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    
    new_red = min (red * 2, 255)
    new_green = min(green *2, 255)
    new_blue = min(blue * 2, 255)
    new_colors =  [new_red, new_green, new_blue]
    return new_colors

def vibrant_filter(image):
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            pixel = image.get_pixel(x,y)
            new_colors = custom_filter(pixel)
            image.set_red(x, y, new_colors[0])
            image.set_green(x, y, new_colors[1])
            image.set_blue(x, y, new_colors[2])

def change_image():
    global image
    image = vibrant_filter(image)
    
timer.set_timeout(change_image, IMAGE_LOAD_TIME)
print("This will take a bit, please be patient. BEHOLD THE BRIGHT VIBRANT AMAZINGNESS!!XD")