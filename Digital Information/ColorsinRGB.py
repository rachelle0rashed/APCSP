from tkinter import *

WIDTH = 475
HEIGHT = 290
RED = 0
GREEN = 0
BLUE = 0

root = Tk()
screen = Canvas(root, width=WIDTH, height=HEIGHT, background="white")
screen.pack()

img = PhotoImage(width=WIDTH, height=HEIGHT)
screen.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

def rgb_to_hex(rgb):
    # translates an rgb tuple of int to a hex color code for Tkinter
    return "#%02x%02x%02x" % rgb  

# Create a single pixel at x, y coordinates with a
# RGB values from 0 to 255
def set_pixel_RGB(x, y, r, g, b):
    img.put(rgb_to_hex((r, g, b)), (x, y))

def create_column(x_pos, r, g, b):
    for y_pos in range(30, 230):
        # Color each individual pixel
        set_pixel_RGB(x_pos, y_pos, r, g, b)

for i in range(256):
    r = RED
    g = GREEN
    b = i
    # Offest first column by 30
    create_column(30 + i, r, g, b)

mainloop()