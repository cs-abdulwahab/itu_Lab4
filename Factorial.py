# Recursive Functions
# n!  =  n *   (n-1)!
#  fact (n)   = n * fact(n-1)

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


def permutation(n, r):
    return fact(n) // fact(n - r)


def combination(n, r):
    return (fact(n) // ( fact(r) * fact(n - r) ))


# i = int(input("Enter First value "))
# j = int(input("Enter Second value "))
print(combination(16, 3))
