#a10q3 Enhan Zhao enz889 CMPT145

# CMPT 145: Huffman Codes
# Implements a decoder application
#
# The input to the program is a text file
# with the following format:
# line 0: <code-size> <msg-size>
# lines 1 thru <code-size>:
#    bits:'char'
# lines <code-size>+1 thru <code-size> + <message-size> + 1


import sys as sys

# send the output to the console
DEFAULT_OUTPUT_FILE = '<console>'


def main():
    """
    Purpose
        The main program.
        Usage: python3 Decoder.py <filename>
        Sends output to DEFAULT_OUTPUT_FILE
    Return:
        :return: None
    """
    if len(sys.argv) != 2:
        print('Usage: python3', sys.argv[0], '<filename>')
        print('-- sends output to', DEFAULT_OUTPUT_FILE, '-- ')
        return

    s = open(sys.argv[1], "r")
    sizes = s.readline().rstrip().split() #grab the first line for sizes

    code_size = int(sizes[0]) #assign sizes to variables
    message_size = int(sizes[1])

    codes = []  #grab code for decoder, use readline() to step through each line
    for i in range(0, code_size):
        line = s.readline().rstrip()
        codes.append(line)

    dc = build_decoder(codes)

    for i in range(message_size):   #readline() is now pointing at the first line of message. This way we grab 1 line at a time instead of the whole message section.
        line = s.readline().rstrip()
        msg = decode_message(line, dc)
        print(msg)
    s.close()



def build_decoder(code_lines):
    """
    Purpose:
        Build the dictionary for decoding from the given list of code-lines
    Preconditions:
        :param code_lines: A list of strings of the form "CODE:'<char>'"
    Return:
        :return: a dictionary whose keys are 'CODE' and values are <char>
    """
    codec = {}
    for code_str in code_lines:
        cchr = code_str.split(':')
        code = cchr[0]
        char = cchr[1]
        codec[code] = char[1]   # The input file has ' ' around the character
    return codec


def decode_message(coded_message, codec):
    """
    Purpose:
        Decode the message using the decoder.
    Preconditions:
        :param coded_message: An encoded string consisting of digits '0' and '1'
        :param codec: a Dictionary of coded_message-character pairs
    Return:
        :return: A string decoded from coded_message
    """
    decoded_chars = []
    first = 0
    last = first + 1
    while first < len(coded_message):
        partial_code = coded_message[first:last]
        if partial_code in codec:
            decoded_chars.append(codec[partial_code])
            first = last
            last = first + 1
        else:
            last += 1
    return ''.join(decoded_chars)





if __name__ == '__main__':
    main()

