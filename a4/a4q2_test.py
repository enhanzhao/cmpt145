#a4q2_test enz889 Enhan Zhao cmpt145

import a4q2 as c

######TEST calculate()#####################################################

#Assuming that the inputs will be syntactically correct

test_suite =  [     {"input": "( 1 + 1.5 )",
                    "output" : 2.5,
                    "reason" : "Tests + operator on positive numbers"},
                    {"input": "( -6 + -5 )",
                    "output" : -11.0,
                    "reason" : "Tests + operator on negative numbers"},
                    {"input" : "( 1 - 1 )",
                    "output" : 0.0 ,
                    "reason" : "Tests - operator on positive numbers"},
                    {"input": "( -10 - -11.5 )",
                    "output" : 1.5,
                    "reason" : "Tests - operator on negative numbers"},
                    {"input": "( 5 * 5 )",
                    "output": 25.0,
                    "reason": "Test * operator"},
                    {"input": "( -5 * -5 )",
                    "output": 25.0,
                    "reason": "Test * operator on negative numbers"},
                    {"input": "( 999 / 10 )",
                    "output" : 99.9,
                    "reason" : "Test / operator on positive numbers"},
                    {"input": "( 999 / 10 )",
                    "output" : 99.9,
                    "reason" : "Test / operator on negative numbers"},
                    {"input" : "( ( ( 1 + 1 ) + ( ( 1 - 1 ) * ( 1 * 1 ) ) ) + ( 1 / 1 ) )",
                    "output" : 3.0,
                    "reason" : "Test four types of operators, test each if statement when checking operator type."},
                    {"input": "( ( ( ( ( ( -5 * 1 ) + 1 ) + 1 ) + 1 ) + 1 ) + 1 )",
                    "output": 0.0,
                    "reason": "Test the if statement checking for '(', start with 6 brackets"}]
for test in test_suite:
    inputs = test["input"]
    outputs = test["output"]
    result = c.calculate(inputs)
    if result != outputs:
        print("Error in calculate(), expected:", outputs, "but got:", result, test["reason"])
print("**********End of testing**********")