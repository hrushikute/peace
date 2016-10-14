#!/usr/bin/python


'''
Program to find
1.Whether the number is prime.
2.Whether the number is Armstrong

So lets have fun.

Author : Hrushikesh Kute
Copyright 2016

'''

print __doc__
import math
ip_num=input('Enter the number : ')


def armstrong(ip_num):
    deg=len(str(ip_num))
    total=0
    while ip_num!=0:
        temp=ip_num%10
        total+=temp**deg
        ip_num=ip_num/10

    return total

def prime_num(ip_num):
    Bool=False
    till=int(math.sqrt(ip_num))
    print "Till",till
    for counter in range(2,till):
        if ip_num%counter==0:
            Bool=True
            break
    print Bool
    return Bool



total=armstrong(ip_num)
print total,ip_num
if total==ip_num:
    print "Number : %d is armstrong number " %(ip_num)
else:
    print "Number : %d is NOT armstrong number " %(ip_num)

Bool=prime_num(ip_num)
if Bool==True:
    print "Number %d is NOT a  prime number " %(ip_num)
else:
    print "Number %d is a  prime number " % (ip_num)