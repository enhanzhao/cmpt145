#enz889 Enhan Zhao assignment 1 question 3

def read_file(txt_doc):
    """
    reads a file and returna list of lists of each line from the file
    :param txt_doc: a text document
    :return: a list of lists
    """
    f = open(txt_doc, "r")
    triangle = []
    for line in f:
        triangle.append([int(x) for x in line.split()])
    f.close()
    return triangle

def if_pascal(triangle_raw):
    """
    checks if a list of lists is a pascal triangle
    :param triangle_raw: a list of lists of ints that is potentially a pascal triangle
    :return: a Boolean value depending on if triangle is a pascal triangle
    """
    triangle = [x for x in triangle_raw if x != []]     #creates new triangle without empty lines
    for i in range(len(triangle)):      #checks if triangle size n is n+1 on the next line
        if len(triangle[i]) != i+1:
            return False
    if triangle[0] != [1]:
        return False
    elif triangle[1] != [1, 1]:
        return False
    new = [x for x in triangle]
    del new[0]
    for line in new:            #checks if first and last number is 1
        if line[0] != 1 or line[-1] != 1:
            return False
    for l in range(len(new)-1):
        for n in range(1, len(new[l])):
            if new[l][n-1] + new[l][n] != new[l+1][n]:
                return False
    return True


t = read_file("EvidenceTriangle.txt")
if if_pascal(t) == False:
   print("the evidence is not a real Pascal Triangle, NOT GUILTY!")
else:
    print("the evidence is a real Pascal Triangle, GUILTY!")
