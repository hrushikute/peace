#!/usr/bin/python

'''
Program to swap two numbers
input 1 > Number
input 2 > Number

Author : Hrushikesh Kute
Copyright 2016

'''

# Let have some fun with swapping of numbers.

pname='Program to swap numbers'
prompt='>'

pname.center(40,'-')

print " Enter number 1 :"

Num1= input(prompt)

print " Enter number 2 :"

Num2 = int(raw_input(prompt))

Num1=Num1^Num2 # XOR operation
Num2=Num1^Num2
Num1=Num1^Num2

print "After Swapping :Number 1  %d" % (Num1)
print "After Swapping :Number 2  %d" % (Num2)


