#a5q3 enz889    Enhan Zhao cmpt145

import node as node
import a5q2 as a5q2


def contains_duplicates(node_chain):
    """
    Purpose:
        Returns whether or not the given node_chain contains one or more duplicate data values.
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty
    Return:
        :return: True if duplicate data value(s) were found, False otherwise
    """
    if node_chain == None or node.get_next(node_chain) == None:
        return False

    anode = node_chain
    values = []  # store values in a list
    while node.get_next(anode) != None:
        this_data = node.get_data(anode)
        if this_data in values:         #check if current data is in list
            return True
        anode = node.get_next(anode)
        values.append(this_data)
    if node.get_data(anode) in values:  # check last node
        return True
    return False



def reverse_chain(node_chain):
    """
    Purpose:
        Completely reverses the order of the given node_chain.
    Pre-conditions:
        :param node_chain: a node chain, possibly empty
    Post-conditions:
        The front of the node_chain is altered to be the back, with all nodes now pointing next the opposite direction.
    Return:
        :return: The resulting node chain that has had its order reversed
    """
    if node_chain == None:
        return None
    if node.get_next == None:  # only 1 data, return node chain
        return node_chain
    anode = node_chain
    new_node = node.create(node.get_data(anode))  # end of new node
    while node.get_next(anode) != None:  # step through original and create new node in reverse
        new_node = node.create(node.get_data(node.get_next(anode)), new_node)
        anode = node.get_next(anode)
    return new_node




def insert_value_sorted(node_chain, number_value):
    """
    Purpose:
        Insert the given number_value into the node-chain so that it appears after a previous value that is <= value. If the node_chain was empty, new value is simply placed at the front.
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty, containing only numbers
        :param number_value: a numerical value to be inserted
        Assumption:  node_chain only contains numbers (which can be compared to the given number_value)
    Post-condition:
        The node-chain is modified to include a new node with number_value as its data after a previous node's data value is <= number_value.
    Return
        :return: the node-chain with the new value in it
    """
    if node_chain == None:
        return node.create(number_value)
#1 node
    anode = node_chain
    current = node.get_data(anode)
    if number_value <= current:  #add to front, regardless of node size
        return node.create(number_value, anode)
    if node.get_next(anode) == None:    #add after
        node.set_next(anode, node.create(number_value))
        return anode
#2 nodes
    next1 = node.get_data(node.get_next(anode))
    if node.get_next(node.get_next(anode)) == None:
        if number_value <= next1:      #add in middle
            node.set_next(anode, node.create(number_value, node.get_next(anode)))
            return anode
        if number_value > next1:
            node.set_next(node.get_next(anode), node.create(number_value))
            return anode
#3+
    next1 = node.get_data(node.get_next(anode))
    while node.get_next(node.get_next(anode)) != None:                 #step until the second last one
        if number_value > current and number_value <= next1:          #if larger than current and smaller than next
            node.set_next(anode, node.create(number_value, node.get_next(anode)))
            return node_chain
        anode = node.get_next(anode)
        current = node.get_data(anode)
        next1 = node.get_data(node.get_next(anode))
    if number_value <= next1:        #check last 2 values
        node.set_next(anode, node.create(number_value, node.get_next(anode)))
        return node_chain
    node.set_next(node.get_next(anode), node.create(number_value))
    return node_chain



