def ifeven(number):
    return (number/2)

def ifodd(number):
    return ((number*3)+1)

limit=int(raw_input("Enter the limit No: "))

for n in xrange(2,limit):
    ind=0
    while n !=1:
        ind+=1
        if n%2==0:
            #print n
            n=ifeven(n)
        else:
            #print n
            n=ifodd(n)
    print ind
