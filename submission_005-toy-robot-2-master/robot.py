import re
import operator

def get_name():
    """Gets user input for the name of the robot"""
    name = input('What do you want to name your robot? ')
    print(name + ': Hello kiddo!')
    return name

def turn_off(name,off_check):
    """Turns the program off"""
    print(name + ': Shutting down..')
    off_check = True
    return off_check

def help_commands():
    """Shows list of commands"""
    print("""I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FOWARD  - Move the robot foward
BACK  - Move the robot backwards
RIGHT  - Turn the robot to the right
LEFT  - Turn the robot to the left
SPRINT  - Make the robot sprint""")

def list_to_str(x_y):
    """Converts list to str"""
    return'(' + str(x_y[0]) + ',' + str(x_y[1]) + ')'

def move_foward(steps,name,x_y,direction,direct_index):
    """Moves the robot forward"""
    print(' > ' + name + ' moved forward by ' + str(steps) + ' steps.')
    x_y = change_direction(direct_index,direction,x_y,'+',steps,False)
    current_position(name,x_y)
    return x_y

def move_back(steps,name,x_y,direction,direct_index):
    """Moves the robot back"""
    print(' > ' + name + ' moved back by ' + str(steps) + ' steps.')
    x_y = change_direction(direct_index,direction,x_y,'-',steps,True)
    current_position(name,x_y)
    return x_y

def move_right(x_y,direct_index,name):
    """Makes the robot turn right"""
    direct_index = direct_index + 1
    if direct_index == 4:
        direct_index = 0
    print(' > ' + name + ' turned right.')
    current_position(name,x_y)
    return direct_index

def move_left(direct_index,name,x_y):
    """Moves the robot left"""
    direct_index = direct_index - 1
    if direct_index == -1:
        direct_index = 3
    print(' > ' + name + ' turned left.')
    current_position(name,x_y)
    return direct_index

def change_direction(direct_index,direction,x_y, sign,steps,back):
    """Calculates the new position of the robot"""
    ops = { '+': operator.add, '-': operator.sub }
    if direction[direct_index] == 'N':
        x_y[1] = ops[sign](x_y[1],steps)
    if direction[direct_index] == 'E':
        x_y[0] = ops[sign](x_y[0],steps)
    if direction[direct_index] == 'S':
        if back == True:
            x_y[1] = (ops[sign](x_y[1],steps)) + (2 * steps)
        else:
            x_y[1] = (ops[sign](x_y[1],steps)) - (2 * steps)
    if direction[direct_index] == 'W':
        if back == True:
            x_y[0] = (ops[sign](x_y[0],steps)) + (2 * steps)
        else:
            x_y[0] = (ops[sign](x_y[0],steps)) - (2 * steps)
    return x_y

def check_area_foward(direct_index,num,x_y,name,check):
    """Checks if the robot will move outside the safe area"""
    if not check:
        if direct_index == 1  and (x_y[0] + num) >= 101:
            print(name + ': Sorry, I cannot go outside my safe zone.')
            return True
        if direct_index == 3 and (x_y[0] - num) <= -101:
            print(name + ': Sorry, I cannot go outside my safe zone.')
            return True
        if direct_index == 0 and (x_y[1] + num) >= 201:
            print(name + ': Sorry, I cannot go outside my safe zone.')
            return True
        if direct_index == 2 and (x_y[1] - num) <= -201:
            print(name + ': Sorry, I cannot go outside my safe zone.')
            return True
        else:
            return False
    return True

def check_area_back(direct_index,num,x_y,name):
    """Checks if the robot will move outside the safe area"""
    if direct_index == 1  and (x_y[0] - num) <= -101:
        print(name + ': Sorry, I cannot go outside my safe zone.')
        return True
    if direct_index == 3 and (x_y[0] + num) >= 101:
        print(name + ': Sorry, I cannot go outside my safe zone.')
        return True
    if direct_index == 0 and (x_y[1] - num) <= -201:
        print(name + ': Sorry, I cannot go outside my safe zone.')
        return True
    if direct_index == 2 and (x_y[1] + num) >= 201:
        print(name + ': Sorry, I cannot go outside my safe zone.')
        return True
    return False

def current_position(name,x_y):
    """Displays the current position"""
    print(' > ' + name + ' now at position ' + list_to_str(x_y) + '.')

def move_sprint(steps,original_steps,name,direction,direct_index,x_y):
    check = False
    #base case
    if steps == original_steps:
        if not check_area_foward(direct_index,steps,x_y,name,check):
            print(' > ' + name + ' moved forward by ' + str(steps) + ' steps.')
            x_y = change_direction(direct_index,direction,x_y,'+',steps,False)
        else:
            check = True
        return check,x_y
    #recursion
    check,x_y = move_sprint(steps + 1,original_steps,name,direction,direct_index,x_y)
    if not check_area_foward(direct_index,steps,x_y,name,check):
        print(' > ' + name + ' moved forward by ' + str(steps) + ' steps.')
        x_y = change_direction(direct_index,direction,x_y,'+',steps,False)
    else:
        check = True
        return check,x_y
    return check,x_y

def check_commands(name):
    """Checks if a command has been entered and then calls the correct function"""
    direction = ['N','E','S','W']
    direct_index = 0
    x_y = [0,0]
    off_check = False
    while not off_check:
        user_input = input(name + ': What must I do next? ')
        num = 0
        try:
            num = int(re.search(r'\d+', user_input).group())
        except:
            pass
        if user_input.upper() == 'OFF':
            off_check = turn_off(name,off_check)
        elif user_input.lower() == 'help':
            help_commands()
        elif user_input.upper() == ('FORWARD ' + str(num)):
            check = check_area_foward(direct_index,num,x_y,name,False)
            if check:
                current_position(name,x_y)
            else:
                x_y = move_foward(num,name,x_y,direction,direct_index)
        elif user_input.upper() == ('BACK ' + str(num)):
            check = check_area_back(direct_index,num,x_y,name)
            if check:
                current_position(name,x_y)
            else:
                x_y = move_back(num,name,x_y,direction,direct_index)
        elif user_input.upper() == 'RIGHT':
            direct_index = move_right(x_y,direct_index,name)
        elif user_input.upper() == 'LEFT':
            direct_index = move_left(direct_index,name,x_y)
        elif user_input.upper() == 'SPRINT ' + str(num):
            check2,x_y = move_sprint(1,num,name,direction,direct_index,x_y)
            current_position(name,x_y)
        else:
            print(name + ': Sorry, I did not understand \'' + user_input + '\'' +'.')


def robot_start():
    """This is the entry function, do not change"""
    name = get_name()
    check_commands(name)
        
pass


if __name__ == "__main__":
    robot_start()
