

def count_lines(filename:str):
    myfile = open(filename, 'r')
    lines = 0
    for line in myfile:
            lines += 1
    myfile.close()
    return lines
def count_chars(filename:str):
    myfile = open(filename,'r')
    mytext = myfile.read()
    return len(mytext)
def test(filename:str):

    return count_lines(filename),  count_chars(filename)

