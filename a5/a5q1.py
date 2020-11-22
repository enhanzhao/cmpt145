#a5q1 Enhan Zhao enz889 cmpt 145

import node as node

def to_string(node_chain):
    """
    Purpose:
        Create a string representation of the node chain.  E.g.,
        [ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]
    Pre-conditions:
        :param node_chain:  A node-chain, possibly empty
    Post_conditions:
        None
    Return: A string representation of the nodes.
    """
    # special case: empty node chain
    if node_chain == None:  #added return here so rest of the code wont be executed
        return 'EMPTY'
    walker = node_chain
    value = node.get_data(walker)
    result = '[ ' + str(value) + ' |'
    while node.get_next(walker) != None:         #Heres the bug, didnt index dictionary
        walker = node.get_next(walker)
        value = node.get_data(walker)
    # represent the next with an arrow-like figure
        result += ' *-]-->[ '+str(value)+' |'
    # at the end of the chain, use '/'
    result += ' / ]'
    return result

