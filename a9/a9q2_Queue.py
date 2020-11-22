#a9q2_Queue enz889 Enhan Zhao cmpt145

import a9q2_Container as c
import Node

class Queue(c.Container):
    def __init__(self):
        '''
        Purpose: initialize the subclass queue under the container super class
        '''
        c.Container.__init__(self)
        self.back = None

    def enqueue(self, value):
        '''
        Purpose: add a value to the front of the node data structure.
        Preconditions:
        value: the value to be added
        Postconditions: back of queue changed, size of queue increased
        :return: nothing
        '''
        new_node = Node.Node(value)
        if self.count == 0:
            self.head = new_node
            self.back = new_node
        else:
            prev_last_node = self.back
            prev_last_node.set_next(new_node)
            self.back = new_node
        self.count += 1

    def dequeue(self):
        '''
        Purpose: delete and return the value at the front of the queue data structure.
        Postconditions: front of queue deleted, returned, size decreased
        :return: the value at front of queue
        '''
        assert self.count > 0, "dequeued from an empty stack"
        prev_first_node = self.head
        result = prev_first_node.get_data()
        self.head = prev_first_node.get_next()
        self.count -= 1
        if self.count == 0:
            self.back = None
        return result

    def peek(self):
        '''
        Purpose: return the data value at the front of the queue
        :return: the data at the front of the queue
        '''
        assert self.count > 0, "peeked an empty stack"
        return self.head.get_data()


