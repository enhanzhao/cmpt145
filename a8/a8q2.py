#a8q2 enz889 Enhan Zhao cmpt145

import treenode as tn
import treefunctions as tf

def mirrored(t1, t2):
    """
    Purpose: checks if 2 binary trees satisfy the mirror property
    preconditions:
    :param t1: a tree
    :param t2: a tree that might mirror t1
    postconditions: none
    :return: True if the 2 trees are mirrors of each other, False otherwise
    """
    if t1 is None and t2 is None: #if both are None, return True
        return True
    if t1 is None or t2 is None:  #if 1 is None, return False
        return False
    return tn.get_data(t1) == tn.get_data(t2) and mirrored(tn.get_left(t1), tn.get_right(t2)) and mirrored(tn.get_right(t1), tn.get_left(t2)) #compare data, and the rest

def reflect(tnode):
    """
    Purpose: swap every left and right sub tree in a tree
    preconditions:
    :param tnode: a tree
    postconditions: left and right in tree and sub tree swapped
    :return: nothing
    """
    if tnode is None or tf.is_leaf(tnode) is True:      #base: do nothing if end
        return
    left = tn.get_left(tnode)
    right = tn.get_right(tnode)
    tn.set_left(tnode, right)       #swap left and right.
    tn.set_right(tnode, left)
    reflect(tn.get_left(tnode))
    reflect(tn.get_right(tnode))

def reflection(tnode):
    """
    Purpose: create a new tree that is the mirror of the original
    precoditions:
    :param tnode: a tree
    Postconditions: a new object is created
    :return: the new tree that is the mirror of the original
    """
    if tnode == None:
        return
    if tf.is_leaf(tnode) is True:
        return tn.create(tn.get_data(tnode))
    mirrored = tn.create(tn.get_data(tnode))  # recursive: set left and right to right and left of tnode
    tn.set_left(mirrored, reflection(tn.get_right(tnode)))
    tn.set_right(mirrored, reflection(tn.get_left(tnode)))
    return mirrored

