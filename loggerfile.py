'''
logging module is used to create logging in multithreaded env

'''

import logging,threading,time

# We can also put the data in file

#logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s](%(threadName)s)(%(message)s)')

logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s](%(threadName)s)(%(message)s)',
                    filename=r'/home/hrushi/PycharmProjects/Classes/hrushicode/threadlog.log',
                    filemode='w')

def func1():
    logging.info('Starting')
    time.sleep(2)
    logging.info('Exitingg')


def func2():
    logging.info('Starting')
    time.sleep(2)
    logging.info('Exitingg')


t1=threading.Thread(target=func1,name='My thread 1')

t2=threading.Thread(target=func2,name='My thread 1 for func 2')

t3=threading.Thread(target=func2,name='My thread 2 for func 2')

t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()

