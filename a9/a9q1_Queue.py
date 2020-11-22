#a9q1_Queue Enhan Zhao enz889 cmpt145

import Node

class Queue(object):
    def __init__(self):
        '''
            Purpose: initialize the queue data structure as a class
        '''
        self.count = 0
        self.front = None
        self.back = None

    def size(self):
        """
        Purpose: returns the number of data values in the given queue
        Return: The number of data values in the queue
        """
        return self.count

    def is_empty(self):
        """
        Purpose: check if the queue has no data in it.
        :return: True if queue is empty, False other wise
        """
        return self.count == 0

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
            self.front = new_node
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
        prev_first_node = self.front
        result = prev_first_node.get_data()
        self.front = prev_first_node.get_next()
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
        return self.front.get_data()

    def to_string(self):
        """
            Purpose:
                Create a string representation of the Queue.  E.g.,
                [ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]
                where 1 is the front of the queue and 3 is the back of the queue
            Pre-conditions:
                :param queue:  A node-based Queue, possibly empty
            Post_conditions:
                None
            Return: A string representation of the queue.
            """
        # special case: empty queue
        if self.count == 0:
            result = 'EMPTY'
        else:
            walker = self.front
            value = walker.get_data()
            result = '[ ' + str(value) + ' |'
            while walker.get_next() is not None:
                walker = walker.get_next()
                value = walker.get_data()
                result += ' *-]-->[ ' + str(value) + ' |'
            result += ' / ]'
        return result

