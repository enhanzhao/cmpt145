#a9q2_Container enz889 Enhan Zhao cmpt145

import Node

class Container(object):
    def __init__(self):
        '''
        Purpose: initialize a superclass for container like data structures
        '''
        self.count = 0
        self.head = None

    def size(self):
        '''
        Purpose: return the size of the container
        :return: the size/number of items in the container
        '''
        return self.count

    def is_empty(self):
        '''
        Purpose: determine if the container is empty or not
        :return: True if empty, False if not empty
        '''
        return self.count == 0

    def peek(self):
        '''
        Purpose: return the data value at the front of the queue
        :return: the data at the front of the queue
        '''
        assert self.count > 0, "peeked an empty stack"
        return self.head.get_data()

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
            walker = self.head
            value = walker.get_data()
            result = '[ ' + str(value) + ' |'
            while walker.get_next() is not None:
                walker = walker.get_next()
                value = walker.get_data()
                result += ' *-]-->[ ' + str(value) + ' |'
            result += ' / ]'
        return result

