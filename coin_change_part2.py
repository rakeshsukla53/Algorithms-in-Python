__author__ = 'rakesh'

coins = [1, 5, 10, 21, 30]
sum = []
#lent = len(coins) - 1

def coinsRequired(n):
    global lent
    while (lent >= 0) and (n >= 0):

        if n >= coins[lent]:
            x = coins[lent]
            sum.append(x)
            coinsRequired(n-x)
        else:
            lent = lent - 1

    return sum


for i in range(0, len(coins)):
    lent = len(coins) - 1
    lent = lent - i
    sum = []
    print len(coinsRequired(63))   #this approach is actually dynamic approach which will be useful to select a
                                   #how any coins to choose
                                   #so 21 will be used instead of 30 coins which why it is called dynamic



