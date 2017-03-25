#!/usr/bin/python

import re

'''
Pattern matching


'''


match=re.match('this', 'this is a man !')

print match

print match.span()
print match.start()
print match.end()
print match.group()

# pattern also match a part of string

match=re.match('this','thisisisisisiisthisis89w9 is a man')
print match
print match.span()
print match.group()

# with case insensetive
print ' Case insestetive :'
match=re.match('THis','this is a man this',flags=re.I)
print match.span()


# Searrch the occurence

match=re.search('is','thisis si s aistring !')
print match.span()


#Compile

patternObj=re.compile('is')
match=patternObj.search('thisis si ssisiiisisi!')
print match.span()

#findall

allmatch = re.findall('is','this is is a sting')
print allmatch


'''
Wild card charachters

.(Dot) --> match  any single Occurence of any thing except  \n
'''

match =re.search('..i','his the  name is maya')
print match.group()

match =re.search('.i','his the  name is maya')
print match.group()

match =re.search('10.',' the number 101  has ip : 10.21.343.454')
print match.group()

# Due to back slash \ the wild crad ness of dor . has be removed.

match =re.search('10\.',' the number 101  has ip : 10.21.343.454')
print match.group()

'''
Wild card
[] --> charachter class
[abc] --> either a b or c

'''

match =re.search('[abcde]',' The number 101  has ip : 10.21.343.454')
print match.group()


match =re.search('[a-h]',' The number 101  has ip : 10.21.343.454')
print match.group()

match =re.search('[a-z]',' The number 101  has ip : 10.21.343.454')
print match.group()

match =re.search('[a-zA-Z]',' The number 101  has ip : 10.21.343.454')
print match.group()

match =re.search('[0-9][0-9]\.[0-9][0-9]',' the number 101  has ip : 10.21.343.454')
print match.group()


'''

[^abc] --> other than a b or c
'''

match =re.search('[^a-zA-Z]',' The number 101  has ip : 10.21.343.454')
print match.group()


'''
? --> Zero or one occurence of previos charachter

'''

match =re.search('ab?',' this is an abbbb pattern')
print match.group()

match =re.search('ab?',' this is abbbb pattern removed an' )
print match.group()

match =re.search('ab??',' this is an abbbb pattern')
print match.group()

'''
* --> Zero or more occurence of previos occurence
'''

match =re.search('ab*',' this is an abbbb pattern')
print match.group()

match =re.search('ab*',' this is  abbbb pattern')
print match.group()

# make it non greedy

match =re.search('ab*?',' this is an abbbb pattern')
print match.group()

'''
+ --> minimun one occurence of prev charchter


'''

match =re.search('ab+',' this is an abbbb pattern')
print match.group()


'''
{min,max} --> range of occurence of previous charchter

'''

match =re.search('ab{1,3}',' this is an abbbb pattern')
print match.group()

match =re.search('ab{,3}',' this is an abbbb pattern')
print match.group()

match =re.search('ab{1}',' this is an abbbb pattern')
print match.group()


match =re.search('[0-9]+\.[0-9]+\.\d+\.\d+',' the number 101  has ip : 10.21.343.454')
print match.group()



'''
re.M  ---> multi line search

re.S --> scan a complete string

re.X --> verbose -- used for pattern readability

^ -- > start with

$ --> String should end with


'''

match=re.search('^THis','Thi is a man \nthis is a girl ! ',flags=re.I|re.M)
print match.group ()


match=re.search('.*','Thi is a man \nthis is a girl ! ',flags=re.I)
print match.group ()

match=re.search('.*','Thi is a man \nthis is a girl ! ',flags=re.I|re.S)
print match.group ()


match =re.search(' \d+\. \d+\. \d+\. \d+',' the number 101  \n has ip : 10.21.343.454',flags=re.I|re.S| re.X)
print match.group()


string ='ip : 10.11.12.32 again  ip: 89.33.22.11'
print re.sub('\d+\.\d+\.\d+\.\d+','<HIDDEN CHARACHTERS>',string,flags=re.I)