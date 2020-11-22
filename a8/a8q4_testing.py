#a8q4_testing enz889 Enhan Zhao cpt145

import treenode as tn
import a8q4
#test path_to()###############################################
path_to = [
    {'inputs'  : [None, 1],
     'outputs' : (False, None),
     'reason'  : 'empty tree'},

    {'inputs'  : [tn.create(1), 1],
     'outputs' : (True, [1]),
     'reason'  : 'singleton tree'},

    {'inputs'  : [tn.create(1, tn.create(2)), 2],
     'outputs' : (True, [2, 1]),
     'reason'  : 'simple tree left'},

    {'inputs'  : [tn.create(1, None, tn.create(2)), 2],
     'outputs' : (True, [2, 1]),
     'reason'  : 'simple tree right'},

    {'inputs'  : [tn.create(1, tn.create(2, tn.create(4), tn.create(5)), tn.create(3, tn.create(6), tn.create(7))), 7],
     'outputs' : (True, [7, 3, 1]),
     'reason'  : 'complex tree 1'},

    {'inputs'  : [tn.create(1, tn.create(2, tn.create(4), tn.create(5)), tn.create(3, None, tn.create(6, tn.create(7), tn.create(9)))), 7],
     'outputs' : (True, [7, 6, 3, 1]),
     'reason'  : 'complex tree 2'},
]
for t in path_to:
    inputs = t['inputs']
    expected = t['outputs']
    result = a8q4.path_to(inputs[0], inputs[1])
    if result != expected:
        print('Error in path_to(): expected ', expected,
              ' but got ', result, '--', t['reason'])

#test find_path()#
find_path = [
    {'inputs'  : [None, 1, 1],
     'outputs' : None,
     'reason'  : 'empty tree'},

    {'inputs'  : [tn.create(1), 1, 1],
     'outputs' : [1],
     'reason'  : 'singleton tree'},

    {'inputs'  : [tn.create(1), 0, 1],
     'outputs' : None,
     'reason'  : 'singleton tree not found'},

    {'inputs'  : [tn.create(1, tn.create(2)), 2, 1],
     'outputs' : [2, 1],
     'reason'  : 'simple tree left found'},

    {'inputs'  : [tn.create(1, None, tn.create(2)), 2, 1],
     'outputs' : [2, 1],
     'reason'  : 'simple tree right found'},

    {'inputs'  : [tn.create(1, tn.create(2, tn.create(4), tn.create(5)), tn.create(3, tn.create(6), tn.create(7))), 4, 7],
     'outputs' : [4, 2, 1, 3, 7],
     'reason'  : 'complex tree 1 found'},

    {'inputs'  : [tn.create(1, tn.create(2, tn.create(4), tn.create(5)), tn.create(3, tn.create(6), tn.create(7))), 3, 4],
     'outputs' : [3, 1, 2, 4],
     'reason'  : 'complex tree 1 found, right to left'},

    {'inputs'  : [tn.create(1, tn.create(2, tn.create(4), tn.create(5, tn.create(8))), tn.create(3, tn.create(6), tn.create(7, tn.create(9)))), 8, 9],
     'outputs' : [8, 5, 2, 1, 3, 7, 9],
     'reason'  : 'complex tree 2 found'},

    {'inputs'  : [tn.create(1, tn.create(2, tn.create(4), tn.create(5, tn.create(8))), tn.create(3, tn.create(6), tn.create(7, tn.create(9)))), 9, 0],
     'outputs' : None,
     'reason'  : 'complex tree 2 not found, right to left'},
]
for t in find_path:
    inputs = t['inputs']
    expected = t['outputs']
    result = a8q4.find_path(inputs[0], inputs[1], inputs[2])
    if result != expected:
        print('Error in find_path(): expected ', expected,
              ' but got ', result, '--', t['reason'])
print("***End of testing***")