#a8q1.py enz889 Enhan Zhao  cmpt145

import treenode as tn
import treefunctions as tf
import TQueue as Q

def count_node_types(tnode):
    """
    Purpose: count the number of leaf nodes and non-leaf nodes in a tree.
    Preconditions
    :param tnode: a tree node
    Postconditions: nothing
    :return: a tuple(# leaf, # non-leaf)
    """
    if tnode == None:
        return (0, 0)
    leaf_count = 0
    root_count = 0
    if tf.is_leaf(tnode) is True:     #base case, 1 leaf
        return (leaf_count + 1, root_count)
    else:           #recursive case
        leaf_count += count_node_types(tn.get_left(tnode))[0] + count_node_types(tn.get_right(tnode))[0]
        root_count += (count_node_types(tn.get_left(tnode))[1] + count_node_types(tn.get_right(tnode))[1]) + 1
    return (leaf_count, root_count)

def subst(tnode, t, r):
    """
    Purpose: replace target value with replacement value in a tree
    Preconditions:
    :param tnode: a tree
    :param t: target value
    :param r: replacement value
    Postconditions: values are replaced, if match
    :return: None
    """
    if tnode == None:
        return None
    if tf.is_leaf(tnode) is True:       #base
        if tn.get_data(tnode) == t:
            tn.set_data(tnode, r)
    if tn.get_data(tnode) == t:
        tn.set_data(tnode, r)
    subst(tn.get_left(tnode), t, r)
    subst(tn.get_right(tnode), t, r)

def copy(tnode):
    """
    Purpose: create a new object that is the same as tnode
    Preconditions:
    :param tnode: a tree
    Postconditions: a new object created, tnode not changed
    :return: reference to the newly created tree
    """
    if tnode == None:
        return None
    if tf.is_leaf(tnode) is True:       #base: if leaf, create tree with data
        return tn.create(tn.get_data(tnode))
    new_tree = tn.create(tn.get_data(tnode))        #recursive: set left and right to copy() child
    tn.set_left(new_tree, copy(tn.get_left(tnode)))
    tn.set_right(new_tree, copy(tn.get_right(tnode)))
    return new_tree

def nodes_at_level(tnode, level):
    """
    Purpose: count how many nodes are at the given level of a tree.
    Preconditions:
    :param tnode: a tree
    :param level: the level to be counted
    postconditions: none
    :return: the number of nodes at the level, 0 if invalid
    """
    if tnode is None:
        return 0
    if level == 0:  #base: if we are on the level we want, each node is 1. level is a counter
        return 1
    return nodes_at_level(tn.get_left(tnode), level - 1) + nodes_at_level(tn.get_right(tnode), level -1) #recursive: traverse through tree until level is 0.


