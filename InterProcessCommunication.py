
'''
Pipe
Queue are the two ways used for IPC in python.


'''

from multiprocessing import  Process ,Pipe

import os
import time

print "Process PID", os.getpid()

def target_function(proc,fmsg):
    #fmsg='Message from child process'
    count =0
    while count <10 :
        msg=proc.recv
