from multiprocessing import Pool

def square(num):
    return num * num

if __name__=='__main__' :
    p=Pool(3)
    newlist=p.map(square,range(1,101),3)
    print newlist


