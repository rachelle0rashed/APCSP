# Make your creation here!

#A blue car driving to the Bangladesh flag


red_sun = 50
flag_width = red_sun * 6
flag_height = red_sun * 4
flag_offset_x = red_sun * 2.5
flag_offset_y = red_sun * 2
cap_r = 50

def circ(x,y):
    circ = Circle(red_sun)
    circ.set_position(x,y)
    circ.set_color(Color.red)
    add(circ)
    
def flag(x,y):
    flag = Rectangle(flag_width, flag_height)
    flag.set_color(Color.green)
    flag_x = x - flag_offset_x
    flag_y = y - flag_offset_y
    flag.set_position(flag_x, flag_y)
    add(flag)
    
def pole(x,y):
    flag_x = x - flag_offset_x
    flag_y = y - flag_offset_y
    pole = Line(flag_x, flag_y, flag_x, flag_height + (flag_y + 100))
    pole.set_color(Color.black)
    add(pole)

def car(x,y):
    rect = Rectangle(100,60)
    rect.set_position(x+100, y+155)
    rect.set_color(Color.blue)
    add(rect)
    
    
    circ = Circle(20)
    circ.set_color(Color.black)
    circ.set_position((x*2)-18, (y*2)-20)
    add(circ)
    
    circ = Circle(20)
    circ.set_color(Color.black)
    circ.set_position((x*2)-80, (y*2)-20)
    add(circ)
    
    rect = Rectangle(50, 25)
    rect.set_color(Color.white)
    rect.set_position(((x*2) - 100), (y*2) - 85)
    add(rect)
  

def bflag(x,y): 
    flag(x,y)
    circ(x,y)
    pole(x,y)
    car(x,y)
    
center_x = get_width()/2
center_y = get_height()/2
bflag(center_x, center_y)