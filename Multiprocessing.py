'''
GIL : GLobal interpreter lock.

'''

import multiprocessing as mp
import os

import time

start=time.time()
def start_process(i):
    print os.getpid()
    while i:
      i-=1
    return

itreration = 50000000

'''
t1=mt.Thread(target=start_thread,args=(itreration/3,))
t2=mt.Thread(target=start_thread,args=(itreration/3,))
t3=mt.Thread(target=start_thread,args=(itreration/3,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
'''

p1= mp.Process(target=start_process,args=(itreration/2,))
p2= mp.Process(target=start_process,args=(itreration/2,))

p1.start()
p2.start()

p1.join()
p2.join()
end=time.time()

print "Two processes took : {} secons to finish " .format (end-start)


