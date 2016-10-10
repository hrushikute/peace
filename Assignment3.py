#!/usr/bin/python

'''
Program to convert Celcius to faranhite

Author : hrushikesh
Copyright 2016


'''
def Convert_CENTI_TO_FAR (centi):
    far= ((centi*9)/5.0) + 32
    return far

prompt='-'
print '*'*20
print 'Program from conversion of celcius to faranhite.'
print '*'*20
print "Enter the celcius value : "
centi=input(prompt)

far= Convert_CENTI_TO_FAR(centi)
print "Faranhite value : %.2f" %(far)


