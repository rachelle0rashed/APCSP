#################################################################
# In this project, you'll use steganography to encode a secret
# image inside of a cover image without the cover
# image looking modified.
#
# YOUR JOB: implement the following functions
#################################################################

#==============CONSTANTS==============\\

# Constants for the images
ORIGINAL_URL = "https://codehs.com/uploads/c709d869e62686611c1ac849367b3245"
SECRET_URL = "https://codehs.com/uploads/e07cd01271cac589cc9ef1bf012c6a0c"
IMAGE_LOAD_WAIT_TIME = 1000

# Constants for pixel indices
RED = 0
GREEN = 1
BLUE = 2

# Constants for colors
MAX_COLOR_VALUE = 255
MIN_COLOR_VALUE = 0
COLOR_THRESHOLD = 128

# Constants for spacing
X_GAP = 100
Y_GAP = 50
TEXT_Y_GAP = 4
IMAGE_WIDTH = 100
IMAGE_HEIGHT = 100
IMAGE_X = 25
IMAGE_Y = 25

# Set Canvas size
set_size(400, 480)

#################################################################
#
# Encodes the given secret pixel into the low bits of the
# RGB values of the given cover pixel
# Returns the modified cover pixel
#
#################################################################
def set_lowest_bit(value, bit_value):
    new_value = value + bit_value
    return new_value

#################################################################
# Extracts the RGB values for a secret pixel from the low bits
# of the given cover pixel
# 
# Input is an array of RGB values for a pixel.
# 
# Returns a tuple of RGB values for the decoded pixel
#################################################################
def decode_pixel(cover_pixel):
    # Implement this function
    secret_pixel = [0,0,0]
    for i in range(len(cover_pixel - 1)):
        secret_pixel[i] = get_lowest_bit(cover_pixel[i] * 255)
        new_bit[0] = 255
        return secret_pixel

#=========HELPER FUNCTIONS==========#

# Returns true if the given value is even, false otherwise
def is_even(value):
    if int(value) % 2 == 0:
        return True
    if int(value) % 2 == 1:
        return False

#################################################################
#
# Given a number, return the lowest bit in the binary representation
# of the number.
# Returns either a 0 or a 1
#
#################################################################
def get_lowest_bit(value):
    # Implement this function
    lowest_bit = 0
    if is_even(value) == True:
        lowest_bit = 0
    else: 
        lowest_bit = 1
    # return a temporary value.  Change this!!
    return lowest_bit 


#################################################################
# 
# Given a number, return a new number with the same underlying bits
# except the lowest bit is set to the given bit_value.
#
#################################################################
def encode_pixel(cover_pixel, secret_pixel):
    pixel_value = [0,0,0]
    for i in range(3):
        if secret_pixel[i]>= COLOR_THRESHOLD:
            lowBit = get_lowest_bit(cover_pixel[i])
            if is_even(lowBit) == True:
                pixel_value[i] = set_lowest_bit(cover_pixel[i],1)
            elif is_even(lowBit) == False:
                pixel_value = set_lowest_bit(cover_pixel[i], 0)
        elif secret_pixel[i] < COLOR_THRESHOLD:
            lowBit = get_lowest_bit(cover_pixel[i])
            if is_even(lowBit) == True:
                pixel_value[i] = set_lowest_bit(cover_pixel[i], 0)
            if is_even(lowBit) == False:
                pixel_value[i] = set_lowest_bit(cover_pixel[i], -1)
    return pixel_value


"""
********************STARTER CODE BELOW******************************

 Feel free to read the starter code and see how this program works!
 But you do not need to change any code below this line.

 Your job is to implement the functions above this line!

********************************************************************/
"""

