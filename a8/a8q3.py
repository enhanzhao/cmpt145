#a8q3 enz889 Enhan Zhao cmpt145

import treenode as tn
import treefunctions as tf

def complete(tnode):
    """ Purpose: Determine if the given tree is complete.
    Pre-conditions:
    :param tnode: a primitive binary tree
    :return: A tuple (True, height) if the tree is complete, A tuple (False, None) otherwise.
    """
    if tnode is None:
        return False, None
    if tf.is_leaf(tnode) is True:      #base 1: if leaf
        return True, 1
    elif tn.get_left(tnode) is None or tn.get_right(tnode) is None:     #base 2: if incomplete
        return False, None
    left_flag, left_height = complete(tn.get_left(tnode))       #check left side first
    if left_flag is False:
        return False, None
    right_flag, right_height = complete(tn.get_right(tnode))        #check right side first
    if right_flag is False:
        return False, None
    if left_height == right_height:     #if height is equal, then tree is complete
        return True, left_height +1

