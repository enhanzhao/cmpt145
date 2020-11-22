#a7q6_testing enz889 Enhan Zhao cmpt145
import a7q6
import node
#test to_string
test_to_string = [
    {'inputs' : None,
     'outputs': "EMPTY",
     'reason' : 'Empty node chain'},

    {'inputs' : node.create(1),
     'outputs': "[ 1 | / ]",
     'reason' : 'node chain with one node'},

    {'inputs' : node.create(1, node.create(2, node.create(3))),
     'outputs': "[ 1 | * -]-->[ 2 | * -]-->[ 3 | / ]",
     'reason' : 'node chain with multiple nodes'},]
for t in test_to_string:
    inputs = t['inputs']
    expected = t['outputs']
    result = a7q6.to_string(inputs)
    assert result == expected, 'to_string(): got '\
        +str(result)+' expected '+str(expected)+' -- ' +t['reason']

#test copy()
test_copy = [
    {'inputs' : None,
     'outputs': None,
     'reason' : 'Empty node chain'},

    {'inputs' : node.create(1),
     'outputs': node.create(1),
     'reason' : 'node chain with one node'},

    {'inputs' : node.create(1, node.create(2, node.create(3))),
     'outputs': node.create(1, node.create(2, node.create(3))),
     'reason' : 'node chain with multiple nodes'},]
for t in test_copy:
    inputs = t['inputs']
    expected = t['outputs']
    result = a7q6.copy(inputs)
    assert result == expected, 'copy(): got '\
        +str(result)+' expected '+str(expected)+' -- ' +t['reason']

#test replace()
test_replace = [
    {'inputs' : [None, 0, 0],
     'outputs': None,
     'reason' : 'Empty node chain'},

    {'inputs' : [node.create(1, node.create(2, node.create(3))), 5, 0],
     'outputs': node.create(1, node.create(2, node.create(3))),
     'reason' : 'no replacement'},

    {'inputs' : [node.create(1, node.create(2, node.create(3))), 1, 0],
     'outputs': node.create(0, node.create(2, node.create(3))),
     'reason' : 'replace first'},

    {'inputs': [node.create(1, node.create(2, node.create(3))), 2, 0],
     'outputs': node.create(1, node.create(0, node.create(3))),
     'reason': 'replace middle'},

    {'inputs': [node.create(1, node.create(2, node.create(3))), 3, 0],
     'outputs': node.create(1, node.create(2, node.create(0))),
     'reason': 'replace last'},
]
for t in test_replace:
    inputs = t['inputs']
    expected = t['outputs']
    result = a7q6.replace(inputs[0], inputs[1], inputs[2])
    assert result == expected, 'replace(): got '\
        +str(result)+' expected '+str(expected)+' -- ' +t['reason']

print("***Testing complete***")