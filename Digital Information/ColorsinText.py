from tkinter import *

WIDTH = 475
HEIGHT = 290
SIZE_IN_PIXELS = 30
COLORS = ["red", "orange", "yellow", "green", "blue", "indigo"]


root = Tk()
screen = Canvas(root, width=WIDTH, height=HEIGHT, background="white")
screen.pack()

img = PhotoImage(width=WIDTH, height=HEIGHT)
screen.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

def set_pixel_color(x, y, color):
    img.put(color, (x, y))
    
def create_column(x, color):
    for i in range(SIZE_IN_PIXELS):
        x_pos = x + i
        for y_pos in range(30, 230):
            # Color each individual pixel
            set_pixel_color(x_pos, y_pos, color)

for i in range(len(COLORS)):
    # Offest first column by 30
    create_column(30 + SIZE_IN_PIXELS * i, COLORS[i])

mainloop()