#a7q5.py enz889 Enhan Zhao cmpt145

#a Fibonacci sequence

def find_fib(n):
    """
    Purpose: to find the n th fibonacci number based on its sequence.
    Pre-conditions: n : the nth fibonacci number to be found
    Post-conditions: None
    return the nth fibonacci number
    """
    assert n >= 0, "invalid input, must be positive int"
    if n == 0:          #base case 1
        return 0
    elif n == 1:        #base case 2
        return 1
    else:               #recursive case
        return find_fib(n - 1) + find_fib(n-2)

#b moosonacci sequence

def find_moo(n):
    """
        Purpose: to find the n th moosonacci number based on its sequence.
        Pre-conditions: n : the nth moosonacci number to be found
        Post-conditions: None
        return the nth moosonacci number
    """
    assert n >= 0, "invalid input, must be positive int"
    if n == 0:      #base case 1
        return 0
    elif n == 1:    #base case 2
        return 1
    elif n == 2:    #base case 3
        return 2
    else:
        return find_moo(n-1) + find_moo(n-2) + find_moo(n-3)

#c substr

def substr(s, c, r):
    """
    Purpose: replace target character in string with replacement character, using recursion
    Pre-conditions:
    s: a string
    c: a target character
    r: a replacement character
    Post-conditions: c in s is substituted by r
    return: modified s
    """
    #task: replace target with replacement value
    #sub task: dont index, check previous
    #return: concatenation of subtasks
    if s == "":         #base case
        return ""
    if s[0] == c:       #recursive conditional: if match
        return r + substr(s[1:], c, r)
    return s[0] + substr(s[1:], c, r)   #if does not match




