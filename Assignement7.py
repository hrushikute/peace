#!/usr/bin/python

'''

Program to fin the fibonacci series of N Numbers.

input : Integer Number

output: Fibonacci series of input number.

Author : Hrushikesh Kute.

Copyright 2016.

'''


print __doc__

N = input('Enter the number for fibonacci series :')

if N <= 0:
    print "Cannot compute fibbonaci series !"
    quit()
fib_series=[]
if N == 1:
    fib_series.append(0)
    print "Fibonacci Series : ",fib_series
elif N == 2:
    fib_series.append(0)
    fib_series.append(1)
    print "Fibonacci Series : ",fib_series
else:
    fib_series.append(0)
    fib_series.append(1)
    for i in range(3,N+1):
        fib_series.append(fib_series[i-3] + fib_series[i-2])

print "Fibonacci Series : ", fib_series