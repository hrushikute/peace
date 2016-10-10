#!/usr/bin/python

'''
Program to get the sum of all the subjects and percentage calculation
Author : Hrushikesh Kute
Copyright 2016
'''
Total=500

## declare sample DS
st={1: ['Hrushikesh', 80, 90, 78, 80, 45], 2: ['Rohan', 89, 56, 78, 23, 56]}

for ky in st.keys():  # Get the keys from dictionary 
    sum=0
    for sub in range(1,len(st[ky])):
        sum=sum+st[ky][sub]
    print "Name : %s Total :%d Percent %.2f" %(st[ky][0],sum,(sum*100.0)/Total)
