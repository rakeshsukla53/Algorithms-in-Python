__author__ = 'rakesh'

#mutable and immutable. There are various things which we need to consider when define objects. How can we know whether
#the object is mutable or immutable. Here are few examples

def mutable():
    x = "Rakesh" #we know that strings are immutable
    y = x
    y = "Bikash" + x
    print x  #the value of x will not change because it is immutable
    print y  #different object

#mutable()

def immutable():
    x = [1,2,3,4]
    y = x
    y.append(7)
    print x  #the value of x will change since the list object is immutable


def immutable1():
    x = {}   #your dictionary is also immutable and and you can check through output
    x[1] = "rakesh"  #list assignment is simple here
    y = x
    y[2] = "Bikash"
    for key, value in x.iteritems():    #this function has to be used to iterative over key value pair in one way
        print key, value

#immutable()

immutable1()

