#!/usr/bin/python

'''

Program to To get the Basic salary and calculate Goss salary
input :  Basic Salary
output : Gross Salary

Author : Hrushikesh
Copyright 2016

'''

'''

Docstring

'''
print __doc__

# Function to compute Gross salary
def Compute_gross(basic):
    Gross = basic + basic * 0.1 + basic * 0.12
    return Gross


prompt=' > > '
print "Enter Basic Salary :"

basic=input(prompt)

Gross=Compute_gross(basic)

print "Gross salary = %0.2f" %(Gross)

