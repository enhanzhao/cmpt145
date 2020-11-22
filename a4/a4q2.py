#a4q2 enz889 Enhan Zhao cmpt145

import isfloat as f
import TStack as s


def calculate(expression):
    """
    Purpose: By using stacks, complete the calculations of a mathematical expression in the form of a string. Each item in
        expression is examined: numbers gets pushed to a number stack, operators gets pushed to an operator stack. For each ")",
        the previous 2 numbers and the previous operator are poped and evaluated, then pushed back to the stack.
    Preconditions:
    expression: a string that is a math expression with brackets around every operator seperated by a space.
    Postconditions: none
    return: the value of the math expression as a float
    """
    numbers = s.create()
    operators = s.create()
    for l in expression.split():
        if l == "(":
            pass
        elif f.isfloat(l) == True:
            s.push(numbers, float(l))
        elif l != ")":
            s.push(operators, l)
        elif l == ")":
            second = s.pop(numbers)
            first = s.pop(numbers)
            operator = s.pop(operators)
            if operator == "+":     #addition
                s.push(numbers, (first + second))
            elif operator == "-":     #subtraction
                s.push(numbers, (first - second))
            elif operator == "*":     #multiplication
                s.push(numbers, (first * second))
            elif operator == "/":     #division
                s.push(numbers, (first / second))
    return s.pop(numbers)
