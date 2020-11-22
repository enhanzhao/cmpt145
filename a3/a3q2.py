#a3q2 Enhan Zhao enz889 cmpt145

#############################
#Statistics ADT#
##########################

def create():
    """
    Purpose:
        Create a Statistics record.
    Pre-conditions:
        (none)
    Post-conditions:
        a new record is allocated
    Return:
        A reference to a Statistics record.
    """
    b = {}
    b['count'] = 0      # how many data values have been seen
    b['avg'] = 0        # the running average so far
    b["values"] = []
    return b


def add(stat, value):
    """
    Purpose:
        Use the given value in the calculation of statistics.
    Pre-Conditions:
        stat: a Statistics record
        value: the value to be added
    Post-Conditions:
        none
    Return:
        none
    """
    stat['count'] += 1
    stat["values"].append(value)
    k = stat['count']           # convenience
    diff = value - stat['avg']  # convenience
    stat['avg'] += diff/k

def mean(stat):
    """
    Purpose:
        Return the mean of all the values seen so far.
    Pre-conditions:
        stat: the Statistics record
    Post-conditions:
        (none)
    Return:
        The mean of the data seen so far.
        Note: if no data has been seen, 0 is returned.
              This is clearly false.
    """
    return stat['avg']

def count(stat):
    """
    Purpose: given the statistics record, return the number of values recorded already
    Pre-cnditions:
        stat: a statistic record
    Post-conditions:
        none
    Return: the number of data values in the statistics record
    """
    return stat["count"]

def maximum(stat):
    """
    Purpose: give the statistics record, return the maximum value recorded so far
    Pre-cnditions:
        stat: a statistic record
    Post-conditions:
        none
    Return: the max value recorded so far, None if empty
    """
    if stat["values"] == []:
        return None
    return max(stat["values"])
    
def minimum(stat):
    """
    Purpose: give the statistics record, return the minimum value recorded so far
    Pre-cnditions:
        stat: a statistic record
    Post-conditions:
        none
    Return: the min value recorded so far, None if empty
    """
    if stat["values"] == []:
        return None
    return min(stat["values"])
