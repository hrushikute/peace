#!/usr/bin/python

# Lets have fun with Strings and Text

'''
Author : Hrushikesh Kute
Copyright @2016

'''

x= "There are %d types of people." % 10
binary='Binary'
do_not="don't"
y ="Those who now %s and those who %s." %(binary,do_not)

print x
print y

print "I said : %r." % x
print "I also said :'%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny? %r"

print joke_evaluation % hilarious

w = "This is a left side of .."
e = "a sting witj a right side."

print w + e