"""

 Encrypts the secret image inside of the cover image.
 For each pixel in the cover image, the lowest bit of each
 R, G, and B value is set to a 0 or 1 depending on the amount of
 R, G, and B in the corresponding secret pixel.
 If an R, G, or B value in the secret image is between 0 and 127,
 set a 0, if it is between 128 and 255, set a 1.
 
 Then returns an image.

"""
def encrypt(cover, secret):
    # Loop over each pixel in the image
    for x in range(IMAGE_WIDTH):
        for y in range(IMAGE_HEIGHT):
            pass
            # Get the pixels at this location for both images
            cover_pixel = cover.get_pixel(x, y)
            secret_pixel = secret.get_pixel(x, y)
            
            # Modify the cover pixel to encode the secret pixel
            new_cover_color = encode_pixel(cover_pixel, secret_pixel)
            
            # Update this pixel in the cover image to have the
            # secret bit encoded
            cover.set_red(x, y, new_cover_color[RED])
            cover.set_green(x, y, new_cover_color[GREEN])
            cover.set_blue(x, y, new_cover_color[BLUE])
    print("Done encrypting")
    return cover

"""

 Decrypts a secret image from an encoded cover image.
 Returns an Image
 
"""
def decrypt(cover_image, result):
    # secret image will start off with the cover pixels
    # As we loop over the coverImage to discover the secret embedded image,
    # we will update secretImage pixel by pixel
    # Loop over each pixel in the image
    for x in range(IMAGE_WIDTH):
        for y in range(IMAGE_HEIGHT):
            #Get the current pixel of the cover image
            cover_pixel = cover_image.get_pixel(x, y)
        
            # Compute the secret_pixel from this cover pixel
            secret_pixel_color = decode_pixel(cover_pixel)
            result.set_red(x, y, secret_pixel_color[RED])
            result.set_green(x, y, secret_pixel_color[GREEN])
            result.set_blue(x, y, secret_pixel_color[BLUE])
       
    print("Done decrypting")
    return result

# Image width cannot be odd, it messes up the math of the encoding
if IMAGE_WIDTH % 2 == 1:
    IMAGE_WIDTH -= 1

#Set up original image
#Image(x, y, filename, width=50, height=50, rotation=0) // x,y top left corner
original = Image(ORIGINAL_URL, IMAGE_X, IMAGE_Y, IMAGE_WIDTH, IMAGE_HEIGHT)

# Set up secret image
secret = Image(SECRET_URL, IMAGE_X + original.get_width() + X_GAP, IMAGE_Y,
     IMAGE_WIDTH, IMAGE_HEIGHT)

# Set up the cover image 
# (identical to original, but will be modified to encode the secret image)
cover_x = IMAGE_X + IMAGE_WIDTH 
cover_y = IMAGE_Y + Y_GAP + IMAGE_HEIGHT
cover = Image(ORIGINAL_URL, cover_x, cover_y, IMAGE_WIDTH, IMAGE_HEIGHT)

# Set up result image
result = Image(ORIGINAL_URL, cover_x, cover_y + Y_GAP + IMAGE_HEIGHT,
                 IMAGE_WIDTH, IMAGE_HEIGHT)

# Add originals
add(original)
add(secret)


# Add cover and result
add(cover)
add(result)

# Add labels for each image
font = "11pt Arial"
def make_label(text, x, y, font):
    label = Text(text)
    label.set_position(x,y)
    label.set_font(font)
    add(label)

# Text(label, x=0, y=0, color=None,font=None) // x,y is 
# original label
x_pos = original.get_x()
y_pos = original.get_y() - TEXT_Y_GAP
make_label("Original Cover Image", x_pos, y_pos, font)

#secret label
x_pos = secret.get_x()
y_pos = secret.get_y() - TEXT_Y_GAP
make_label("Original Secret Image", x_pos, y_pos, font)

# cover label
x_pos = IMAGE_X
y_pos = cover.get_y() - TEXT_Y_GAP
make_label("Cover Image with Secret Image encoded inside", x_pos, y_pos, font)

# result label
x_pos = IMAGE_X
y_pos = cover.get_y() + IMAGE_HEIGHT + Y_GAP - TEXT_Y_GAP
make_label("Resulting Secret Image decoded from Cover Image", x_pos, y_pos, font)


# Encrypt and decrypt the image
# Displays the changed images
def run_encryption():
    encrypt(cover, secret)
    print("Decrypting .........")
    timer.set_timeout(lambda: decrypt(cover, result), IMAGE_LOAD_WAIT_TIME)
    
# Wait for images to load before encrypting and decrypting
print("Encrypting ............")
timer.set_timeout(run_encryption, IMAGE_LOAD_WAIT_TIME)