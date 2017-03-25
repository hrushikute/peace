# Editing strings in Python
#Copyright 2016 Hrushikesh
import sys


def main():
    print "Hello7" + str(6)
    print  sys.argv # Prints the arguments passed to code
    calculate_length("Hrushikesh")
    calculate_length("Hello world")
    calculate_length(sys.argv[0])
    print_name('Alice')
    print_name('Hrushikesh')

def calculate_length(value):
    length=len(value)
    print value,"-->" +str(length)


def print_name(name):
    if name == 'Alice':
        print 'Alert : Alice mode on !'
        name = name + '????'
        print "Hello" ,name
    name = name + '!!!!'
    print name
#standard boilerplate that calls main
if __name__ == '__main__':
    main()

