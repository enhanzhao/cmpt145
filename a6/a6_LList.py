#assignment 6 LList.py enz889 Enhan Zhao cmpt 145

# CMPT 145: Node-Based Data Structures
# Defines the Linked List ADT
#
# Here we re-invent Python's built-in lists.  We will provide a subset of
# the operations that a Python list provides.
#
# Implementation:
#   This implementation uses the linked node structure.

import node as node


def create():
    """
    Purpose
        creates an empty list
    Return
        :return an empty list
    """
    llist = {}
    llist['size'] = 0     # how many elements in the stack
    llist['head'] = None  # the node chain starts here; initially empty
    llist['tail'] = None
    return llist

def is_empty(alist):
    """
    Purpose
        Checks if the given list has no data in it
    Pre-conditions:
        :param alist: a list created by create()
    Return:
        :return True if the list has no data, or False otherwise
    """
    return alist["size"] == 0

def size(alist):
    """
    Purpose
        Returns the number of data values in the given list
    Pre-conditions:
        :param alist: a list created by create()
    Return:
        :return The number of data values in the list
    """
    return alist["size"]

def add_to_front(alist, val):
    """
    Purpose
        Insert val into alist at the front of the node chain
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
    Post-conditions:
        The list increases in size.
        The new value is at index 0.
        The values previously in the list appear after the new value.
    Return:
        :return None
    """
    new = node.create(val)
    if alist["head"] is None:
        alist["head"] = new
        alist["tail"] = new
    else:
        alist["head"] = node.create(val, alist["head"])
    alist["size"] += 1

def add_to_back(alist, val):
    """
    Purpose
        Insert val into alist at the end of the node chain
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
    Post-conditions:
        The list increases in size.
        The new value is last in the list.
    Return:
        :return None
    """
    new = node.create(val)
    if alist["tail"] is None:
        alist["head"] = new
        alist["tail"] = new
    else:
        node.set_next(alist["tail"], new)
        alist["tail"] = new
    alist["size"] += 1

def value_is_in(alist, val):
    """
    Purpose
        Check if the given value is in the given list
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
    Post-conditions:
        none
    Return:
        :return True if the value is in the list, False otherwise
    """
    if alist["head"] is None:         #if empty
        return False
    walker = alist["head"]
    while node.get_next(walker) is not None:
        value = node.get_data(walker)
        if value == val:
            return True
        walker = node.get_next(walker)
    value = node.get_data(walker)           #check last value
    if value == val:
        return True
    return False

def get_index_of_value(alist, val):
    """
    Purpose
        Return the smallest index of the given val in the given alist.
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
    Post-conditions:
        none
    Return:
        :return the tuple (True, idx) if the val appears in alist
        :return the tuple (False, None) if the vale does not appear in alist
    """
    if alist["head"] is None:         #if empty
        return False, None
    walker = alist["head"]
    index = 0
    while node.get_next(walker) is not None:
        value = node.get_data(walker)
        if value == val:
            return True, index
        walker = node.get_next(walker)
        index += 1
    value = node.get_data(walker)           #check last value
    if value == val:
        return True, index
    return False, None

def retrieve_data_at_index(alist, idx):
    """
    Purpose
        Return the value stored in alist at the index idx
    Preconditions:
        :param alist: a list created by create()
        :param idx:   a non-negative integer
    Post-conditions:
        none
    Return:
        :return (True, val) if val is stored at index idx and idx is valid
        :return (False, None) if the idx is not valid for the list
    """
    if alist["head"] is None or idx >= alist["size"]:
        return False, None
    index = 0
    walker = alist["head"]
    while index < idx:              #binds index 0 with item 1
        walker = node.get_next(walker)
        index += 1
    return True, node.get_data(walker)

def set_data_at_index(alist, idx, val):
    """
    Purpose
        Store val into alist at the index idx
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
        :param idx:   a non-negative integer
    Post-conditions:
        The value stored at index idx changes to val
    Return:
        :return True if the index was valid, False otherwise
    """
    if alist["head"] is None or idx >= alist["size"]:
        return False
    walker = alist["head"]
    index = 0
    while index < idx:
        walker = node.get_next(walker)
        index += 1
    node.set_data(walker, val)
    return True

def remove_from_front(alist):
    """
    Purpose
        Removes and returns the first value in alist
    Preconditions:
        :param alist: a list created by create()
    Post-conditions:
        The list decreases in size.
        The returned value is no longer in in the list.
    Return:
        :return The tuple (True, value) if alist is not empty
        :return The tuple (False, None) if alist is empty
    """
    if alist["head"] is None:
        return False, None
    val = node.get_data(alist["head"])
    if size(alist) is 1:
        alist["head"] = None
        alist["tail"] = None
    else:
        alist["head"] = node.get_next(alist["head"])
    alist["size"] -= 1
    return True, val

def remove_from_back(alist):
    """
    Purpose
        Removes and returns the last value in alist
    Preconditions:
        :param alist: a list created by create()
    Post-conditions:
        The list decreases in size.
        The returned value is no longer in in the list.
    Return:
        :return The tuple (True, value) if alist is not empty
        :return The tuple (False, None) if alist is empty
    """
    if alist["tail"] is None:
        return False, None
    val = node.get_data(alist["tail"])
    if size(alist) is 1:    #singleton
        alist["head"] = None
        alist["tail"] = None
        alist["size"] -= 1
        return True, val
    walker = alist["head"]
    count = 1
    while count < size(alist)-1:            #point walker to second last node
        walker = node.get_next(walker)
        count += 1
    node.set_next(walker, None)
    alist["tail"] = walker
    alist["size"] -= 1
    return True, val

def insert_value_at_index(alist, val, idx):
    """
    Purpose
        Insert val into alist at index idx
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
        :param idx:   a valid index for the list
    Post-conditions:
        The list increases in size.
        The new value is at index idx.
        The values previously in the list at idx or later appear after the new value.
    Return:
        :return If the index is valid, insert_value_at_index returns True.
        :return If the index is not valid, insert_value_at_index returns False.
    """
    if idx > alist["size"] or idx < 0:            #if index out of range
        return False
    new = node.create(val)
    if alist["head"] is None and idx is 0:           #if empty list
        add_to_front(alist, val)
        return True
    else:
        if idx is 0:                        #if add to front
            add_to_front(alist, val)
            return True
        if idx is size(alist):              #if add to rear: idx is the same as size
            add_to_back(alist, val)
            return True
    walker = node.get_next(alist["head"])
    previous = alist["head"]
    index = 1
    while True:                             #add in between
        if index == idx:
            node.set_next(previous, new)
            node.set_next(new, walker)
            alist["size"] += 1
            return True
        walker = node.get_next(walker)
        previous = node.get_next(previous)
        index += 1

def delete_item_at_index(alist, idx):
    """
    Purpose
        Delete the value at index idx in alist.
    Preconditions:
        :param alist: a list created by create()
        :param idx:   a non-negative integer
    Post-conditions:
        The list decreases in size if the index is valid
        The value at idx is no longer in the list.
    Return:
        :return True if index was valid, False otherwise
    """
    if idx >= alist["size"] or idx < 0:            #if index out of range
        return False
    if idx is 0:                            #if remove from front
        remove_from_front(alist)
        return True
    elif idx is size(alist) - 1:            #if remove from rear
        remove_from_back(alist)
        return True
    walker = node.get_next(alist["head"])              #all other cases
    previous = alist["head"]
    index = 1
    while True:
        if index == idx:
            node.set_next(previous, node.get_next(walker))
            alist["size"] -= 1
            return True
        walker = node.get_next(walker)
        previous = node.get_next(previous)
        index += 1



