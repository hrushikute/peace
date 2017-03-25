'''
GIL : GLobal interpreter lock.

'''

import threading as mt

import time

start=time.time()
def start_thread(i):
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

t1= mt.Thread(target=start_thread,args=(itreration/2,))
t2= mt.Thread(target=start_thread,args=(itreration/2,))

t1.start()
t2.start()

t1.join()
t2.join()
end=time.time()

print "Two threads took : {} secons to finish " .format (end-start)


