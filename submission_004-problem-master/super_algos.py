
def find_min(element):
    """TODO: complete for Step 1"""
    if element:
        for x in range(len(element)):
            if not isinstance(element[x],int):
                return -1
    else:
        return -1
    #base case
    if len(element) == 1:
        return element[0]
    #recursion
    if element[0] < find_min(element[1:]):
        return element[0] 
    else:
        return (find_min(element[1:])) 
    pass


def sum_all(element):
    """TODO: complete for Step 2"""
    if element:
        for x in range(len(element)):
            if not isinstance(element[x],int):
                return -1
    else:
        return -1
    #base case
    if len(element) == 1:
        return element[0]
    #recursion
    return element[0] + sum_all(element[1:])
    pass


def find_possible_strings(character_set, n):
    """TODO: complete for Step 3"""
    if character_set:
        for x in range(len(character_set)):
            if not isinstance(character_set[x],str) or len(character_set[x]) != 1 or not n > 0:
                return []
    else:
        return []
    return find_all_possible(character_set,n,'',[])
    pass

def find_all_possible(character_set,n,word,list_of_combos):
    newword = ''
    count = 0
    #base case
    if n == 0:
        list_of_combos.append(word)
        return
    #recursion
    while count < len(character_set):
        newword = word + character_set[count]
        find_all_possible(character_set,n-1,newword,list_of_combos)
        count = count + 1
    return list_of_combos
    pass