#a8q4 enz889 Enhan Zhao cmpt145

import treenode as tn
import treefunctions as tf

def path_to(tnode, value):
    """
    Purpose: to determine if value is found in a tree and return a list with the path to that value from root
    Preconditions:
    :param tnode: a tree
    :param value: a value to find
    :return: tuple (True, alist) if found, (False, None) if not found
    """
    if tnode is None:
        return False, None
    this_node = tn.get_data(tnode) #base
    if this_node == value:      #if match
        return True, [this_node]
    #recursive
    left, left_value = path_to(tn.get_left(tnode), value)
    if left:
        return True, left_value + [tn.get_data(tnode)]
    right, right_value = path_to(tn.get_right(tnode), value)
    if right:
        return True, right_value + [tn.get_data(tnode)]
    return False, None

def find_path(tnode, val1, val2):
    """
    Purpose: construct a path from one node in a tree to another node in a tree
    :param tnode: a tree with all unique data.
    :param val1: the start value
    :param val2: the finish value
    :return: a tuple (bool - if both values found, alist (the path from val1 to val2))
    """
    if tnode is None:
        return None
    v1boo, path1 = path_to(tnode, val1)
    v2boo, path2 = path_to(tnode, val2)
    if v1boo is False or v2boo is False:
        return None
    common_count = 0        #find common values in both path from root
    for i in path1:
        if i in path2:
            common_count += 1
    if common_count == 1:    #then values are from different sub trees. append reversed path 2 minus common to path1
        path2.reverse()
        path2 = path2[1:]
        path1.extend(path2)
        return path1
    if common_count > 1: #then values are from the same sub tree. eliminate common
        while common_count > 1:
            path1.pop()
            path2.pop()
            common_count -= 1
        path2.reverse()
        path2 = path2[1:]
        return path1 + path2


