__author__ = 'rakesh'

coins = [1, 5, 15]
sum = []


def coinsRequired(n, lent):
    print n, lent
    while (lent >= 0) and (n >= 0):

        if n >= coins[lent]:
            print "hi"
            break
            x = coins[lent]
            sum.append(x)
            #coinsRequired(n-x, lent)
        else:
            lent = lent - 1

    return sum

#for i in range(0, len(coins)):
print coinsRequired(10, 2)   #this approach is actually dynamic approach



