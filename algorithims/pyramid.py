'''
    given a number return rows with spaces on both ends
    and it will grow in a pyramid format.
'''

# generate_sequence = input("Choose a number for your pyramid\n")

def pyramid(num):
    my_symbol = '*'
    # generate string\n for every line
    # every line goes up in value with corresponding space on both sides
    mystr = ''
    for i in range(1,num+1):
            # str = ' ' * i
            # print(len(str))
            ok = (i * my_symbol)
            # ok = str +(i * my_symbol)
            print('s',add_spaces(ok, num))
            mystr = mystr + ok + '\n'   
    return mystr
def add_spaces(str, num):
    # print(str)
    for i in range(num,0,-1):
        # print(i)
        space = ' ' * i
        str = space + str
        # print(str)
    # print(str)     
    return str
    # return len(str)
    
# pyramid(3)
# print(pyramid(3))
print(pyramid(7))
