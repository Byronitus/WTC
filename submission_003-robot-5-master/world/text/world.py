import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 


directions = ['forward', 'right', 'back', 'left']
min_y, max_y = -200, 200
min_x, max_x = -100, 100
x_old = 0
y_old = 0
global position_x, position_y,new_x ,new_y
position_x = 0
position_y = 0

def show_obstacles(ob_list):
    """Prints out all the obstacles if the list of obstacles was generated"""
    if ob_list:
        print('There are some obstacles:')
        for x in ob_list:
            print('- At position ' + str(x[0]) + ',' + str(x[1]) + ' (to ' + str(x[0] + 4) + ',' + str(x[1] + 4) + ')')

def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y

def show_position(robot_name,x,y):
    print(' > '+robot_name+' now at position ('+str(x)+','+str(y)+').')


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
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
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
        print('Robot went to ' + str(x[0]) + ',' + str(x[1]))
    return new_list[-1]