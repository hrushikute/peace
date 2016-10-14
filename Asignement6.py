#!/usr/bin/python

'''

Program to find
1. duplicate element in list
2. Unique element in list

  Author : Hrushikesh Kute
  Copyright
'''

print __doc__

orig_list=[]

no_of_element =input('Enter number of elements in list :')

for i in range(no_of_element):
    orig_list.append(input('Enter number :'))

duplicate_list=[]
# find the ducplicate numbers in list
for i in  orig_list:
    if orig_list.count(i) >1:
        if i not in duplicate_list:
            duplicate_list.append(i)


print "duplicate members in list are" , duplicate_list

distinct_list=[]

# find the unique elemets in list

for member in orig_list:
    if member not in distinct_list:
        distinct_list.append(member)


print "Distinct members in list : ", distinct_list

unique_list=[]

for mem in duplicate_list:
    if mem in distinct_list:
        distinct_list.remove(i)

print "Unique mebers in list :", distinct_list

