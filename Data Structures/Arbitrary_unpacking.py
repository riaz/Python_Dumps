#Arbitrary Unpacking using *

records = [
        ('foo',1,2),
        ('bar','hello'),
        ('foo',3,4)
    ]

def do_foo(x,y):
    print ('foo',x,y)

def do_bar(s):
    print ('bar',s)

#Trick tag is the first val in the tuples, *args takes the rest
""" for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
"""

#Finding the sum of last but all

items = [1,2,3,4,5,6,7,8]

def avg(items):
    head,*others = items
    return sum(*others)/len(*others)

print "First but all Average : " . avg(items)
        
