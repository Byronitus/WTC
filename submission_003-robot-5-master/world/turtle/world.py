import turtle
screen = turtle.getscreen()
m = turtle.Turtle()
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
screen = turtle.Screen()
screen.setup((100 - -100) * 4, (200 - -200) * 4)
screen.setworldcoordinates(-100, -200, 200, 200)

directions = ['forward', 'right', 'back', 'left']
min_y, max_y = -200, 200
min_x, max_x = -100, 100
global position_x, position_y
x_old = 0
y_old = 0
global position_x, position_y,new_x ,new_y
position_x = 0
position_y = 0

def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def draw_obstacles(ob_list):
    """Draws every obstacle that is in the list"""
    turtle.tracer(0, 0)
    for x in ob_list:
        m.penup()
        m.goto(x[0],x[1])
        m.pendown()
        m.begin_fill()
        for i in range(4):
            m.forward(4)
            m.left(90)
        m.end_fill()
        m.penup()
        m.home()
    turtle.update()
    turtle.tracer(1,1)

def draw_barrier():
    """Draws the barrier"""
    m.speed(0)
    m.color('red')
    m.penup()
    m.goto(101,201)
    m.pendown()
    m.goto(101,-201)
    m.goto(-101,-201)
    m.goto(-101,201)
    m.goto(101,201)
    m.penup()
    m.home()


draw_barrier()
m.left(90)

def show_position(robot_name,x,y):
    """Makes the turtle go to the x y position"""
    m.pendown()
    m.goto(x,y)
    m.penup()


def update_position(steps,x,y,current_direction_index):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y, new_x , new_y, x_old , y_old
    x_old = x
    y_old = y
    position_x = x
    position_y = y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        m.right(90)
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        m.left(90)
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


def return_position():
    """Returns the current position"""
    return position_x, position_y

def mazerun(new_list):
    """makes the robot go through the path"""
    for x in new_list:
        m.speed(1)
        m.goto(x)
    return new_list[-1]