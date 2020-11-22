# enz889 Enhan Zhao cmpt 145 assignment 2 test case

import numpy as np
import a2q1
test_case_check_sudoku = [
    {'inputs'  : np.array([[4, 7, 5, 1, 8, 9, 2, 3, 6],
                [2, 8, 3, 4, 6, 5, 1, 9, 7],
                [6, 9, 1, 2, 7, 3, 5, 4, 8],
                [9, 3, 2, 6, 5, 8, 7, 1, 4],
                [7, 4, 6, 9, 1, 2, 3, 8, 5],
                [1, 5, 8, 7, 3, 4, 9, 6, 2],
                [3, 2, 7, 8, 9, 6, 4, 5, 1],
                [8, 1, 9, 5, 4, 7, 6, 2, 3],
                [5, 6, 4, 3, 2, 1, 8, 7, 9]]) ,
     'outputs' : True,
     'reason'  : 'Checks a real 9x9 sudoku'},

    {'inputs'  : np.array([[4, 7, 5, 1, 8, 9, 2, 3, 6],
                [2, 8, 3, 4, 6, 5, 1, 9, 7],
                [6, 9, 1, 2, 7, 3, 5, 4, 8],
                [9, 3, 2, 6, 5, 8, 7, 1, 4],
                [7, 7, 7, 7, 7, 7, 7, 7, 7],
                [1, 5, 8, 7, 3, 4, 9, 6, 2],
                [3, 2, 7, 8, 9, 6, 4, 5, 1],
                [8, 1, 9, 5, 4, 7, 6, 2, 3],
                [5, 6, 4, 3, 2, 1, 8, 7, 9]]) ,
     'outputs' : False,
     'reason'  : 'Checks the row loop when a row does not contain ints 1 to 9 once each. row 5'},

    {'inputs'  : np.array([[4, 7, 5, 1, 8, 9, 2, 3, 6],
                [2, 8, 3, 4, 6, 5, 1, 9, 7],
                [6, 9, 1, 2, 7, 3, 5, 4, 8],
                [9, 3, 2, 6, 5, 8, 7, 1, 4],
                [7, 4, 6, 9, 1, 2, 3, 8, 5],
                [1, 5, 8, 7, 3, 4, 9, 6, 2],
                [3, 2, 7, 8, 9, 6, 4, 5, 1],
                [8, 1, 9, 5, 4, 7, 6, 2, 3],
                [9, 6, 4, 3, 2, 1, 8, 7, 5]]),
     'outputs' : False,
     'reason'  : 'Checks the column loop when a column does not contain int 1 to 9 once each. column 1'},

    {'inputs'  : np.array([[4, 7, 5, 1, 8, 9, 2, 3, 6],
                [2, 8, 3, 4, 6, 5, 1, 9, 7],
                [6, 9, 1, 2, 7, 3, 5, 4, 8],
                [9, 3, 2, 6, 5, 8, 7, 1, 4],
                [7, 4, 6, 9, 1, 2, 3, 8, 5],
                [1, 5, 8, 7, 3, 4, 9, 6, 2],
                [3, 2, 7, 8, 9, 6, 4, 5, 1],
                [8, 1, 9, 5, 4, 7, 6, 2, 3],
                [9, 6, 4, 3, 2, 1, 8, 7, 0]]),
     'outputs' : False,
     'reason'  : 'Checks the sum loop when values in a 3x3 square does not add up to 45'}
]


for t in test_case_check_sudoku:
    l = t['inputs']
    expected = t['outputs']

    # replace the len function with the function you want to test. Usually, you will need to import your aXqY file first.
    result = a2q1.check_sudoku(l)
    if result != expected:
        print('Error in check(): expected ', expected[0],
              ' but got ', result, '--', t['reason'])
