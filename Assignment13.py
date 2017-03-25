#!/usr/bin/python

'''

Program to sort the below list with second item
mylist = [["john", 1, "a"], ["larry", 0, "b"]].

Author : Hrushikesh Kute
Copyright 2016

'''

print __doc__


mylist = [["john", 1, "a"], ["larry", 0, "b"]]

print "List Before : ",mylist
mylist.sort(key=lambda list:list[1])

print "List After : ",mylist