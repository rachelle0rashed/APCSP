""" 
 Draws the first scene on the canvas and outputs the first
 section of text for the story.
"""
#Make Background
def background():
    sky = Rectangle(get_width(),get_height())
    sky.set_position(0,0)
    sky.set_color(Color.blue)
    add(sky)
    ground = Rectangle(get_width(),get_height()/6)
    ground.set_position(0,400)
    ground.set_color(Color.green)
    add(ground)
    
#make head of ghost
def head(x,y,color):
    head = Circle(35)
    head.set_position(x,y)
    head.set_color(color)
    add(head)
# make body of ghost
def body(x,y,color):
    body = Rectangle(35*2,60)
    body.set_position(x-70/2,y)
    body.set_color(color)
    add(body)
    
#make eyes looking at the right
def eyes_looking_r(x,y): 
    eye = Circle(10)
    eye.set_position(x-14,y)
    eye.set_color(Color.white)
    add(eye)
    eye = Circle(4)
    eye.set_position(x-8, y)
    eye.set_color(Color.blue)
    add(eye)
    eye = Circle(10)
    eye.set_position(x+14,y)
    eye.set_color(Color.white)
    add(eye)
    eye = Circle(4)
    eye.set_position(x+20,y)
    eye.set_color(Color.blue)
    add(eye)
#make eyes looking the left
def eyes_looking_l(x,y):
    eye = Circle(10)
    eye.set_position(x-14,y)
    eye.set_color(Color.white)
    add(eye)
    eye = Circle(4)
    eye.set_position(x-19,y)
    eye.set_color(Color.blue)
    add(eye)
    eye = Circle(10)
    eye.set_position(x+14,y)
    eye.set_color(Color.white)
    add(eye)
    eye = Circle(4)
    eye.set_position(x+9,y)
    eye.set_color(Color.blue)
    add(eye)
#make feet of ghost    
def feet(x,y,color):
    dis = (70/(3*2)) * 2
    for i in range(3): 
        foot = Circle(70/(3*2))
        foot.set_color(color)
        foot_x = x - 35 + 70/6 + i * dis
        foot_y = y + 60
        foot.set_position(foot_x, foot_y)
        add (foot)
#make purple ghost   
def draw_purple():
    head(100,300,Color.purple)
    body(100,300,Color.purple)
    eyes_looking_r(100,300)
    feet(100,300,Color.purple)
#Make red ghost
def draw_red():
    head(300,300,Color.red)
    body(300,300,Color.red)
    eyes_looking_l(300,300)
    feet(300,300,Color.red)
    
#make scene 1
def draw_scene1():
    print("Polly wanted to find friends and came across a red ghost and ask questions.")
    background()
    draw_purple()
    draw_red()
#make text
    txt = Text("Hi! My name is Polly.")
    txt.set_position(10,150)
    txt.set_color(Color.black)
    txt.set_font("15pt Arial")
    add(txt)
    txt2 = Text("What's your name and do you like food?")
    txt2.set_position(10,180)
    txt2.set_color(Color.black)
    txt2.set_font("15pt Arial")
    add(txt2)
""" txt.set
 Draws the second scene on the canvas and outputs the second
 section of text for the story.
"""
#Make scene 2
def draw_scene2():
    print("Polly listens to the red ghost and finds out her name as she is answering her questions.")
    background()
    draw_purple()
    draw_red()
#make text
    txt = Text("My name is Tiana")
    txt.set_position(220,150)
    txt.set_color(Color.black)
    txt.set_font("15pt Arial")
    add(txt)
    txt2 = Text(" and yes I love food!")
    txt2.set_position(220,180)
    txt2.set_color(Color.black)
    txt2.set_font("15pt Arial")
    add(txt2)
""" 
 Draws the third scene on the canvas and outputs the second
 section of text for the story.
"""
#make scene 3
def draw_scene3():
    print("Polly finds the courages to asked Tiana to be her friend. ")
    background()
    draw_purple()
    draw_red()
#make text
    txt = Text("Can we be friends?:P")
    txt.set_position(10,90)
    txt.set_color(Color.black)
    txt.set_font("15pt Arial")
    add(txt)
    txt2 = Text("Sure!:)")
    txt2.set_position(300,150)
    txt2.set_color(Color.black)
    txt2.set_font("15pt Arial")
    add(txt2)
    

""" 
 Draws the fourth scene on the canvas and outputs the second
 section of text for the story.
"""
#make scene 4
def draw_scene4():
    print("They lived happily ever after.")
    background()
#make text
    txt = Text("Polly and Tiana Friendship")
    txt.set_position(30, 100)
    txt.set_color(Color.black)
    txt.set_font("15pt Time New Roman")
    add(txt)
    txt2 = Text("Lived Happily Ever After!")
    txt2.set_position(30,120)
    txt2.set_color(Color.black)
    txt2.set_font("15pt Time New Roman")
    add(txt2)
    txt3 = Text("THE END!:O")
    txt3.set_position(20, 300)
    txt3.set_color(Color.black)
    txt3.set_font("50pt Time New Roman")
    add(txt3)

"""
 This is set up code that makes the story advance from
 scene to scene. Feel free to check out this code and
 learn how it works!
 But be careful! If you modify this code the story might
 not work anymore.
"""

scene_counter = 0

# When this function is called the next scene is drawn.

def draw_next_screen(x, y):
    global scene_counter 
    scene_counter += 1

    if scene_counter == 1:
        draw_scene1()
    elif scene_counter == 2:
        draw_scene2()
    elif scene_counter == 3:
        draw_scene3()
    else:
        draw_scene4()

welcome = Text("Click to Begin!")
welcome.set_position(get_width() / 2 - welcome.get_width() / 2, get_height() / 2)
add(welcome)

add_mouse_click_handler(draw_next_screen)