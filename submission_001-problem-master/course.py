

def create_outline():
    """
    TODO: implement your code here
    """
    set = {'Introduction to Python':'', 'Tools of the Trade':'', 'How to make decisions':'',
     'How to repeat code':'', 'How to structure data':'', 'Functions':'', 'Modules':''}
    problems = ['Problem 1, ','Problem 2, ', 'Problem 3']
    count = 0
    sorted_set = sorted(set)
    print('Course Topics:')
    for x in sorted_set:
        print('* ' + x)
        set[x] = ''.join(problems)
    print('Problems:')
    for x in set:  
        print('* '+ x + ' : ' + set[x])
    print('Student Progress:')
    students = [('John - ','How to repeat code - ', 'Problem 2 ', '[COMPLETED]'),
    ('Melt - ','Functions - ', 'Problem 1 ', '[STARTED]'),
    ('James - ','Modules - ', 'Problem 3 ', '[GRADED]')]
    students.sort(key=lambda b:b[3], reverse=True)
    for x in students:
        print(str(count + 1) + '. ' + str(''.join(students[count])))
        count = count + 1
    pass


if __name__ == "__main__":
    create_outline()
