#!/usr/bin/python

'''

Progam to find whether the input year is leap year or not.

Input : Year
Output: whether the year is leap year or not.

Author : Hrushikesh Kute
Copyright 2016


'''

print __doc__

input_year=input('Enter the year to be checked as leap year or not :')

input_year=abs(input_year)



def check_leap(input_year):
    if input_year % 4 == 0:
        if ((input_year % 100 == 0) and (input_year % 400 != 0)):
            print "Year is not a leap year !"
        else:
            print "Year is a leap year !"

    else:
        print "Year is not a leap year !"

check_leap(input_year)
