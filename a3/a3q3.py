#a3q3 Enhan Zhao enz889 cmpt145

###################
#Experiment ADT###
#####################

def create(filename):
    """
    Purpose: creates and returns a data structure to store experimental data. Each string is stored in a list. Only stores letters "A", "T", "G", "C"
    Preconditions:
     filename: the name of the file to be created
    Postconditions: none
    :return: a list of strings containing each DNA sequence in a file
    """
    f = open(filename, "r")
    DNAlist = []
    index = []
    for line in f:          #read file into list
        DNAlist.append(line.rstrip())
    for i in range(len(DNAlist)):       #takes index of every ">"
        if DNAlist[i][0] == ">":
            index.append(i)
    newDNAlist=[]
    for i in range(len(index)-1):   #combine all strings in between each ">" into one string
        newDNAlist.append("".join(DNAlist[index[i]+1:index[i+1]],))
    newDNAlist.append("".join(DNAlist[index[-1]+1:len(DNAlist)]))       #append everything after the last ">"
    for i in newDNAlist:           #check if only GTCA are in strings, it not delete the string
        for k in range(len(i)):
            if i[k]!= "A" and i[k]!= "T" and i[k]!= "G" and i[k]!= "C":
                newDNAlist.remove(i)
    f.close()
    return newDNAlist

def display(sequences):
    """
    purpose: takes a list of strings and prints each data value after a header
    Preconditions:
        sequences: a list of strings containing DNA sequences
    Postconditions: none
    return: a string
    """
    if sequences == []:
        return ""
    string = ""
    for i in range(len(sequences)):
        string += (">"+str(i+1)+'\n')           #header starting from 1
        string += (sequences[i]+'\n')
    return string

def numSequences(sequences):
    """
    Purpose: return the number of sequences stored in the data structure.
    preconditions:
        sequences: a list of strings containing DNA sequences
    postconditions: none
    return: the number of sequences stored
    """
    if sequences == []:
        return 0
    return len(sequences)

def averageLength(sequences):
    """
    Purpose: return the average length of DNA sequences stored in the data structure.
    preconditions:
        sequences: a list of strings containing DNA sequences
    postconditions: none
    return: the average length of DNA sequences as an int
    """
    if sequences == []:
        return 0
    total = 0
    for i in sequences:
        total += len(i)
    return total//len(sequences)

def lengthDistribution(sequences):
    """
    Purpose: returns a dictionary where the key value pairs are the unique sequence lengths and the count for that length
    preconditions:
        sequences: a list of strings of DNA sequences
    postconditions: none
    return: a dictionary where key is the unique sequence lengths and value is the count for that length
    """
    dict = {}
    for i in sequences:
        if len(i) in dict:
            dict[len(i)] += 1
        else:
            dict[len(i)] = 1
    return dict

def averageGCcontent(sequences):
    """
    Purpose: returns the average count of GC content of each individual DNA sequences in the list.
        ***TAKES THE AVERAGE OF EACH INDIVIDUAL DNA's GC % AND DIVIDE BY THE TOTAL NUMBER OF DNA.
        ***COULD ALSO BE THE TOTAL GC CONTENT IN ALL THE DNA AS ONE STRING IN THE LIST.
        *** "Can do it this way too" - Luana
    preconditions:
        sequences: a list of strings containing DNA sequences
    postconditions: none
    return: the average percentage of GC content in the list accurate to 2 decimals
    """
    if sequences == []:
        return None
    averages = 0
    for i in sequences:
        for k in range(len(i)):
            count = 0
            if i[k] == 'G' or i[k] == 'C':
                count += 1
            averages += (count/len(i))*100
    return '%.2f' % (averages/len(sequences))

def removeLowQuality(sequences, minCutoff, maxCutoff):
    """
    purpose: remove sequences with GC content above or below the cutoff limits
    preconditions:
        sequences: a list of strings containing DNA sequences
        minCutoff: a number in percentage that is the minimum threshold of removal
        maxCutoff: a number in percentage that is the maximum threshold of removal
    postconditions: the data in the ADT modified
    return: nothing
    """
    if sequences == []:
        sequences = []
    else:
        s = [x for x in sequences]   #create a new list to be iterated over so items can be deleted from the original
        for i in s:
            count = 0
            for k in range(len(i)):
                if i[k] == 'G' or i[k] == 'C':
                    count += 1
            averages = (count / len(i)) * 100
            if averages < minCutoff or averages > maxCutoff:
                sequences.remove(i)



