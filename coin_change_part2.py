__author__ = 'rakesh'

coins = [1, 5, 10, 15, 20, 30, 50]
sum = []
lent = len(coins) - 1

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

print coinsRequired(99)   #this approach is actually greedy approach





