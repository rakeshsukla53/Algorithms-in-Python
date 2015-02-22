__author__ = 'rakesh'


coins_available = [1, 5, 10, 15]
amount = 50
sum = []

def coinsRequired(n, x):

    if n >= 15:
        sum.append(15)
        coinsRequired(n-15, 15)
    elif n >= 10:
        sum.append(10)
        coinsRequired(n-10, 10)
    elif n >= 5:
        sum.append(5)
        coinsRequired(n-5, 5)
    elif n >= 1:
        sum.append(1)
        coinsRequired(n-1, 1)

    return sum

print coinsRequired(50, 15)   #the coin problem can be solved using greedy approach


