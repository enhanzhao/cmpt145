#a7q6 enz889 Enhan Zhao cmpt145

#a to_string()
import node

def to_string(node_chain):
    """
    purpose: represent a node chain using string notation.
    Preconditions:
    node_chain: a node chain
    post-conditions: none
    return: a string that represent the node chain
    """
    if node_chain == None:      #empty chain
        return "EMPTY"
    if node.get_next(node_chain) == None:     #single node
        return '[ ' + str(node.get_data(node_chain)) + ' |' + ' / ]'
    else:               #more than 1 nodes
        return '[ ' + str(node.get_data(node_chain)) + ' | * -]-->' + to_string(node.get_next(node_chain))


def copy(node_chain):
    """
    purpose: create a new node chain that is identical to node_chain
    Preconditions:
    node_chain: a node chain
    post-conditions: an identical node chain is created
    return: the newly created node chain
    """
    if node_chain == None:
        return None
    if node.get_next(node_chain) == None:       #base case, 1 node
        return node.create(node.get_data(node_chain))
    else:
        value = node.get_data(node_chain)
        return node.create(value, copy(node.get_next(node_chain)))


def replace(node_chain, target, replacement):
    """
    purpose: replace data in node chain if data matches target
    Preconditions:
    node_chain: a node chain
    post-conditions: data in node chain possibly altered
    return: reference to the node_chain
    """
    if node_chain == None:
        return None
    if node.get_next(node_chain) == None:       #base case
        if node.get_data(node_chain) == target:
            node.set_data(node_chain, replacement)
        return node_chain
    if node.get_data(node_chain) == target:
        node.set_data(node_chain, replacement)
        replace(node.get_next(node_chain), target, replacement)
    else:
        replace(node.get_next(node_chain), target, replacement)
    return node_chain

