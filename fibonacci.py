__author__ = 'rakesh'

a = []

#fibonacci using the recursion method
def Fibo(n):
    a.append(0)
    a.append(1)

    for i in range(2, n):
        a.append(a[i-1] + a[i-2])

    return a

print Fibo(100)

