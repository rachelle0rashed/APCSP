NUM_CIRCLES = 15

# This graphics program should draw a caterpillar. 
# A caterpillar is made up of NUM_CIRCLES circles.
# The circles should alternate red - green - red - green, etc
# Use a for loop to draw the worm, 
# centered vertically in the screen. 
# Also, be sure that the worm is still drawn across 
# the whole canvas, even if the value of NUM_CIRCLES is changed.

RADIUS = get_width()/(NUM_CIRCLES*2)
x = get_width()/2
y = get_height()/2
diameter = get_width()/NUM_CIRCLES

for i in range(NUM_CIRCLES):
    circ = Circle(RADIUS)
    circ.set_position(diameter*i+RADIUS,y)
    if (i % 2 == 0):
        circ.set_color(Color.red)
    else:
        circ.set_color(Color.green)
    add(circ)