# Write a function to draw a horizontal
# line given a y position and a length
x=0
y=0
def horizontal_line(y,x):
    line = Line(0,x,y,x)
    add(line)
    
horizontal_line(100, 200)
horizontal_line(200, 100)
horizontal_line(300, 20)