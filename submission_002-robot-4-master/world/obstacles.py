import random
ob_list = []

def create_list():
    """Generates the random list, called in robot_start"""
    global ob_list
    for x in range(random.randint(1,10)):
        xy_tuple = (random.randint(-100,100),random.randint(-200,200))
        ob_list.append(xy_tuple)

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