#a9q2_Stack enz889 Enhan Zhao cmpt145

import a9q2_Container as c
import Node

class Stack(c.Container):
    def __init__(self):
        '''
        Purpose: initialize the subclass stack under the container super class
        '''
        c.Container.__init__(self)

    def push(self, value):
        """
        Purpose: Add a value to stack object. Increase the size of stack by 1.
        Preconditions:
        :param value: a value to be added
        Postconditions: new value added, size increased, and top changed to the new value
        :return: None
        """
        new = Node.Node(value, self.head)
        self.head = new
        self.count += 1

    def pop(self):
        """
        Purpose: Remove and return the value at the top of the stack.
        Postconditions: top of stack deleted, returned and stack size decreased
        :return: value at the top of the stack
        """
        assert self.count > 0, "popped an empty stack"
        prev_top = self.head
        result = prev_top.get_data()
        self.head = prev_top.get_next()
        self.count -= 1
        return result


