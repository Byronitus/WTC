import random
ob_list = []
ob_list = [
        (-85, 175), (-30, 175), (30, 175) , (80, 175),
        (-56, 150), (0, 150),(56, 150),
        (-85, 120), (-30, 120), (30, 120), (80, 120),
        (-56, 95), (0, 95), (56, 95),
        (-85, 70), (-30, 70), (30, 70), (80, 70),
        (-56, 45), (0, 45), (56, 45),
        (-85, 20), (-30, 20), (30, 20), (80, 20),
        (-56, 0), (-30,0),(30, 0),
        (-85, -25), (-30,-25), (30, -25),(80, -25),
        (-56, -60), (0, -60), (56,-60),
        (-85, -95), (-30, -95), (30, -95), (80, -95),
        (-56, -120), (0, -120), (-56, -120),
        (-85, -145), (-30, -145), (30, -145), (80, -145),
        (-56, -175), (0, -175), (56, -175),
        (-85, -185), (-30, -185), (30, -185), (80, -185)
    ]


def create_list():
    pass
#     """Generates the random list, called in robot_start"""
#     global ob_list
#     for x in range(random.randint(1,10)):
#         xy_tuple = (random.randint(-100,100),random.randint(-200,200))
#         ob_list.append(xy_tuple)

n = 5
def draw_obstacle_line_x_pos(x,y):
    global ob_list
    for i in range(n):
        x_y = (x,y)
        x+=4
        ob_list.append(x_y)

def draw_obstacle_line_x_neg(x,y):
    global ob_list
    for i in range(n):
        x_y = (x,y)
        x-=4
        ob_list.append(x_y)

def draw_obstacle_line_y_pos(x,y):
    global ob_list
    for i in range(5):
        x_y = (x,y)
        y+=4
        ob_list.append(x_y)

def draw_obstacle_line_y_neg(x,y):
    global ob_list
    for i in range(5):
        x_y = (x,y)
        y-=4
        ob_list.append(x_y)

def draw_maze_obstacle(x,y):
    draw_obstacle_line_x_pos(x,y)
    draw_obstacle_line_x_neg(x,y)
    draw_obstacle_line_y_neg(x,y)        
    draw_obstacle_line_y_pos(x,y)

def lol():
    global ob_list
    f = len(ob_list)
    for i in range(f):
        draw_maze_obstacle(ob_list[i][0], ob_list[i][1])
    ob_list = set(ob_list) 

lol()

def is_position_blocked(x,y):
    """Checks if current position is in any of the obstacles"""
    for j in ob_list:
        x_check = False
        y_check = False
        if x >= j[0] and x <= (j[0] + 4):
            x_check = True 
        if y >= j[1] and y <= (j[1] + 4):
            y_check = True
        if x_check and y_check:
            return True
    return False

def smaller_bigger(one,two):
    """Returns the smaller value first"""
    if one > two:
        return two , one
    if two > one:
        return one , two

def is_path_blocked(x1,y1, x2, y2):
    """Checks if there is an obstacle in the path"""
    diff_list = []
    nums_x = smaller_bigger(x1 , x2)
    nums_y = smaller_bigger(y1 , y2)
    x_check = False
    if not x1 == x2:
        diff = range(nums_x[0],nums_x[1],4)
        for q in diff:
            diff_list.append(q)
        diff_list.append(nums_x[1])
        x_check = True
    elif not y1 == y2:
        diff = range(nums_y[0],nums_y[1],4)
        for q in diff:
            diff_list.append(q)
        diff_list.append(nums_y[1])
    else:
        return False
    for z in diff_list:
        if x_check:
            if is_position_blocked(z,y1):
                return True
        else:
            if is_position_blocked(x1,z):
                return True
    return False

def get_obstacles():
    """Returns the list of obstacles"""
    return ob_list

def delete_ob_list():
    """Deletes the list when the user says off"""
    global ob_list
    ob_list = []