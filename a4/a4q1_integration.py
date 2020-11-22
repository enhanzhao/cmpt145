# a4q1_integration Enhan Zhao enz889    cmpt145

import a4q1 as r

test_suite = [{"input" : ['January February March April', 'May June July August', 'September October November December'],
                    "output" : ['rebmetpeS rebotcO rebmevoN rebmeceD', 'yaM enuJ yluJ tsuguA', 'yraunaJ yraurbeF hcraM lirpA'],
                    "reason" : "Test sample file months.txt"},
                    {"input" : ['Hello', 'My name is Paul', 'Nice to meet you!'],
                    "output" : ['eciN ot teem !uoy', 'yM eman si luaP ', 'olleH'],
                    "reason" : "Test multiple words on multiple lines"},
                    {"input" : ["12 34", "56 78", '90 12'],
                    "output" : ['09 21', '65 87', '21 43'],
                    "reason" : "Test multiple items in a line with multiple lines"}]

for test in test_suite:
    file_list = test["input"]     #out put from r.open_file()
    outputs = test["output"]
    reversed_line = r.reverse_lines(file_list)    #put list through both main functions for integration test
    reversed_letters = r.reverse_letters(reversed_line)
    if reversed_letters != outputs:
        print("Error in integration testing, expected:", outputs, "but got:", resulted, "reason", test["reason"])

print("************End of integration testing***********************")