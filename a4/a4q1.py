# a4q1 Enhan Zhao enz889    cmpt145


#Use stacks to reverse lines in file
#Use queues to get words in line
    #Use stacks to reverse letters in word


import TStack as s
import TQueue as q
# reverse_lines() and reverse_letters() takes a list and returns a list by using queues and stacks. This is better for testing.
def open_file(file):
    """
    Purpose: open a txt file and returns a list containing each line as str
    Preconditions:
    file: the name of a file
    Postconditions: none
    return: a list of strings
    """
    f = open(file, "r")
    file = []
    for line in f:
        file.append(line.rstrip())
    f.close()
    return file

def reverse_lines(list):
    """
    Purpose: reverse the item order in a list into a list through using a stack
    Preconditions:
    list: a list of strings
    Postconditions:
    return : a list of strings containing the items in stack in reverse order
    """

    line_stack = s.create()
    for line in list:  # push list items(line) into line stack
        s.push(line_stack, line.rstrip())
    line_reverse = []
    while s.is_empty(line_stack) == False:   #pop line stack and enqueue to list
        line = s.pop(line_stack)
        line_reverse.append(line)
    return line_reverse

def reverse_letters(list):
    """
    Purpose: reverse the order of letters in each word in a string from a list that already has lines reversed. order of words in a list is not affected
    Preconditions:
    queue: a list containing reversed lines as strings
    Postconditions:
    return : a list containing the items in reverse order
    """
    queue = q.create()
    for line in list:      #crate queue for line
        q.enqueue(queue, line)
    reverse_letter = q.create()        #initialize queue for line with word letters revresed
    while q.is_empty(queue) == False:
        line_queue = q.create()
        line = q.dequeue(queue)  #return each line

        for word in line.split():  # for each word in line: focus on 1 line
            letter_stack = s.create() #create stack for letters
            new = ""
            for letter in word:  # push each letter into letter_stack
                s.push(letter_stack, letter)
            while s.is_empty(letter_stack) == False:  #return each letter in reverse order and add to newword
                l = s.pop(letter_stack)
                new = new + l
            q.enqueue(line_queue, new + " ")  # enqueue reversed lines to line queue
            new_line = ""
        while q.is_empty(line_queue) == False:  #return each reversed line and add to new new queue
            n_line = q.dequeue(line_queue)
            new_line = new_line + n_line
        q.enqueue(reverse_letter, new_line)
    reverse_list = []
    while q.is_empty(reverse_letter) == False:      #dequeue each item into a list
        newline = q.dequeue(reverse_letter)
        reverse_list.append(newline)
    reverse_list = [x.rstrip() for x in reverse_list] #remove the right space in each line
    return reverse_list

def display_reversed(list):
    """
    Purpose: display reversed texts to console
    Preconditions:
    queue: a list of strings containing reversed lines and letter
    Postconditions:
    return: nothing
    """
    for line in list:
        print(line)




