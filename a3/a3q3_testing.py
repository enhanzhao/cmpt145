#a3q3_testing enz889 Enhan Zhao cmpt 145
import a3q3 as Exp

#test create()#######################################
# "Don't have to test reading file" - Luana
# test_create = [{'inputs':["sequences1.txt"],
#                 'outputs':['ATGATGATGGCG', 'GGCATATCCGGATACC', 'TAGCTAGCCCGC'],
#                 'reason':"Test reading file"}]
# for test in test_create:
#     inputs = test["inputs"]
#     expected = test["outputs"]
#     result = Exp.create("sequences1.txt")
#     if result != expected:
#         print('Error in create(): expected ', expected,
#               ' but got ', result, '--', test["reason"])

# #test display()####################################################3

test_display = [{'inputs': ["ATGC"],
                'outputs':">1"+"\n"+"ATGC"+"\n",
                'reason':"Test only one data in sequence"},
                {'inputs': ["AAAA", "TT", "GGG", "C"],
                 'outputs':">1"+"\n"+"AAAA"+"\n" +">2"+"\n"+ "TT" +"\n" + ">3"+"\n"+"GGG" +"\n"+">4"+"\n"+"C"+"\n",
                 'reason': "Test multiple datas of multiple length"},                ]
for test in test_display:
    inputs = test["inputs"]
    expected = test["outputs"]
    result = Exp.display(test["inputs"])
    if result != expected:
        print('Error in display(): expected ', expected,' but got ', result, '--', test["reason"])

#test numSequence()#######################################
test_numsequence = [{'inputs':[],
                'outputs': 0,
                'reason':"Test empty list"},
                {'inputs': ["G"],
                'outputs': 1,
                'reason':"Test only one item"},
                {'inputs': ["C", "AT", "TC"],
                'outputs': 3,
                'reason':"test multiple items in list"}]
for test in test_numsequence:
    inputs = test["inputs"]
    expected = test["outputs"]
    result = Exp.numSequences(inputs)
    if result != expected:
        print('Error in numSequence(): expected ', expected,' but got ', result, '--', test["reason"])

#test averageLength()#######################################
test_averagelength = [{'inputs':[],
                'outputs': 0,
                'reason':"Test empty list, cannot divide by zero"},
                {'inputs': ["G"],
                'outputs': 1,
                'reason':"Test only one item with one letter"},
                {'inputs': ["CATCAT"],
                'outputs': 6,
                'reason':"test one item with multiple letters"},
                {'inputs': ["CATG", "C", "TACGG"],
                'outputs': 3,
                'reason': "Test interger divison line with uneven division"}]
for test in test_averagelength:
    inputs = test["inputs"]
    expected = test["outputs"]
    result = Exp.averageLength(inputs)
    if result != expected:
        print('Error in averageLength(): expected ', expected,' but got ', result, '--', test["reason"])

#test lengthDistribution()###################################
test_lengthdistribution = [{'inputs':[],
                     'outputs': {},
                     'reason':"Empty list"},
                     {'inputs':[""],
                     'outputs': {0:1},
                     'reason':"Test empty strings"},
                     {'inputs': ["A"],
                     'outputs': {1:1},
                     'reason': "Test one item with one letter"},
                     {'inputs': ["A", "CC", "TTT", "GGGG"],
                     'outputs': {1:1, 2:1, 3:1, 4:1},
                     'reason': "Test multiple sequences with one count each"},
                     {'inputs': ["AAACT", "", "AA", "T", "CCCTA", "AACGT", "GG", "", "GG", "CGGGG"],
                     'outputs': {0:2, 1:1, 2:3, 5:4},
                     'reason': "Test various inputs of various length"},]
for test in test_lengthdistribution:
    inputs = test["inputs"]
    expected = test["outputs"]
    result = Exp.lengthDistribution(inputs)
    if result != expected:
        print('Error in lengthDistribution(): expected ', expected,' but got ', result, '--', test["reason"])

#test averageGCcontent()#######################################
test_averagegccontent = [{'inputs': ["G", "C"],
                'outputs': '%.2f' % 100.00,
                'reason': "Only G and C"},
                {'inputs': [],
                'outputs': None,
                'reason': "Empty list"},
                {'inputs': ["GT", "CT", "AC"],
                'outputs': '%.2f' % 50.00,
                'reason': "Half of each string is G or C"},
                {'inputs': ["GG", "TT", "CC", "AA"],
                'outputs': '%.2f' % 50.00,
                'reason': "Half of the sequence is G or C"},
                {'inputs': ["GG", "TT", "CC"],
                'outputs': '%.2f' % 66.67,
                'reason': "1/3 of the sequence is G or C"},]

for test in test_averagegccontent:
    inputs = test["inputs"]
    expected = test["outputs"]
    result = Exp.averageGCcontent(inputs)
    if result != expected:
        print('Error in averageGCcontent(): expected ', expected,' but got ', result, '--', test["reason"])

# #test removeLowQuality#######################################
test_removelowquality = [{'inputs': [[],0, 0],
                        'outputs': [],
                        'reason': "Test Empty sequence"},
                        {'inputs': [["GGTT", "CAAA", "TCCC"], 40, 60],
                        'outputs': ["GGTT"],
                        'reason': "Tests min and max range"},
                        {'inputs': [["GGTT", "TTGG", "CCAA"], 50, 50],
                        'outputs': ["GGTT", "TTGG", "CCAA"],
                        'reason': "Test same value for min max, keeping only one value"},
                        {'inputs': [["CAAA", "GTT", "GGA", "CCCA"], 33.2, 66.7],
                        'outputs': ["GTT", "GGA"],
                        'reason': "Test various GC content with decimal min max"}
                         ]
for test in test_removelowquality:
    sequence = test["inputs"][0]
    mini = test["inputs"][1]
    maxi = test["inputs"][2]
    expected = test["outputs"]
    Exp.removeLowQuality(sequence, mini, maxi)
    if sequence != expected:
        print('Error in removeLowQuality(): expected ', expected,' but got ', sequence, '--', test["reason"])

print("********End of test script********")