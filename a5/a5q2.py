# CMPT 145: Assignment 5 Question 2

import node as node



def count_chain(node_chain):
    """
    Purpose:
        Counts the number of nodes in the node chain.
    Pre-conditions:
        :param node_chain: a node chain, possibly empty
    Return:
        :return: The number of nodes in the node chain.
    """
    if node_chain == None:
        return 0
    count = 1
    anode = node_chain
    while node.get_next(anode)!= None:
        anode = node.get_next(anode)
        count += 1
    return count


def delete_front_nodes(node_chain, n):
    """
    Purpose:
        Deletes the first n nodes from the front of the node chain.
    Pre-Conditions:
        :param node_chain: a node-chain, possibly empty
        :param n: integer, how many nodes that should be removed off the front of the node chain
    Post-conditions:
        The node-chain is changed, by removing the first n nodes. If n>length of node_chain, node_chain is set to be empty (None)
    Return:
        :return: The resulting node chain, which may now be empty (None)
    """
    if node_chain == None or n >= count_chain(node_chain):
        return None
    if n == 0:
        return node_chain
    count = 0
    while count < n:
        node_chain = node.get_next(node_chain)
        count += 1
    return node_chain



def replace_last(node_chain, target_val, replacement_val):
    """
    Purpose:
        Replaces the last occurrence of target data value with the new_value. The chain should at most have 1 data value changed.
    Pre-conditions:
        :param node_chain: a node chain, possibly None
        :param target_val: the target data value we are searching to replace the last instance of
        :param replacement_val: the data value to replace the target_val that we found
    Post-conditions:
        The node-chain is changed, by replacing the last occurrence of target_val. If target_val is not present, then the node_chain returns unaltered.
    Return:
        :return: The altered node chain where any data occurrences of target_val has been replaced with replacement_val.
    """
    if node_chain == None:
        return None
    anode = node_chain #step through all nodes but last
    target_node = None
    while node.get_next(anode) != None:    #referece the node with matching value while stepping through all nodes
        if node.get_data(anode) == target_val:
            target_node = anode
        anode = node.get_next(anode)
    if node.get_data(anode) == target_val:   #check last node
        target_node = anode

    if target_node == None:   #if no match, return list
        return node_chain
    else:               #if found, replace and return
        node.set_data(target_node, replacement_val)   #if found, replace and return
        return node_chain


