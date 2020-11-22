# a4q1_unit Enhan Zhao enz889    cmpt145

import a4q1 as r


#TEST reverse_lines() ###########################################################

reverse_lines_test =  [{"input" : ['1', '2', '3', '4', '-5'],
                    "output" : ['-5', '4', '3', '2', '1'],
                    "reason" : "Test only one item in each line"},
                    {"input" : ["1234-5"],
                    "output" : ["1234-5"],
                    "reason" : "Test only one line with one item"},
                    {"input" : ["12 34", "56 78", '90 12'],
                    "output" : ["90 12", "56 78", "12 34"],
                    "reason" : "Test multiple items in a line with multiple lines"}]
for test in reverse_lines_test:
    inputs = test["input"]
    outputs = test["output"]
    result = r.reverse_lines(inputs)
    if result != outputs:
        print("Error in reverse_lines(), expected:", outputs, "but got:", result, "reason", test["reason"])

# #TEST reverse_letters ###########################################################
reverse_letters_test = [{"input" : ['1', '2', '3', '4', '-5'],
                    "output" : ['1', '2', '3', '4', '5-'],
                    "reason" : "Test only one item in each line"},
                    {"input" : ["1234-5"],
                    "output" : ["5-4321"],
                    "reason" : "Test only one line with one item"},
                    {"input" : ["12 34", "56 78 hello", '90 test 12'],
                    "output" : ["21 43", "65 87 olleh", "09 tset 21"],
                    "reason" : "Test multiple items in a line with multiple lines"}]
for test in reverse_letters_test:
    inputs = test["input"]
    outputs = test["output"]
    result = r.reverse_letters(inputs)
    if result != outputs:
        print("Error in reverse_letters(), expected:", outputs, "but got:", result, "reason", test["reason"])

print("-----End of Testing-----")