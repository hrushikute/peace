

try:
    num= input('Enter the number:')
    print 100/numb
    print 'Above is the result of division'
except ZeroDivisionError:
    print 'Dear Sir ! Kindly enter a non zero number.'
    try:
        num = input('Enter the number:')
        print 100 / num

    except ZeroDivisionError :
        print 'Dear Sir ! Khaddayat ja !'
# Single try can have multiple except.

except NameError,N:
    print N
    print 'Name error'
    print type(N)


except Exception,e:
    print e
    print 'in execption e'
    print type(e)
print 'Program completed.'

# A try can alos have an else block