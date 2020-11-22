#a8q1_testing.py enz889 Enhan Zhao  cmpt145

import a8q2
import treenode as tn

#test mirriored()####################
mirrored = [
    {'inputs'  : [None, None],
     'outputs' : True,
     'reason'  : 'empty trees'},

    {'inputs'  : [tn.create(1), tn.create(1)],
     'outputs' : True,
     'reason'  : 'singleton trees mirrored'},

    {'inputs'  : [tn.create(1), tn.create(2)],
     'outputs' : False,
     'reason'  : 'singleton trees not mirrored'},

    {'inputs'  : [tn.create(1, tn.create(2, tn.create(3))), tn.create(1, None, tn.create(2, None, tn.create(3)))],
     'outputs' : True,
     'reason'  : 'only left children in t1 and only right children in t2 mirrored '},

    {'inputs'  : [tn.create(1, tn.create(2, tn.create(4), tn.create(5)), tn.create(3)), tn.create(1, tn.create(3), tn.create(2, tn.create(5), tn.create(4)))],
     'outputs' : True,
     'reason'  : 'trees with assorted children mirrored'},

    {'inputs': [tn.create(1, tn.create(2, tn.create(4), tn.create(5)), tn.create(3)), tn.create(1, tn.create(3, tn.create(4)), tn.create(2, tn.create(5), tn.create(4)))],
     'outputs': False,
     'reason': 'trees with assorted children not mirrored'},
]
for t in mirrored:
    inputs = t['inputs']
    expected = t['outputs']
    result = a8q2.mirrored(inputs[0], inputs[1])
    if result != expected:
        print('Error in mirrored(): expected ', expected,
              ' but got ', result, '--', t['reason'])

#test reflect()####################
reflect = [
    {'inputs'  : None,
     'outputs' : None,
     'reason'  : 'empty tree'},

    {'inputs'  : tn.create(1),
     'outputs' : tn.create(1),
     'reason'  : 'singleton trees'},

    {'inputs'  : tn.create(1, tn.create(2, tn.create(3))),
     'outputs' : tn.create(1, None, tn.create(2, None, tn.create(3))),
     'reason'  : 'left only'},

    {'inputs'  : tn.create(1, None, tn.create(2, None, tn.create(3))),
     'outputs' : tn.create(1, tn.create(2, tn.create(3))),
     'reason'  : 'right only'},

    {'inputs'  : tn.create(1, tn.create(2), tn.create(3)),
     'outputs' : tn.create(1, tn.create(3), tn.create(2)),
     'reason'  : 'level 1 tree swap'},

    {'inputs': tn.create(1, tn.create(2, tn.create(4), tn.create(5)), tn.create(3, None, tn.create(6))),
     'outputs': tn.create(1, tn.create(3, tn.create(6)), tn.create(2, tn.create(5), tn.create(4))),
     'reason': 'complex tree swap'},
]
for t in reflect:
    inputs = t['inputs']
    expected = t['outputs']
    a8q2.reflect(inputs)
    if inputs != expected:
        print('Error in reflect(): expected ', expected,
              ' but got ', result, '--', t['reason'])

#test reflection()###############################################
reflection = [
    {'inputs': None,
     'outputs': None,
     'reason': 'empty tree'},

    {'inputs': tn.create(1),
     'outputs': tn.create(1),
     'reason': 'singleton tree'},

    {'inputs': tn.create(1, tn.create(2, tn.create(3))),
     'outputs': tn.create(1, None, tn.create(2, None, tn.create(3))),
     'reason': 'tree with only left child'},

    {'inputs': tn.create(1, None, tn.create(2, None, tn.create(3))),
     'outputs': tn.create(1, tn.create(2, tn.create(3))),
     'reason': 'tree with only right child'},

    {'inputs': tn.create(1, tn.create(2, tn.create(4), tn.create(5)), tn.create(3, None, tn.create(6))),
     'outputs': tn.create(1, tn.create(3, tn.create(6)), tn.create(2, tn.create(5), tn.create(4))),
     'reason': 'complex tree reflection'},

]
for t in reflection:
    inputs = t['inputs']
    expected = t['outputs']
    copied = a8q2.reflection(inputs)
    if copied != expected:      #must be same data but different reference
        print('Error in reflection(): expected ', expected,
              ' but got ', copied, '--', t['reason'])
print("***End of testing***")