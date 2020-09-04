
def move_square(size):
    '''This function moves the robot in a square'''
    print("Moving in a square of size "+str(size)) 
    for i in range(4):
        degrees = 90
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees") 

def move_rectangle(length,width):
    '''This function moves the robot in a rectangle'''
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")

def move_circle(degrees,length):
    '''#This function moves the robot in a circle'''
    print("Moving in a circle")
    for i in range(360):
        length = 1
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")

# TODO: Decompose into functions
def move():
    '''I chose intiate_robot as the name because this function calls the other move functions instead of actually moving the robot itself'''
    size = 10
    move_square(size)
    length = 20
    width = 10
    move_rectangle(length,width)
    degrees = 1
    move_circle(degrees,length)
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        size = 20
        print("* Move Forward "+str(size))
        move_square(size)
            

    print("Crop circles - 4 circles")
    for i in range(4):
        print("* Move Forward "+str(length))
        move_circle(degrees,length)


def robot_start():
    move()


if __name__ == "__main__":
    robot_start()
