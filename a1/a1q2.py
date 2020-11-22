#enz889 Enhan Zhao assignment 1 question 2

def get_data(n, data):
    """
    gathers data based on how many int inputs are required into a list
    :param n: the total number of inputs
    :param data: a list with all the inputs
    :return: data, a list with all the inputs
    """
    data = []
    for i in range(n):
        d = int(input('Enter one interger only:'))
        if d < 0:
            d = int(input("Please enter a potitive interger:"))
        data.append(d)
    return data

def counting(data):
    """
    counts how many of occurrence of each input value there are and returns a list based on the min and max values input
    :param data:a list of all the inputs
    :return: frequency, a list of all the occurrences of input values
    """
    the_min = min(data)
    the_max = max(data)
    fsize = the_max + 1
    frequency = [0]*(fsize)
    for d in data:
        frequency[d] += 1  
    return frequency

def draw_histogram(frequency,):
    """
    prints to screen the input values along with the number of occurrences as asterisks
    :param frequency: a list with the occurrences of each int
    :return: nothing
    """
    print("\n\n\n ----------- Histogram ----------------\n")
    for f in range(len(frequency)):
        print(f, '*'*frequency[f])
        
data_size = int(input('How many data values?'))
data = get_data(data_size, [])
frequency = counting(data)
draw_histogram(frequency)

