import threading,logging,time

'''
program to make the thread as daemon
'''

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s](%(threadName)s(%(message)s)',
                    filename='Logingdaemon.log',
                    filemode='w')


def daemon_process():
    logging.debug('Starting')
    time.sleep(10)
    logging.debug('Exiting')


d=threading.Thread(target=daemon_process,name='Daemon_thread')
d.setDaemon(True)

def non_daemon_proc():
    logging.info('Starting')
    time.sleep(1)
    logging.info('Exiiting')

d1=threading.Thread(target=non_daemon_proc,name='Non daemon thread')

d2=threading.Thread(target=daemon_process,name='Non daemon : calling daemon proc function')

d.start()
d1.start()
d2.start()
d1.join()
d2.join()