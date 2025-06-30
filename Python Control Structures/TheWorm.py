NUM_CIRCLES = 15

# This graphics program should draw a worm. 
# A worm is made up of NUM_CIRCLES circles. 
# Use a for loop to draw the worm, 
# centered vertically in the screen. 
# Also, be sure that the worm is still drawn across 
# the whole canvas, even if the value of NUM_CIRCLES is changed.
radius = get_width()/(NUM_CIRCLES*2)
x = get_width()/2
y = get_height()/2
diameter = get_width()/NUM_CIRCLES

for i in range(NUM_CIRCLES):
    circ = Circle(radius)
    circ.set_color(Color.black)
    circ.set_position(diameter*i+radius,y)
    add(circ)