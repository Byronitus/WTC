import random
from collections import defaultdict
import robot as r
graph_of_edges = defaultdict(list)
list_of_edges = []
arg = ''

def set_end(command):
    """Sets the end point"""
    global arg
    arg = command
    if command == 'top':
        return (0,200),1,': I am at the top edge.'
    if command == 'bottom':
        return (0,-200),1,': I am at the bottom edge.'
    if command == 'left':
        return (-100,0),0,': I am at the left edge.'
    if command == 'right':
        return (100,0),0,': I am at the right edge.'
    return (0,200),1,': I am at the top edge.'


def is_position_blocked(x,y,ob_list):
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


def create_list_of_edges(ob_list):
    """Creates list of all the edges"""
    global position_list, list_of_edges
    count1 = -200
    while count1 <= 200:
        count2 = -100
        while count2 <= 100:
            if not is_position_blocked(count2,count1,ob_list):
                if not is_position_blocked(count2 , count1 + 1,ob_list) and count1 + 1 <= 200 and count2 % 3 == 0:
                   list_of_edges.append(((count2,count1),(count2 ,count1 + 1)))
                if not is_position_blocked(count2 + 1 , count1,ob_list) and count2 + 1 <= 100:
                    list_of_edges.append(((count2 ,count1),(count2 + 1, count1)))
            count2 = count2 + 1
        count1 = count1 + 1


def create_edges():
    """Changes the list of edges to a graph of edges"""
    global list_of_edges, graph_of_edges
    for y in list_of_edges:
        a,b = y[0] , y[1]
        graph_of_edges[a].append(b)
        graph_of_edges[b].append(a)


def bfs(beginning, end , graph_of_edges,i):
    """Uses the breadth first search algorithm"""
    visited = [] 
    queue = [[beginning]] 
    if beginning == end: 
        return
    while queue: 
        path = queue.pop(0) 
        current_node = path[-1] 
        if current_node not in visited: 
            adjacent_nodes = graph_of_edges[current_node] 
            for node in adjacent_nodes: 
                new_path = list(path) 
                new_path.append(node) 
                queue.append(new_path)
                if node == end  or node[i] == end[i]: 
                    return new_path
            visited.append(current_node) 
    print('No path exists') 
    return []




def win_check(output,dir_index,name):
    """Returns True if win condition is met"""
    if output == ''+name+': Sorry, I cannot go outside my safe zone.' and dir_index == r.current_direction_index:
        return True

def edge_set(arg):
    """Sets which edge the robot must go to"""
    if arg == '' or arg == 'top':
        r.current_direction_index = 0
    elif arg == 'bottom':
        r.current_direction_index = 2
    elif arg == 'left':
        r.current_direction_index = 3
    elif arg == 'right':
        r.current_direction_index = 1

def go_to_edge(name):
    """A more simple pathfinding method used when their are less obstacles to make the process quicker"""
    r.position_x = 0
    r.position_y = 0
    edge_set(arg)
    copy_current_dir_index = r.current_direction_index
    check = False
    while not check:
        r.current_direction_index = copy_current_dir_index
        steps = random.randint(1,10)
        ex , output = r.handle_command(name,'forward ' + str(steps))
        if output == 'Sorry, there is an obstacle in the way.':
            r.current_direction_index = random.randint(0,3)
            ex, output = r.handle_command(name,'forward ' + str(steps))
        if win_check(output,copy_current_dir_index,name):
            return True