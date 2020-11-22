# enz889 Enhan Zhao cmpt 145 assignment 2


def read_file(txtfile):
    """
    purpose: reads a txt document containing 9 rows of 9 intergers into an array
    txtfile: a text file that contains 9 rows of 9 intergers
    post condition: nothing
    returns: a 2d array of 9x9 int
    """
    import numpy as np
    f = open(txtfile, 'r')
    s_list = []
    for line in f:
        s_list.append([int(x) for x in line.split()])
    s_list2 = [x for x in s_list if x != []]
    sudoku = np.array(s_list2)
    shape = sudoku.shape
    f.close()
    if shape != (9, 9):
        print("This file is not 9x9.")
    else:
        return sudoku


def check_sudoku(array9x9):
    """
    Purpose: checks if an array of intergers is a sudoku, with each row, column and 3x3 block containing 1 to 0 exactly once
    :param array9x9: an aray of 9x9 intergers
    :return: Boolean value based if input is a true Sudoku
    """
    for row in array9x9:   #check rows
        for i in range(len(row)):
            for ic in range(len(row)):
                if i != ic:
                    if row[i] == row[ic]:
                        print("No")
                        return False
    for col in array9x9.T:    #check columns
        for i in range(len(col)):
            for ic in range (len(col)):
                if i != ic:
                    if col[i] == col[ic]:
                        print("No")
                        return False
    sqr = []     #check squares
    sqr1 = array9x9[0:3, 0:3].sum()
    sqr2 = array9x9[0:3, 3:6].sum()
    sqr3 = array9x9[0:3, 6:9].sum()
    sqr4 = array9x9[3:6, 0:3].sum()
    sqr5 = array9x9[3:6, 3:6].sum()
    sqr6 = array9x9[3:6, 6:9].sum()
    sqr7 = array9x9[6:9, 0:3].sum()
    sqr8 = array9x9[6:9, 3:6].sum()
    sqr9 = array9x9[6:9, 6:9].sum()
    sqr.extend([sqr1, sqr2, sqr3, sqr4, sqr5, sqr6, sqr7, sqr8, sqr9])
    for i in sqr:
        if i != 45:
            print("No")
            return False
    print("Yes")
    return True

#sudoku = read_file(input("please enter file name with .txt extension:"))
#check_sudoku(sudoku)
