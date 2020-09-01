def is_multiple(x,y):
    '''is_multiple(x,y) -> bool
    returns True is x is a multiple of y, False otherwise
    x, y: int
    '''
    # check if y divides evenly into x
    return (x % y == 0) 

def sum_of_proper_divisors(x):
    '''sum_of_proper_divisors(x) -> int
    returns the sum of the proper divisors of x
    x: int
    '''
    # find every divisor of x from 1 to int(x/2), inclusive, and sum them up
    sumOfProperDivs = 0
    for div in range(1,int(x/2)+1):
        if is_multiple(x,div):
            sumOfProperDivs += div
    return sumOfProperDivs

# test cases
print(sum_of_proper_divisors(6))
print(sum_of_proper_divisors(28))
print(sum_of_proper_divisors(12))

# print a 3-digit number x equal to the sum of its proper divisors
for x in range(100,1000):
    if x == sum_of_proper_divisors(x):
        print(x)
