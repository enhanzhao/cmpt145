#a3q1 enz889 Enhan Zhao cmpt 145

import a3q2 as Stat

test_create = [
    {'inputs' : [],
     'outputs':[0, 0],
     'reason' : 'Checking initial values'},
]

for t in test_create:
    args_in = t['inputs']       # pointless, but keeps the pattern consistent
    expected = t['outputs']
    thing = Stat.create()
    if thing['count'] != expected[0]:
        print('Error in create(): expected count', expected[0],
              ' but found ', thing['count'], '--', t['reason'])
    if thing['avg'] != expected[1]:
        print('Error in create(): expected avg', expected[1],
              ' but found ', thing['avg'], '--', t['reason'])

# test statistics.add()
test_add = [
    {'inputs' : [0],
     'outputs':[1, 0],
     'reason' : 'No change to avg'},
    {'inputs' : [1],
     'outputs':[1, 1],
     'reason' : 'Positive int, avg change to 1'},
    {'inputs' : [-1],
     'outputs':[1, -1],
     'reason' : 'Negative int, avg change to -1'},
    {'inputs' : [0.9],
     'outputs':[1, 0.9],
     'reason' : 'Positive float test'},
    {'inputs' : [-0.9],
     'outputs':[1, -0.9],
     'reason' : 'Negative float test'},
    {'inputs' : [0.1+0.1+0.1],
     'outputs':[1, 0.3],
     'reason' : 'Float addition error test'},
    {'inputs' : [3.141592653589793238462643383279502884],
     'outputs':[1, 3.141592653589793238462643383279502884],
     'reason' : 'Long decimal floating point test'},
    {'inputs' : [9**9],
     'outputs':[1, 387420489],
     'reason' : 'Test a large number'}]

for t in test_add:
    args_in = t['inputs']
    expected = t['outputs']
    thing = Stat.create()
    Stat.add(thing, args_in[0])
    #check the count
    if thing['count'] != expected[0]:
        print('Error in add(): expected count', expected[0],
              ' but found ', thing['count'], '--', t['reason'])

    # check the ave
    if abs(thing['avg'] - expected[1]) > 0.001:
        print('Error in add(): expected avg', expected[1],
              ' but found ', thing['avg'], '--', t['reason'])

# test Statistics.mean()

test_mean = [
    {'inputs' : [0,0,0,0,0],
     'outputs':[5, 0],
     'reason' : 'All zeroes'},
    { 'inputs' : [1, 2, 3, 4, 5],
     'outputs':[5, 3],
     'reason' : 'All positive numbers'},
    {'inputs' : [-1, -2, -3, -4, -5],
     'outputs':[5, -3],
     'reason' : 'All negative numbers'},
    {'inputs' : [-2, -1, 0, 1, 2],
     'outputs':[5, 0],
     'reason' : 'Mixture of positive and negative ints'},
    {'inputs' : [0.5],
     'outputs':[1, 0.5],
     'reason' : 'Test decimal'},
    {'inputs' : [0.1+0.1+0.1, 1.5-0.5],
     'outputs':[2, 0.65],
     'reason' : 'Test float operations'},
    {'inputs' : [9**9],
     'outputs':[1, 387420489],
     'reason' : 'Test a large number'}]

for t in test_mean:
    args_in = t['inputs']
    expected = t['outputs']
    thing = Stat.create()
    for val in args_in:
        Stat.add(thing, val)
    result = Stat.mean(thing)
    if thing['count'] != expected[0]:
        print('Error in add(): expected count', expected[0],
              ' but found ', thing['count'], '--', t['reason'])
    if thing['avg'] != expected[1]:
        print('Error in add(): expected avg', expected[1],
              ' but found ', thing['avg'], '--', t['reason'])
    if result != expected[1]:
        print('Error in mean(): expected avg', expected[1],
              ' but found ', result, '--', t['reason'])


print('*** Test script completed ***')
