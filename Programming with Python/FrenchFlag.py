# Create a Blue rectangle on left
width=get_width() /3
height=get_height() 
blue_rect=Rectangle(width,height)
blue_rect.set_color(Color.blue)
blue_rect.set_position(0,0)
add(blue_rect)
# Create a Red rectangle on right
width=get_width() /3
height=get_height() 
red_rect=Rectangle(width,height)
red_rect.set_color(Color.red)
red_rect.set_position(268,0)
add(red_rect)