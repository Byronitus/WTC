import random
ob_list = []
ob_list.append((0,20))
def check_ob_list(xy_tuple):
    c1 = False
    c2 = False
    count = 0
    for x in ob_list:
        if not xy_tuple == x:
            if abs(xy_tuple[0] - x[0]) <= 1 and abs(xy_tuple[0] - x[0]) >= 0:
                c1 = True
            if abs(xy_tuple[1] - x[1]) <= 1 and abs(xy_tuple[1] - x[1]) >= 0:
                c2 = True
            if c1 and c2:
                return True
        else:
            count = count + 1
        if count > 1:
            return True
    return False
        

def create_list():
    global ob_list
    x = random.randint(149,150)
    count = 0
    while count <= x:
        xy_tuple = (random.randint(-100,100),random.randint(-200,200))
        ob_list.append(xy_tuple)
        if check_ob_list(xy_tuple):
            ob_list.pop(-1)
            count = count -1
        count = count + 1


def is_position_blocked(x,y):
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
    if one > two:
        return two , one
    if two > one:
        return one , two

def is_path_blocked(x1,y1, x2, y2):
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
    return ob_list

def delete_ob_list():
    global ob_list
    ob_list = []