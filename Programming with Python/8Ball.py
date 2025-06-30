# Find the center to use for the ball and number
center_x = get_width() / 2
center_y = get_height() / 2

# Create a circle (black by default)
ball = Circle(100)
ball.set_position(center_x, center_y)
add(ball)

# Add a white 8, 50 pt Arial font
number = Text("8")
number.set_color(Color.white)
number.set_font("50pt Arial")
# Adjust the position based on the size of the number
number.set_position(center_x - number.get_width()/2, 
        center_y + number.get_height()/2)
add(number)