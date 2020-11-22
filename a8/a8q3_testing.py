#a8q3_testing.py enz889 Enhan Zhao  cmpt145

import a8q3
import treenode as tn


#test complete()###############################################
complete = [
    {'inputs'  : None,
     'outputs' : (False, None),
     'reason'  : 'empty tree'},

    {'inputs'  : tn.create(1),
     'outputs' : (True, 1),
     'reason'  : 'singleton tree'},

    {'inputs'  : tn.create(1, tn.create(2)),
     'outputs' : (False, None),
     'reason'  : 'incomplete height 2'},

    {'inputs'  : tn.create(1, tn.create(2), tn.create(3)),
     'outputs' : (True, 2),
     'reason'  : 'complete height 2'},

    {'inputs'  : tn.create(1, tn.create(2, tn.create(4), tn.create(5)), tn.create(3, tn.create(6), tn.create(7))),
     'outputs' : (True, 3),
     'reason'  : 'complex tree complete'},

    {'inputs'  : tn.create(1, tn.create(2, tn.create(4), tn.create(5)), tn.create(3, None, tn.create(6))),
     'outputs' : (False, None),
     'reason'  : 'complex tree incomplete'},
]
for t in complete:
    inputs = t['inputs']
    expected = t['outputs']
    result = a8q3.complete(inputs)
    if result != expected:
        print('Error in complete(): expected ', expected,
              ' but got ', result, '--', t['reason'])

print("***End of testing***")