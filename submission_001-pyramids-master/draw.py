

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    shape_param = input("Shape?: ")
    while shape_param.lower() not in ["square","triangle","pyramid","rectangle","parallelogram","trapezium"]:
        shape_param = input("Shape?: ")
    return shape_param.lower()


# TODO: Step 1 - get height (it must be int!)
def get_height():
    height = "a"
    while height.isnumeric() == False:
        height = input('Height?: ')
    while int(height) >= 80 and int(height) <= 0:
        height = input('Height?: ')
    return int(height)


# TODO: Step 2
def draw_pyramid(height, outline):
    s = '*'
    sp = ' '
    nums = 1
    numsp = height - 1
    count = 1
    if outline == False:
        while count <= height:
            print((sp * numsp) + (s * nums))
            numsp = numsp - 1
            nums = nums + 2
            count = count + 1
    else:
        while count <= height:
            if count == 1 or count == height:
                print((sp * numsp) + (s * nums))
            else:
                print((sp * numsp) + s + (sp * (nums-2)) + s)
            numsp = numsp - 1
            nums = nums + 2
            count = count + 1

        

    


# TODO: Step 3
def draw_square(height, outline):
    count = 1
    if outline == False:
       while count <= height:
        print('*' * height)
        count = count + 1 
    else:
        while count <= height:
            if count == 1 or count == height:
                print('*' * height)
            else:
                print('*' + " " * (height-2) + '*')
            count = count + 1

    


# TODO: Step 4
def draw_triangle(height, outline):
    s = '*'
    sp = ' '
    count = 1
    if outline == False:
       while count <= height:
        print(s * count)
        count = count + 1 
    else:
        while count <= height:
            if count == 1 or count == 2 or count == height:
                print(s * count)
            else:
                print(s + sp * (count - 2) + s)
            count = count + 1


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == 'pyramid':
        draw_pyramid(height, outline)
    elif shape == 'triangle':
        draw_triangle(height, outline)
    elif shape == 'square':
        draw_square(height, outline)
    elif shape == 'rectangle':
        draw_rectangle(height, outline)
    elif shape == 'parallelogram':
        draw_parallelogram(height, outline)
    else:
        draw_trapezium(height, outline)
    


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    answer = input('Outline only? (y/N): ')
    if answer == 'n':
        outline = False
    else:
        outline = True
    return outline


def draw_rectangle(height,outline):
    count = 1
    if outline == False:
        while count <= height:
            print('*' * height * 4)
            count = count + 1 
    else:
        while count <= height:
            if count == 1 or count == height:
                print('*' * height*4)
            else:
                print('*' + " " * ((height* 4)-2) + '*')
            count = count + 1
 


def draw_parallelogram(height, outline):
    count = 1
    s = '*'
    sp = ' '
    numsp = height - 1
    if outline == False:
        while count <= height:
            print((sp * numsp) + s * height)
            numsp = numsp - 1
            count = count + 1
    else:
        while count <= height:
            if count == 1 or count == height:
                print((sp * numsp) + s * height)
            else:
                print((sp * numsp) + s +(sp * (height -2)) + s)
            count = count + 1
            numsp = numsp - 1

def draw_trapezium(height, outline):
    count = 1
    s = '*'
    sp = ' '
    nums = int((height/2) + 10)
    numsp = (height - 1)
    if outline == False:
        while count <= height:
            print((sp * numsp) + (s * nums))
            count = count + 1
            nums = nums + 2
            numsp = numsp - 1
    else:
        while count <= height:
            if count == 1 or count == height:
              print((sp * numsp) + (s * nums))
            else:
                print((sp * numsp) + s +(sp * (nums-2)) + s)  
            count = count + 1
            nums = nums + 2
            numsp = numsp - 1

if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

