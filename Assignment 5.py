#/usr/bin/python

'''
Program to reverse a number.

Author : Hrushikesh Kute.

Copyright 2016.

'''

from math import *

print __doc__

num=input("Enter the number :")

counter=1

num_rev=0

while (num != 0 ):

    rev= num % 10


    if counter == 1 :
        num_rev = rev


    else:
        num_rev = num_rev *10
        num_rev = num_rev + rev

    counter+=1
    num = num / 10



print "Reversed_NUMBER =: %d" %(num_rev)

'''
rev=0
while ( num != 0):
    rev=rev*10
    rev=rev+(num%10)
    num=num/10

print "Reversed_NUMBER =: %d" %(rev)
'''