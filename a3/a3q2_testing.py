#a3q2_testing enz889 Enhan Zhao cmpt 145

import a3q2 as Stat
#test statistics.create()##############################################
test_create = [
    {'inputs' : [],
     'outputs':[0, 0],
     'reason' : 'Checking initial values'},]
for t in test_create:
    args_in = t['inputs']
    expected = t['outputs']
    thing = Stat.create()
    if thing['count'] != expected[0]:
        print('Error in create(): expected count', expected[0],
              ' but found ', thing['count'], '--', t['reason'])
    if thing['avg'] != expected[1]:
        print('Error in create(): expected avg', expected[1],
              ' but found ', thing['avg'], '--', t['reason'])

#test statistics.add()##############################################
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
    if thing['count'] != expected[0]:
        print('Error in add(): expected count', expected[0],
              ' but found ', thing['count'], '--', t['reason'])
    if abs(thing['avg'] - expected[1]) > 0.001:
        print('Error in add(): expected avg', expected[1],
              ' but found ', thing['avg'], '--', t['reason'])

# test Statistics.mean()##############################################
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

#test Statistics.count()##############################################
test_count = [
    {'inputs' : [],
     'outputs' : 0,
     'reason' : "No data value"},
    {'inputs' : [1],
     'outputs' : 1,
     'reason' : "One small positive int"},
    {'inputs' : [-1],
     'outputs' : 1,
     'reason' : "One small negative int"},
    {'inputs' : [9, 9, 9, 9, 9.5, 9.5, 9.5, 9.5],
     'outputs' : 8,
     'reason' : "Test multiple positive numbers"},
    {'inputs' : [-9, -9, -9, -9, -9.5, -9.5, -9.5, -9.5],
     'outputs' : 8,
     'reason' : "Test multiple negative numbers"},
    {'inputs' : [123456789000004444455555],
     'outputs' : 1,
     'reason' : "Test one large number"},
    {'inputs' : [0.1+0.1+0.1],
     'outputs' : 1,
     'reason' : "Test decimal operation"},]
for t in test_count:
    args_in = t['inputs']
    expected = t['outputs']
    thing = Stat.create()
    for val in args_in:
        Stat.add(thing, val)
    result = Stat.count(thing)
    if result != expected:
        print("Error in count(): expected count", expected,
              ' but found ', thing['count'], '--', t['reason'])

#test Statistics.max()##############################################
test_max = [
    {'inputs' : [],
     'outputs' : None,
     'reason' : "No data value"},
    {'inputs' : [0],
     'outputs' : 0,
     'reason' : "Only one value zero"},
    {'inputs' : [1, 3.5, 4, 5, 5.5],
    'outputs' : 5.5,
    'reason' : "Test multiple positive numbers"},
    {'inputs' : [-6.5, -4, -3.5, -2, -1],
    'outputs' : -1,
    'reason' : "Test multiple negative numbers"},
    {'inputs' : [-49.9, -30, 15.55, 0, -15.55, 30, -49.999],
    'outputs' : 30,
    'reason' : "Test mixed pos and neg numbers"},
    {'inputs' : [0.000001, 0.0000005, 0.000000001],
    'outputs' : 0.000001,
    'reason' : "Test small decimals"},]
for t in test_max:
    args_in = t['inputs']
    expected = t['outputs']
    thing = Stat.create()
    for val in args_in:
        Stat.add(thing, val)
    result = Stat.maximum(thing)
    if result != expected:
        print("Error in maximum(): expected val", expected,
              ' but found ', result, '--', t['reason'])

#test Statistics.min()##############################################
test_min = [
    {'inputs' : [],
     'outputs' : None,
     'reason' : "No data value"},
    {'inputs' : [0],
     'outputs' : 0,
     'reason' : "Only one value zero"},
    {'inputs' : [1, 3.5, 4, 5, 5.5],
    'outputs' : 1,
    'reason' : "Test multiple positive numbers"},
    {'inputs' : [-6.5, -4, -3.5, -2, -1],
    'outputs' : -6.5,
    'reason' : "Test multiple negative numbers"},
    {'inputs' : [-49.999, -30, 15.55, 0, -15.55, 30, -49.9],
    'outputs' : -49.999,
    'reason' : "Test mixed pos and neg numbers"},
    {'inputs' : [0.000001, 0.0000005, 0.000000001],
    'outputs' : 0.000000001,
    'reason' : "Test small decimals"},]

for t in test_min:
    args_in = t['inputs']
    expected = t['outputs']
    thing = Stat.create()
    for val in args_in:
        Stat.add(thing, val)
    result = Stat.minimum(thing)
    if result != expected:
        print("Error in minimum(): expected val", expected,
              ' but found ', result, '--', t['reason'])

print('*** Test script completed ***')
