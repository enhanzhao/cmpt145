#a8q1_testing.py enz889 Enhan Zhao  cmpt145

import a8q1
import treenode as tn


#test count_node_types()###############################################
count_node = [
    {'inputs'  : None,
     'outputs' : (0, 0),
     'reason'  : 'empty tree'},

    {'inputs'  : tn.create(1),
     'outputs' : (1, 0),
     'reason'  : 'singleton tree'},

    {'inputs'  : tn.create(1, tn.create(2, tn.create(3))),
     'outputs' : (1, 2),
     'reason'  : 'tree with only left child'},

    {'inputs'  : tn.create(1, None, tn.create(2, None, tn.create(3))),
     'outputs' : (1, 2),
     'reason'  : 'tree with only right child'},

    {'inputs'  : tn.create(1, tn.create(2, tn.create(4, tn.create(6)), tn.create(5)), tn.create(3, tn.create(7))),
     'outputs' : (3, 4),
     'reason'  : 'tree with assorted children'},
]
for t in count_node:
    inputs = t['inputs']
    expected = t['outputs']
    result = a8q1.count_node_types(inputs)
    if result != expected:
        print('Error in count_node_types(): expected ', expected,
              ' but got ', result, '--', t['reason'])
#test subst()###############################################
subst = [
    {'inputs'  : [None, 1, 0],
     'outputs' : None,
     'reason'  : 'empty tree'},

    {'inputs'  : [tn.create(1), 1, 0],
     'outputs' : tn.create(0),
     'reason'  : 'singleton tree changed'},

    {'inputs'  : [tn.create(1), 2, 0],
     'outputs' : tn.create(1),
     'reason'  : 'singleton tree unchanged'},

    {'inputs'  : [tn.create(1, tn.create(1, tn.create(2), tn.create(2)), tn.create(1, tn.create(2), tn.create(2))), 2, 0],
     'outputs' : tn.create(1, tn.create(1, tn.create(0), tn.create(0)), tn.create(1, tn.create(0), tn.create(0))),
     'reason'  : 'only leaves are changed'},

    {'inputs'  : [tn.create(1, tn.create(1, tn.create(2), tn.create(2)), tn.create(1, tn.create(2), tn.create(2))), 1, 0],
     'outputs' : tn.create(0, tn.create(0, tn.create(2), tn.create(2)), tn.create(0, tn.create(2), tn.create(2))),
     'reason'  : 'only non-leaf nodes are changed'},

    {'inputs'  : [tn.create(1, tn.create(1, tn.create(1, tn.create(1)), tn.create(1)), tn.create(1, tn.create(1))), 1, 0],
     'outputs' : tn.create(0, tn.create(0, tn.create(0, tn.create(0)), tn.create(0)), tn.create(0, tn.create(0))),
     'reason'  : 'every value is changed, complex tree'},

    {'inputs'  : [tn.create(1, tn.create(1, tn.create(1, tn.create(1)), tn.create(1)), tn.create(1, tn.create(1))), 8, 0],
     'outputs' : tn.create(1, tn.create(1, tn.create(1, tn.create(1)), tn.create(1)), tn.create(1, tn.create(1))),
     'reason'  : 'no values changed, complex tree'},

    {'inputs'  : [tn.create(0, tn.create(1, tn.create(1, tn.create(1)), tn.create(1)), tn.create(1, tn.create(1))), 0, 9],
     'outputs' : tn.create(9, tn.create(1, tn.create(1, tn.create(1)), tn.create(1)), tn.create(1, tn.create(1))),
     'reason'  : 'only first parent is changed'},

]
for t in subst:
    inputs = t['inputs']
    expected = t['outputs']
    a8q1.subst(inputs[0], inputs[1], inputs[2])
    changed_tree = inputs[0]
    if changed_tree != expected:
        print('Error in subst(): expected ', expected,
              ' but got ', changed_tree, '--', t['reason'])


#test copy()###############################################
copy = [{'inputs': tn.create(1),
     'outputs': tn.create(1),
     'reason': 'singleton tree'},

    {'inputs': tn.create(1, tn.create(2, tn.create(3))),
     'outputs': tn.create(1, tn.create(2, tn.create(3))),
     'reason': 'tree with only left child'},

    {'inputs': tn.create(1, None, tn.create(2, None, tn.create(3))),
     'outputs': tn.create(1, None, tn.create(2, None, tn.create(3))),
     'reason': 'tree with only right child'},

    {'inputs': tn.create(1, tn.create(2, tn.create(4, tn.create(6)), tn.create(5)), tn.create(3, tn.create(7))),
     'outputs': tn.create(1, tn.create(2, tn.create(4, tn.create(6)), tn.create(5)), tn.create(3, tn.create(7))),
     'reason': 'tree with assorted children'},

]
for t in copy:
    inputs = t['inputs']
    expected = t['outputs']
    copied = a8q1.copy(inputs)
    if copied != expected or copied is inputs:      #must be same data but different reference
        print('Error in copy(): expected ', expected,
              ' but got ', copied, '--', t['reason'])

#test nodes_at_level()###############################################
nodes_at_level = [
    {'inputs'  : [None, 1],
     'outputs' : 0,
     'reason'  : 'empty tree'},

    {'inputs'  : [tn.create(1), 0],
     'outputs' : 1,
     'reason'  : 'singleton tree'},

    {'inputs': [tn.create(1), 8],
     'outputs': 0,
     'reason': 'singleton tree out of range'},

    {'inputs'  : [tn.create(1, tn.create(2, tn.create(3))), 2],
     'outputs' : 1,
     'reason'  : 'tree with only left child'},

    {'inputs'  : [tn.create(1, None, tn.create(2, None, tn.create(3))), 2],
     'outputs' : 1,
     'reason'  : 'tree with only right child'},

    {'inputs'  : [tn.create(1, tn.create(2, tn.create(4, tn.create(6)), tn.create(5)), tn.create(3, tn.create(7))), 2],
     'outputs' : 3,
     'reason'  : 'tree with assorted children'},
]
for t in nodes_at_level:
    inputs = t['inputs']
    expected = t['outputs']
    result = a8q1.nodes_at_level(inputs[0], inputs[1])
    if result != expected:
        print('Error in nodes_at_level(): expected ', expected,
              ' but got ', result, '--', t['reason'])

print("***End of Testing***")