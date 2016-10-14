#!/usr/bin/python


'''

Program to calculate the factorial of a number.

Author : Hrushikesh Kute.
Copyright 2016.

'''

print __doc__


def facto(fact_num):
    factorial = 1
    for counter in range(1, fact_num + 1):
        factorial = factorial * counter
    return factorial

fact_num=input('Enter the number to calculate the factorial : ')

print "Factorial of number :" , facto(fact_num)



