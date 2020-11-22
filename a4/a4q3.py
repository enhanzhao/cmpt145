#a4q3 enz889 Enhan Zhao cmpt145

import a4q2 as c

print("Welcome to calculator!")
x = input("Input math expression with brackets around each operation")
while x != "quit":
    print(c.calculate(x))
    x = input("Enter another expression")
print("Thank you for using calculator!")