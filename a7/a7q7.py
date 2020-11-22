#a7q7 enz889 Enhan Zhao cmpt145


#a
def marioCount(a, b):
    """
    Purpose: find the number of shortest paths mario can take in a room ab
    Preconditions:
    a: width of room
    b: length of room
    Postconditions: nothing
    return: the number of shortest paths available
    """
    if a == 1 or b == 1: #base case
        return 1
    else:                   #recursive case
        return marioCount(a-1, b) + marioCount(a, b-1)
#b
print(marioCount(3, 3))
print(marioCount(4, 4))
print(marioCount(10, 12))