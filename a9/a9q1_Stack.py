#a9q1_Stack Enhan Zhao enz889 cmpt145
import Node
class Stack(object):
    def __init__(self):
        '''
        Purpose: initialize the stack data structure as a class
        '''
        self.count = 0
        self.top = None


    def size(self):
        """
        Purpose: Return the size of the stack object as an int.
        :return: the size of the stack
        """
        return self.count

    def is_empty(self):
        """
        Purpose: Returns Boolean based on if the stack object is empty.
        :return: True if empty, False if not empty
        """
        return self.count == 0

    def push(self, value):
        """
        Purpose: Add a value to stack object. Increase the size of stack by 1.
        Preconditions:
        :param value: a value to be added
        Postconditions: new value added, size increased, and top changed to the new value
        :return: None
        """
        new = Node.Node(value, self.top)
        self.top = new
        self.count += 1

    def pop(self):
        """
        Purpose: Remove and return the value at the top of the stack.
        Postconditions: top of stack deleted, returned and stack size decreased
        :return: value at the top of the stack
        """
        assert self.count > 0, "popped an empty stack"
        prev_top = self.top
        result = prev_top.get_data()
        self.top = prev_top.get_next()
        self.count -= 1
        return result

    def peek(self):
        """
        Purpose: Returns the top of the stack.
        :return: Nothing
        """
        assert self.count > 0, "peeked an empty stack"
        first_node = self.top
        data = first_node.get_data()
        return data

    def to_string(self):
        """
        Purpose:
        Create a string representation of the Stack.  E.g.,
        [ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]
        where 1 is the top of the stack and 3 is the end of the stack
    Pre-conditions:
        :param stack:  A node-based Stack, possibly empty
    Post_conditions:
        None
    Return: A string representation of the stack.
        :return:
        """
        if self.count == 0:
            result = 'EMPTY'
        else:
            walker = self.top
            value = walker.get_data()
            result = '[ ' + str(value) + ' |'
            while walker.get_next() is not None:
                walker = walker.get_next()
                value = walker.get_data()
                result += ' *-]-->[ ' + str(value) + ' |'
            result += ' / ]'
        return result



