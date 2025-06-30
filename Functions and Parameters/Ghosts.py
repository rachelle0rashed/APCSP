# Constants for body
HEAD_RADIUS = 35
BODY_WIDTH = HEAD_RADIUS * 2
BODY_HEIGHT = 60
NUM_FEET = 3
FOOT_RADIUS = (BODY_WIDTH) / (NUM_FEET * 2)

# Constants for eyes
PUPIL_RADIUS = 4
PUPIL_LEFT_OFFSET = 8
PUPIL_RIGHT_OFFSET = 20
EYE_RADIUS = 10
EYE_OFFSET = 14


# Put your function(s) here
def head(x, y, color):
    head = Circle(HEAD_RADIUS)
    head.set_position(x,y)
    head.set_color(color)
    add(head)
    
def body(x, y, color):   
    body = Rectangle(BODY_WIDTH, BODY_HEIGHT)
    body.set_position(x-BODY_WIDTH/2, y)
    body.set_color(color)
    add(body)
    
def eyes(x, y):
    # lefteye
    eye = Circle(EYE_RADIUS)
    eye.set_position(x-EYE_OFFSET, y)
    eye.set_color(Color.white)
    add(eye)
    #leftpupil
    eye = Circle(PUPIL_RADIUS)
    eye.set_position(x-19, y)
    eye.set_color(Color.blue)
    add(eye)
    #righteye
    eye = Circle(EYE_RADIUS)
    eye.set_position(x+EYE_OFFSET, y)
    eye.set_color(Color.white)
    add(eye)
    #rightpupil
    eye = Circle(PUPIL_RADIUS)
    eye.set_position(x+8, y)
    eye.set_color(Color.blue)
    add(eye)
    
#feet
def feet(x, y, color):
    dis = FOOT_RADIUS * 2
    for i in range(NUM_FEET):
        foot = Circle(FOOT_RADIUS)
        foot.set_color(color)
        foot_x = (x - (BODY_WIDTH/2) + FOOT_RADIUS + i * dis )
        foot_y = y + BODY_HEIGHT 
        foot.set_position(foot_x, foot_y)
        add(foot)
        
#draw the ghost booooo
def draw_ghost(x, y, color):
    head(x, y, color)
    body(x, y, color)
    eyes(x, y)
    feet(x, y, color)
    
center_x = get_width()/2
center_y = get_height()/2
draw_ghost(center_x, center_y, Color.red)
draw_ghost(100, 100, Color.green)
draw_ghost(370, 150, Color.black)
draw_ghost(40, 200, Color.orange)
draw_ghost(300, 50, Color.yellow)
draw_ghost(300, 300, Color.blue)